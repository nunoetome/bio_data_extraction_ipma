# -------------- worker_ipma_rss_bolsas.py --------------
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
# RSS NAME: Bolsas de investigação IPMA
# 
# -------------------change log -------------------------
# [2024-10-06] - [Nuno Tomé] - final alpha version
# [2024-10-07] - [Nuno Tomé] - final beta version


# ------------------- Description -------------------------
# This script downloads RSS data from IPMA and saves it to a file
# ------------------- info -------------------------
# its based on the original worker script from the room1:
# worker_ipma_rss_news.py - alpha version
# -------------------change log -------------------------
# version: alpha
# [2024-10-06] - [Nuno Tomé] - [Initial Version]
# changed: header



import os
import re
import feedparser
import requests
from logging_config import LOGGER
from datetime import datetime
import xml.etree.ElementTree as ET


# ----------------- In code constant definition -----------------

RSS_URL = "https://www.ipma.pt/resources.www/rss/rss.bolsas.ipma.xml"

DATASET_ID = 'ipma_rss_bolsas'
DATASET_DESCRIPTION = 'Dataset containing RSS data from IPMA'
DATASET_FOLDER = 'datasets/bolsas'
HISTORIC_FILE = 'datasets/bolsas/ipma_rss_bolsas_history.txt'

# ---------------------------------------------------------------

def __get_rss_items(rssResponse):
    # define whats the item looks like
    item_pattern = re.compile(r'<item>.*?</item>', re.DOTALL)
    # find all occurrences of <item>...</item> with content 
    # between them
    items = re.findall(item_pattern, rssResponse)
            
    return items

def __get_rss_header(rssResponse):
    # define whats the item looks like
    item_pattern = re.compile(r'<item>.*?</item>', re.DOTALL)
    
    # Remove all occurrences of <item>...</item> with content 
    # between them
    cleaned_data = re.sub(item_pattern, '', rssResponse)
            
    return cleaned_data


# This function selects all unprocessed files in the folder, filters 
# them to only the xml files, then filters them to only the ones
# that start with the dataset id (original files), then filters
# off the ones are compiled files
def __get_all_basic_dataset_files():
    # select all files in the folder
    all_files = os.listdir(DATASET_FOLDER)
    #filter the files to only the xml files
    all_files = [f for f in all_files if f.endswith('.xml')]
    # filter the files to only the ones that start with the dataset id (original files)
    all_files = [f for f in all_files if f.startswith('ipma_rss_bolsas')]
    # filter the files to only the ones that start with the dataset id and have the word compiled
    # this is to avoid compiling the compiled files
    all_files = [f for f in all_files if not f.startswith('ipma_rss_bolsas_compiled')]
    return all_files
    
def __get_all_compiled_dataset_files():   
    # select all files in the folder
    all_files = os.listdir(DATASET_FOLDER)
    #filter the files to only the xml files
    all_files = [f for f in all_files if f.endswith('.xml')]
    # filter compiled files
    all_files = [f for f in all_files if f.startswith('ipma_rss_bolsas_compiled')]
    return all_files

#TODO: implement this function 
def __is_header_duplicate(header, all_compiled_dataset_files):
    return False

#TODO: #1 implement this function __generate_rss_compiled_file_name ()
def __generate_rss_compiled_file_name ():
    return 'teste.xml'

# this function adds the items to the identified file
def __add_items_to_compiled_file(file_name, items):
    compiled_file_name = __generate_rss_compiled_file_name ()
    #Duvda: o filename ta correcto?
    compiled_file_path = os.path.join(DATASET_FOLDER, compiled_file_name)
    
    try:
        # Open the compiled file and read its content
        with open(compiled_file_path, 'r') as f:
            compiled_data = f.read()
        
        # Parse the compiled data
        compiled_tree = ET.ElementTree(ET.fromstring(compiled_data))
        compiled_root = compiled_tree.getroot()
        
        # Add new items to the compiled file
        for item in items:
            compiled_root.find('.//channel').append(ET.fromstring(item))
        
        # Save the updated compiled file
        compiled_tree.write(compiled_file_path, encoding='utf-8', xml_declaration=True)
        LOGGER.info(f"Items added to compiled file {compiled_file_path}")
    
    except FileNotFoundError:
        LOGGER.error(f"Compiled file {compiled_file_path} not found")
    except ET.ParseError as e:
        LOGGER.error(f"Failed to parse compiled file {compiled_file_path}: {e}")
    except Exception as e:
        LOGGER.error(f"Failed to add items to compiled file {compiled_file_path}: {e}")
    pass

