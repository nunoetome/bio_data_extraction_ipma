# app.py

# Description: Main application file

#import logging
import json
#import configparser
from logging_config import LOGGER, ini_logging
from impa_rss import downloadImaRssComunicados
#from impa_rss import extractRssInfo

SETTINGS_FILE_PATH = 'settings.json'

def load_settings():
    with open(SETTINGS_FILE_PATH, 'r') as file:
        settings = json.load(file)
    return settings

def main():
    #settings = load_settings()
    ini_logging()
    LOGGER.info(">>>>>>>>> Starting application <<<<<<<<<")
    downloadImaRssComunicados()
    #LOGGER.debug(f"Settings: {settings}".encode('utf-8'))
    #extractRssInfo()
    
    
if __name__ == '__main__':
    main()