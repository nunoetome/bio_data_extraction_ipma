# -------------- worker_ipma_api_av_met_3.py --------------
#
#TODO: #2 review the heather for worker_ipma_api_av_met_3.py
# ------------------- Description -------------------------
# This script downloads api data from IPMA and saves it to a file
# It es part of a set of scripts dedicated to IPMA, and very similar
# between them, with some changes in the constants and the 
# functions that are called, as much as some minor customizations.
#
# This is part of the application "bio_data_data_extraction_ipma",
# https://github.com/nunoetome/bio_data_extraction_ipma_legacy,
# and it part a larger scope project that aims to extract 
# data from various sources and store it in a database for 
# scientific and technological research purposes.
#
# ------------------- info -------------------------
# Category: Worker
# api NAME: Avisos Meteorológicos até 3 dias
# -------------------change log -------------------------
# [2024-10-06] - [Nuno Tomé] - final alpha version
# [2024-10-07] - [Nuno Tomé] - final beta version


# ------------------- Description -------------------------
# This script downloads api data from IPMA and saves it to a file
# ------------------- info -------------------------
# its based on the original worker script from the room1:
# worker_ipma_api_news.py - alpha version
# -------------------change log -------------------------
# version: alpha
# [2024-10-06] - [Nuno Tomé] - [Initial Version]
# changed: header



#import feedparser
from datetime import datetime
import requests
from logging_config import LOGGER
#from datetime import datetime
#import xml.etree.ElementTree as ET
import json


# ----------------- In code constant definition -----------------

API_URL = "https://api.ipma.pt/open-data/forecast/warnings/warnings_www.json"

DATASET_ID = 'ipma_api_av_met_3'
DATASET_DESCRIPTION = 'Dataset containing api data from IPMA'
DATASET_FOLDER = 'datasets/av_met_3'
HISTORIC_FILE = 'datasets/av_met_3/ipma_api_av_met_3_history.txt'

# ---------------------------------------------------------------

# Generate a file name for the api data
def __generate_api_file_name (dataset_name):
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    LOGGER.debug("Current date and time: %s", current_time)
    file_name = f"{dataset_name}_{current_time}.xml"
    LOGGER.debug("Dataset name: %s", dataset_name)
    LOGGER.info("File name: %s", file_name)
    return file_name



# Main function, the one that is called by the exterior
# This function is responsible for downloading api information
# from IPMA and saving it to a file
def worker_ipma_api_av_met_3():
    LOGGER.info("Downloading api data from %s", DATASET_ID)
    
    try:
        # Downloads the content from the API
        api_response = requests.get(API_URL, timeout=10)
        api_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        LOGGER.error("Failed to download API from %s: %s", API_URL, e)
        return
    LOGGER.debug("API Response: %s", api_response)

    #TODO: #3 verify and expunge duplicated information
    # Save the content to a file
    file_name = __generate_api_file_name(DATASET_ID)
    try:
        file_path = f"{DATASET_FOLDER}/{file_name}"
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(api_response.json()))
    except (IOError, OSError, json.JSONDecodeError) as e:
        LOGGER.error("Failed to save API data to file %s: %s", file_name, e)
        return



 
# Test function
# This is not going to used in production
# FOR DEBUGGING ONLY
if __name__ == '__main__':
    LOGGER.warning(">>>> Starting SELF RUNNING TEST for %s <<<<", __name__)
    worker_ipma_api_av_met_3()
    LOGGER.warning(">>>> Ending SELF RUNNING TEST for %s <<<<", __name__)