def __create_new_compiled_file(header, items):
    compiled_file_name = __generate_rss_compiled_file_name ()
    compiled_file_path = os.path.join(DATASET_FOLDER, compiled_file_name)
    
    try:
        # Create a new XML tree with the header
        compiled_tree = ET.ElementTree(ET.fromstring(header))
        compiled_root = compiled_tree.getroot()
        
        # Add new items to the compiled file
        for item in items:
            compiled_root.find('.//channel').append(ET.fromstring(item))
        
        # Save the new compiled file
        compiled_tree.write(compiled_file_path, encoding='utf-8', xml_declaration=True)
        LOGGER.info(f"New compiled file {compiled_file_path} created")
    except Exception as e:
        LOGGER.error(f"Failed to create new compiled file {compiled_file_path}: {e}")
    pass  
    
#this function picks up the RSS data from all files in the folder
# and compiles it into a single file, removing duplicates
# if the file is empty, it is discarded
# if the header changed, 2 files are created, one with the old header
def compile_all_rss_data():    
    LOGGER.info(f"Compiling RSS data from {RSS_URL}")
    
    # select all files in the folder
    all_basic_dataset_files = __get_all_basic_dataset_files()
    LOGGER.info(f"Found {len(all_basic_dataset_files)} files to compile")   
    
    # for each file, define the header of the dataset file as 
    # all the data from the file but the <item> tags and their 
    # content
    ## header = ''
    ## item_pattern = re.compile(r'<item>.*?</item>', re.DOTALL)
    for file_name in all_basic_dataset_files:
        LOGGER.debug(f"Processing file {file_name}")
        
        file_path = os.path.join(DATASET_FOLDER, file_name)
        LOGGER.debug(f"Reading file {file_path}")
        # Open the file and read the content
        #TODO: try except
        with open(file_path, 'r') as f:
            data = f.read()
        LOGGER.debug(f"File {file_name} read, {len(data)} bytes")
        
        #TODO: if the file is empty, it is discarded
                
        # separate the header from the items
        header = __get_rss_header (data)
        LOGGER.debug(f"Header extracted from file {file_name}, {len(header)} bytes")
        items = __get_rss_items(data)
        LOGGER.debug(f"Items extracted from file {file_name}, {len(items)} items")
        
        # if the file has no items, it is discarded
        if len(items) == 0:
            os.remove(file_path)
            LOGGER.warning(f"Empty file {file_name} discarded")
            continue
        
        # get all compiled files
        all_compiled_dataset_files = __get_all_compiled_dataset_files ()
        LOGGER.debug(f"Found {len(all_compiled_dataset_files)} compiled files")
        
        # manage header changes
        is_header_duplicate = __is_header_duplicate(header, all_compiled_dataset_files)
        LOGGER.debug(f"Header duplicate: {is_header_duplicate}")
        if is_header_duplicate:
            #adds the items to the identified file
            __add_items_to_compiled_file(file_name, items)
            LOGGER.debug(f"Items added to compiled file {file_name}")
        else:
            #creates a new file
            __create_new_compiled_file(header, items)
            LOGGER.debug(f"New compiled file created")
    pass
    
# Test function
# This shold no be used in production
# FOR DEBUGGING ONLY
if __name__ == '__main__':
    #TODO: alterar o nome do ficheiro
    LOGGER.warning(f">>>> Starting SELF RUNNING TEST for {__name__} <<<<")
    compile_all_rss_data()
    LOGGER.warning(f">>>> Ending SELF RUNNING TEST for {__name__} <<<<")