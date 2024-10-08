# -------------- worker_ipma_rss_mobilidade.py --------------
#
# ------------------- Description -------------------------
# This script downloads RSS data from IPMA and saves it to a file
# It es part of a set of scripts dedicated to IPMA, and very similar
# between them, with some changes in the constants and the 
# functions that are called, as much as some minor customizations.
#
# This is part of the application "bio_data_data_extraction_ipma",
# https://github.com/nunoetome/bio_data_extraction_ipma_legacy,
# and it part a larger scope project that aims to extract 
# data from various sources and store it in a database for 
# cientific and technological research purposes.
#
# ------------------- info -------------------------
# Category: Worker
# RSS NAME: Procedimentos por mobilidade IPMA
# 
# -------------------change log -------------------------
# [2024-10-06] - [Nuno Tomé] - final alpha version
# [2024-10-07] - [Nuno Tomé] - final beta version

import feedparser
import requests
from logging_config import LOGGER
from datetime import datetime
import xml.etree.ElementTree as ET


# ----------------- In code constant definition -----------------

RSS_URL = "https://www.ipma.pt/pt/produtoseservicos/rss/rss.mobilidade.xml"

DATASET_ID = 'ipma_rss_mobilidade'
DATASET_DESCRIPTION = 'Dataset containing RSS data from IPMA'
DATASET_FOLDER = 'datasets/mobilidade'
HISTORIC_FILE = 'datasets/mobilidade/ipma_rss_mobilidade_history.txt'

# ---------------------------------------------------------------


# Função para fazer o download dos anexos
# Esta função recebe um item do XML e faz o download do anexo
# associado a esse item
# so esta testado num unico item
def __download_item_atachments(item):
    
    LOGGER.debug("Downloading item atachments")
    link = item.find('link').text
    response = requests.get(link)
    LOGGER.debug(f"Downloaded attachment from {link}")
    
    # Get the publication date and format it to be used 
    # in the file name
    # then replace the spaces and colons with underscores
    #pub_date = item.find('pubDate').text.replace(" ", "_").replace(":", "-")
    pub_date = datetime.strptime(item.find('pubDate').text, "%a, %d %b %Y %H:%M:%S %Z").strftime("%Y%m%d-%H%M")

    if response.status_code == 200:
        file_name = pub_date + '-' + link.split('/')[-1]
        output_file = DATASET_FOLDER + '/' + DATASET_ID+ file_name
        with open(output_file, 'wb') as file:
            file.write(response.content)
        LOGGER.info(f"Attachment saved to {output_file}")
    else:
        LOGGER.error(f"Failed to download attachment from {link}, status code: {response.status_code}")
    return output_file


def __download_rss_atachments(rssResponse):
    items = rssResponse.findall('.//item')
    for item in items:
        output_file = __download_item_atachments(item)
        # Create a new element <link-internal> and set its text 
        # to the output file path
        item_link_internal = ET.Element('link-internal')
        item_link_internal.text = output_file
        
        # Append the new element to the current item
        item.append(item_link_internal)
    pass



def __item_counter(rssResponse):
    # Conta o numero deitens no XML 
    items = rssResponse.findall('.//item')
    LOGGER.debug(f"Numero de itens no XML: {len(items)}")
    return len(items)

# Verificar se o item já foi descarregado
def __is_duplicate(item):
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

def __records_items_in_history(item):
    # Identifys the item by link + pubDate
    pub_date = item.find('pubDate').text
    LOGGER.debug(f"PubDate do item: {pub_date}")
    link = item.find('link').text
    LOGGER.debug(f"Link do item: {link}")
    validation = f"{link} - {pub_date}"
    with open(HISTORIC_FILE, 'a') as file:
        file.write(f"{validation}\n")
    pass

def __records_rss_file_in_history(rssResponse):
    # Encontrar todos os itens no XML
    items = rssResponse.findall('.//item')
    
    # Iterar sobre os itens e registar aqueles que ainda 
    # não estão no histórico
    for item in items:
        __records_items_in_history(item)
    pass


#********* NEW CODE *********
# Todo: dar nome inetressante a esta função
# algo com estilo tipo uma personagem do cinema ou da banda desenhada
# que tenha a capacidade de detetar duplicados ou de eliminalos.
# ALERTA: possibilidade de haver um bug nesta função
# por poder estar a haver um equivoco entre s estamos a  retornar 
def __purge_duplicate (xmlAPorgar):
    # Encontrar todos os itens no XML
    thisXmlAPorgar = xmlAPorgar
    items = thisXmlAPorgar.findall('.//item')        
   
    for item in items:
     
      if __is_duplicate(item):
        LOGGER.error(f"Item {item.find('pub_date')} já foi descarregado")
        thisXmlAPorgar.find('.//channel').remove(item)
        LOGGER.info(f"Item {item.find('pub_date')} removido")
      else:
        LOGGER.info(f"Item {item.find('pub_date')} ainda não tinha sido descarregado")
    LOGGER.debug(f"XML LIMPO {thisXmlAPorgar}")
    return thisXmlAPorgar

def __generate_rss_file_name (datasetName):
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    LOGGER.debug(f"Data e hora atual: {current_time}")
    LOGGER.debug(f"Nome do dataset: {datasetName}")
    fileName = f"{datasetName}_{current_time}.xml"
    LOGGER.info(f"A dar nome ao ficheiro do dataset: {fileName}")
    return fileName

def __save_rss_data_to_file(cleanedResponse, datasetName):
    LOGGER.debug(f"Saving RSS data to file datasetName: {datasetName}")
    # Save the cleaned XML to a file
    fileName = __generate_rss_file_name(datasetName)
    LOGGER.debug(f"Nome do ficheiro: {fileName}")
    
    output_file = DATASET_FOLDER + '\\' + fileName
    
    LOGGER.debug(f"Nome do ficheiro com caminho: {output_file}")
    with open(output_file, 'wb') as file:
        file.write(ET.tostring(cleanedResponse, encoding='utf-8', method='xml'))
    LOGGER.info(f"Cleaned RSS data saved to {output_file}")



def download_ipma_rss_mobilidade():
    LOGGER.info("Downloading RSS data from IPMA")
    
    # Faz o download do conteúdo do RSS
    rssResponse = requests.get(RSS_URL)
    parcedRss = ET.fromstring(rssResponse.text)
    
    LOGGER.debug(f"Parced RSS: {parcedRss}")
    cleanedResponse = __purge_duplicate (parcedRss)
    LOGGER.debug(f"Cleaned Response: {cleanedResponse}")
    
    if __item_counter(cleanedResponse) == 0:
        LOGGER.info("NO NEW ITEMS TO DOWNLOAD, file discarded") 
        return
    else:
        __download_rss_atachments (cleanedResponse)
        __save_rss_data_to_file(cleanedResponse, DATASET_ID)
        __records_rss_file_in_history(cleanedResponse)
    pass
    

# Test function
# This shold no be used in production
if __name__ == '__main__':
    download_ipma_rss_mobilidade()