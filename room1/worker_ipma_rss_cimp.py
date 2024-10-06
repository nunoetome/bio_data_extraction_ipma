# ------------------- Description -------------------------
# This script downloads RSS data from IPMA and saves it to a file
# ------------------- info -------------------------
# its based on the original worker script from the room1:
# worker_ipma_rss_news.py - alpha version
# -------------------change log -------------------------
# version: alpha
# [2024-10-06] - [Nuno Tomé] - [Initial Version]
# changed: header



import feedparser
import requests
from logging_config import LOGGER
from datetime import datetime
import xml.etree.ElementTree as ET


# ----------------- In code constant definition -----------------

RSS_URL = "https://www.ipma.pt/resources.www/rss/rss.cimp.ipma.xml"

DATASET_ID = 'ipma_rss_cimp'
DATASET_DESCRIPTION = 'Dataset containing RSS data from IPMA - (rss_cimp)'
DATASET_FOLDER = 'datasets'
HISTORIC_FILE = 'datasets\ipma_rss_cimp_history.txt'

# ---------------------------------------------------------------

def item_counter(rssResponse):
    # Conta o numero deitens no XML 
    items = rssResponse.findall('.//item')
    LOGGER.debug(f"Numero de itens no XML: {len(items)}")
    return len(items)

# Verificar se o item já foi descarregado
def is_duplicate(item):
    LOGGER.debug("Verificando se o item já foi descarregado")
    # Identifys the item by link + pubDate
    pub_date = item.find('pubDate').text
    LOGGER.debug(f"PubDate do item: {pub_date}")
    link = item.find('link').text
    LOGGER.debug(f"Link do item: {link}")
    validation = f"{link} - {pub_date}"
    with open(HISTORIC_FILE, 'r') as file:
        for line in file:
            if line.strip() == validation:
                return True
    return False

def records_items_in_history(item):
    # Identifys the item by link + pubDate
    pub_date = item.find('pubDate').text
    LOGGER.debug(f"PubDate do item: {pub_date}")
    link = item.find('link').text
    LOGGER.debug(f"Link do item: {link}")
    validation = f"{link} - {pub_date}"
    with open(HISTORIC_FILE, 'a') as file:
        file.write(f"{validation}\n")
    pass

def records_rss_file_in_history(rssResponse):
    # Encontrar todos os itens no XML
    items = rssResponse.findall('.//item')
    
    # Iterar sobre os itens e registar aqueles que ainda 
    # não estão no histórico
    for item in items:
        records_items_in_history(item)
    pass


#********* NEW CODE *********
# Todo: dar nome inetressante a esta função
# algo com estilo tipo uma personagem do cinema ou da banda desenhada
# que tenha a capacidade de detetar duplicados ou de eliminalos.
# ALERTA: possibilidade de haver um bug nesta função
# por poder estar a haver um equivoco entre s estamos a  retornar 
def purge_duplicate (xmlAPorgar):
    # Encontrar todos os itens no XML
    thisXmlAPorgar = xmlAPorgar
    items = thisXmlAPorgar.findall('.//item')        
   
    for item in items:
     
      if is_duplicate(item):
        LOGGER.error(f"Item {item.find('pub_date')} já foi descarregado")
        thisXmlAPorgar.find('.//channel').remove(item)
        LOGGER.info(f"Item {item.find('pub_date')} removido")
      else:
        LOGGER.info(f"Item {item.find('pub_date')} ainda não tinha sido descarregado")
    LOGGER.debug(f"XML LIMPO {thisXmlAPorgar}")
    return thisXmlAPorgar

def generate_rss_file_name (datasetName):
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    LOGGER.debug(f"Data e hora atual: {current_time}")
    LOGGER.debug(f"Nome do dataset: {datasetName}")
    fileName = f"{datasetName}_{current_time}.xml"
    LOGGER.info(f"A dar nome ao ficheiro do dataset: {fileName}")
    return fileName

def save_rss_data_to_file(cleanedResponse, datasetName):
    LOGGER.debug(f"Saving RSS data to file datasetName: {datasetName}")
    # Save the cleaned XML to a file
    fileName = generate_rss_file_name(datasetName)
    LOGGER.debug(f"Nome do ficheiro: {fileName}")
    
    output_file = DATASET_FOLDER + '\\' + fileName
    
    LOGGER.debug(f"Nome do ficheiro com caminho: {output_file}")
    with open(output_file, 'wb') as file:
        file.write(ET.tostring(cleanedResponse, encoding='utf-8', method='xml'))
    LOGGER.info(f"Cleaned RSS data saved to {output_file}")



def download_ipma_rss_cimp():
    LOGGER.info("Downloading RSS data from IPMA")
    
    # Faz o download do conteúdo do RSS
    rssResponse = requests.get(RSS_URL)
    parcedRss = ET.fromstring(rssResponse.text)
    
    LOGGER.debug(f"Parced RSS: {parcedRss}")
    cleanedResponse = purge_duplicate (parcedRss)
    LOGGER.debug(f"Cleaned Response: {cleanedResponse}")
    
    if item_counter(cleanedResponse) == 0:
        LOGGER.info("NO NEW ITEMS TO DOWNLOAD, file discarded") 
        return
    else:
        save_rss_data_to_file(cleanedResponse, DATASET_ID)
        records_rss_file_in_history(cleanedResponse)
    pass
    

# Test function
# This shold no be used in production
if __name__ == '__main__':
    download_ipma_rss_cimp()