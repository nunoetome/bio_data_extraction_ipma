import feedparser
import requests
from logging_config import LOGGER
from datetime import datetime
import xml.etree.ElementTree as ET


# ----------------- In code constant definition -----------------

# --- RSS URL 1 ---
# RSS URL
# TEST_RSS_URL = "test_rss\ipma_rss_comunicados.xml"
# RSS_URL = TEST_RSS_URL
RSS_URL = "https://www.ipma.pt/resources.www/rss/comunicados.xml"

DATASET_ID = 'ipma_rss_comunicados'
DATASET_DESCRIPTION = 'Dataset containing RSS data from IPMA'
DATASET_FOLDER = 'datasets'
HISTORIC_FILE = 'datasets\ipma_rss_comunicados_historico.txt'

# ---------------------------------------------------------------


def itemCounter(rssResponse):
    # Conta o numero deitens no XML 
    items = rssResponse.findall('.//item')
    LOGGER.debug(f"Numero de itens no XML: {len(items)}")
    return len(items)


# Verificar se o item já foi descarregado
def isDuplicate(item):
    LOGGER.debug("Verificando se o item já foi descarregado")
    # Identifica o item por pubDate
    pub_date = item.find('pubDate').text
    LOGGER.debug(f"PubDate do item: {pub_date}")
    with open(HISTORIC_FILE, 'r') as file:
        for line in file:
            if line.strip() == pub_date:
                return True
    return False

def registaItemEmHistorico(item):
    #LOGGER.debug(f"Registando item {item.find('title').text} no histórico")
    
    pub_date = item.find('pubDate').text
    with open(HISTORIC_FILE, 'a') as file:
        file.write(f"{pub_date}\n")
        #LOGGER.debug(f"Item {item.find('title').text} pubDate: {pub_date}  registado com data {pub_date}")
    pass

def registaEmHistorico(rssResponse):
    # Encontrar todos os itens no XML
    items = rssResponse.findall('.//item')
    #LOGGER.debug(f"Items: {items}")
    
    # Iterar sobre os itens e registar aqueles que ainda não estão no histórico
    for item in items:
        #if not isDuplicate(item):
        registaItemEmHistorico(item)
    pass


#********* NEW CODE *********
# Todo: dar nome inetressante a esta função
# algo com estilo tipo uma personagem do cinema ou da banda desenhada
# que tenha a capacidade de detetar duplicados ou de eliminalos.
# ALERTA: possibilidade de haver um bug nesta função
# por poder estar a haver um equivoco entre s estamos a  retornar 
def expurgaDuplicados (xmlAPorgar):
    # Encontrar todos os itens no XML
    thisXmlAPorgar = xmlAPorgar
    items = thisXmlAPorgar.findall('.//item')        
   
    # Iterar sobre os itens e remover aqueles que são duplicados em relação
    # ao histórico da totalidade dos itens já descarregados, não apenas os
    # que estão no XML atual
    for item in items:
  
      
      if isDuplicate(item):
        LOGGER.error(f"Item {item.find('pub_date')} já foi descarregado")
        thisXmlAPorgar.find('.//channel').remove(item)
        LOGGER.info(f"Item {item.find('pub_date')} removido")
      else:
        LOGGER.info(f"Item {item.find('pub_date')} ainda não tinha sido descarregado")
    LOGGER.debug(f"XML LIMPO {thisXmlAPorgar}")
    return thisXmlAPorgar

def darNomeAoFicheiro (datasetName):
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    LOGGER.debug(f"Data e hora atual: {current_time}")
    LOGGER.debug(f"Nome do dataset: {datasetName}")
    fileName = f"{datasetName}_{current_time}.xml"
    LOGGER.info(f"A dar nome ao ficheiro do dataset: {fileName}")
    return fileName

def saveRssDataToFile(cleanedResponse, datasetName):
    LOGGER.debug(f"Saving RSS data to file datasetName: {datasetName}")
    # Save the cleaned XML to a file
    #output_file = r'datasets\cleaned_ipma_rss_comunicados.xml'
    fileName = darNomeAoFicheiro(datasetName)
    LOGGER.debug(f"Nome do ficheiro: {fileName}")
    
    output_file = DATASET_FOLDER + '\\' + fileName
    
    LOGGER.debug(f"Nome do ficheiro com caminho: {output_file}")
    with open(output_file, 'wb') as file:
        file.write(ET.tostring(cleanedResponse, encoding='utf-8', method='xml'))
    LOGGER.info(f"Cleaned RSS data saved to {output_file}")



def downloadImaRssComunicados():
    LOGGER.info("Downloading RSS data from IPMA")
    
    # Faz o download do conteúdo do RSS
    rssResponse = requests.get(RSS_URL)
    parcedRss = ET.fromstring(rssResponse.text)
    # Parse the XML
    #LOGGER.debug(f"RSS Response: {rssResponse.content}")
    #parcedRss = ET.fromstring(rssResponse)
    LOGGER.debug(f"Parced RSS: {parcedRss}")
    cleanedResponse = expurgaDuplicados (parcedRss)
    LOGGER.debug(f"Cleaned Response: {cleanedResponse}")
    
    if itemCounter(cleanedResponse) == 0:
        LOGGER.info("NO NEW ITEMS TO DOWNLOAD, file discarded") 
        return
    else:
        saveRssDataToFile(cleanedResponse, DATASET_ID)
        registaEmHistorico(cleanedResponse)
    pass
    
    
if __name__ == '__main__':
    downloadImaRssComunicados()