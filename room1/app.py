# app.py

# - Description: 
# - This is the main file of the application. 
# - It is responsible for starting the application and 
# calling the necessary functions to download the data 
# from IPMA and extract the information from it.
# -------------------change log -------------------------
# [2024-10-04] - [Nuno Tomé] - [Initial Version]
# [2024-10-06] - [Nuno Tomé] - final alpha version

import json
from logging_config import LOGGER, ini_logging
from worker_ipma_rss_comunicados import download_ipma_rss_comunicados
#from impa_rss import download_ipma_rss_comunicados

SETTINGS_FILE_PATH = 'settings.json'

#todo: implementar a leitura do ficheiro de configuração
def load_settings():
    with open(SETTINGS_FILE_PATH, 'r') as file:
        settings = json.load(file)
    return settings

def main():
    ini_logging()
    LOGGER.info(">>>>>>>>> Starting application IPMA RSS downloader <<<<<<<<<")
    download_ipma_rss_comunicados()
    #todo: implementar outros RSS
    LOGGER.info(">>>>>>>>> Application finished <<<<<<<<<")
    
if __name__ == '__main__':
    main()