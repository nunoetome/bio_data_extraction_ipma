import feedparser
import requests
from logging_config import LOGGER
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
HISTORIC_FILE = DATASET_FOLDER+'\\'+'ipma_rss_comunicados_historico.txt'

# ---------------------------------------------------------------

# Verificar se o item já foi descarregado
def isDuplicate(item):
    LOGGER.debug(f"Verificando se item {item.find('title').text} já foi descarregado")
    # Identifica o item por pubDate
    pub_date = item.find('pubDate').text
    with open(HISTORIC_FILE, 'r') as file:
        for line in file:
            if line.strip() == pub_date:
                return True
    return False

def registaEmHistorico(item):
    LOGGER.debug(f"Registando item {item.find('title').text} no histórico")
    
    pub_date = item.find('pubDate').text
    with open(HISTORIC_FILE, 'a') as file:
        file.write(f"{pub_date}\n")
        LOGGER.info(f"Item {item.find('title').text} pubDate: {pub_date}  registado com data {pub_date}")
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
    LOGGER.debug(f"Items: {items}")
    
    # Iterar sobre os itens e remover aqueles que são duplicados em relação
    # ao histórico da totalidade dos itens já descarregados, não apenas os
    # que estão no XML atual
    for item in items:
      LOGGER.info(f"A tratar item {item.find('title').text} com data {item.find('pubDate').text}")
      
      if isDuplicate(item):
        LOGGER.info(f"Item {item.find('title').text} já foi descarregado")
        root.find('.//channel').remove(item)
        
        LOGGER.info(f"Item {item.find('title').text} removido")
      else:
        LOGGER.info(f"Item {item.find('title').text} não foi descarregado")
    return xmlAPorgar


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
    pass
    
    
if __name__ == '__main__':
    downloadImaRssComunicados()