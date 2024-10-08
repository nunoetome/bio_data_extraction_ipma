# ------------------------- app.py -------------------------
#
# ------------------- Description -------------------------
# This is the main file of the application. 
#
# It is responsible for starting the application and 
# calling the necessary functions to download the data 
# from IPMA RSS sources and extract the information from it.
# ------------------- info -------------------------
# this starts:
# - download_ipma_rss_comunicados
# - download_ipma_rss_cimp
# - download_ipma_rss_comuns
# - download_ipma_rss_dirigentes
# - download_ipma_rss_investigacao
# - download_ipma_rss_mobilidade
# - download_ipma_rss_news
# - download_ipma_rss_bolsas
# -------------------change log -------------------------
# [2024-10-04] - [Nuno Tomé] - [Initial Version]
# [2024-10-06] - [Nuno Tomé] - final alpha version
# [2024-10-07] - [Nuno Tomé] - final beta version

import json
from logging_config import LOGGER, ini_logging
from worker_ipma_rss_bolsas import download_ipma_rss_bolsas
from worker_ipma_rss_news import download_ipma_rss_news
from worker_ipma_rss_mobilidade import download_ipma_rss_mobilidade
from worker_ipma_rss_investigacao import download_ipma_rss_investigacao
from worker_ipma_rss_dirigentes import download_ipma_rss_dirigentes
from worker_ipma_rss_comuns import download_ipma_rss_comuns
from worker_ipma_rss_cimp import download_ipma_rss_cimp
from worker_ipma_rss_comunicados import download_ipma_rss_comunicados

SETTINGS_FILE_PATH = 'settings.json'

#todo: use this function to load the settings
def load_settings():
    with open(SETTINGS_FILE_PATH, 'r') as file:
        settings = json.load(file)
    return settings

def main():
    ini_logging()
    LOGGER.info(">>>>>>>>> Starting application IPMA RSS downloader <<<<<<<<<")
    
    LOGGER.debug("starting download_ipma_rss_comunicados")
    download_ipma_rss_comunicados()
    LOGGER.debug("finished download_ipma_rss_comunicados")
    
    LOGGER.debug("starting download_ipma_rss_cimp")
    download_ipma_rss_cimp()
    LOGGER.debug("finished download_ipma_rss_cimp") 
    
    LOGGER.debug("starting download_ipma_rss_comuns")
    download_ipma_rss_comuns()
    LOGGER.debug("finished download_ipma_rss_comuns")
    
    LOGGER.debug("starting download_ipma_rss_dirigentes")
    download_ipma_rss_dirigentes()
    LOGGER.debug("finished download_ipma_rss_dirigentes")
    
    LOGGER.debug("starting download_ipma_rss_investigacao")
    download_ipma_rss_investigacao()
    LOGGER.debug("finished download_ipma_rss_investigacao")
    
    LOGGER.debug("starting download_ipma_rss_mobilidade")
    download_ipma_rss_mobilidade()
    LOGGER.debug("finished download_ipma_rss_mobilidade")
    
    LOGGER.debug("starting download_ipma_rss_news")
    download_ipma_rss_news()
    LOGGER.debug("finished download_ipma_rss_news")
    
    LOGGER.debug("starting download_ipma_rss_bolsas")
    download_ipma_rss_bolsas()
    LOGGER.debug("finished download_ipma_rss_bolsas")
  
    LOGGER.info(">>>>>>>>> Application finished <<<<<<<<<")

if __name__ == '__main__':
    main()