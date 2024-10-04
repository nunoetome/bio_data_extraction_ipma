import feedparser
import requests
from logging_config import LOGGER




# ----------------- In code constant definition -----------------

# --- RSS URL 1 ---
# RSS URL
TEST_RSS_URL = "test_rss\ipma_rss_comunicados.xml"
RSS_URL = TEST_RSS_URL
#RSS_URL = "https://www.ipma.pt/resources.www/rss/comunicados.xml"

DATASET_ID = 'ipma_rss_comunicados'
DATASET_DESCRIPTION = 'Dataset containing RSS data from IPMA'



# ---------------------------------------------------------------


# ----------------- TEST FILE EXTRACTION -----------------
# This functions extracts the RSS information to a test files
# This is useful so copilot can work with the test file and
# not with the actual RSS feed, been able to run the code
# in the local environment

# --- RSS URL 1 ---
def extractRssInfoToTestFile():
    
    # Faz o download do conteúdo do RSS
    response = requests.get(RSS_URL)

    # Verifica se o download foi bem-sucedido
    if response.status_code == 200:
        # Grava o conteúdo em um ficheiro
        with open( TEST_RSS_URL, 'wb') as file:
            file.write(response.content)
        LOGGER.info(f"RSS feed gravado com sucesso:{TEST_RSS_URL}" )
    else:
        LOGGER.error(f"Erro ao acessar o RSS feed: {response.status_code}")
        LOGGER.error(f"URL: {RSS_URL}")
        LOGGER.error(f"Conteúdo: {response.content}")
        LOGGER.error(f"TEST_RSS_URL: {TEST_RSS_URL}")
# ---------------------------------------------------------------

# ----------------- REAL RSS EXTRACTION -----------------
def extractRssInfo():
    
    # Faz o parsing do feed
    feed = feedparser.parse(RSS_URL)
    #feed.encoding = 'us-ascii'
    #extractRssInfoToTestFile()        
    
    # Verifica se há algum erro no processamento do feed
    # Se houver, exibe o erro
    if feed.bozo:
        LOGGER.error(f"Erro ao processar o feed: {feed.bozo_exception}")
 
    
    # Exibe algumas informações sobre o feed
    print(f"Título do Feed: {feed.feed.title}")
    #for entry in feed.entries:
    #    print(f"{key}\n")
    #    for key in entry.keys():
    #        #print(f"{key}: {entry[key]}")
    #        print(f"{key}\n")
    for key in feed.keys():
        print(f"{key}\n")    

        #print('--------------------')
        #print(f"entry: {entry}")
        #for key in entry.keys():
        #    print(f"{key}: {entry[key]}")


#def cleanRssDuplicateInfo():
    
    
def downloadRssFile():
    # Faz o download do conteúdo do RSS
    response = requests.get(RSS_URL)

    # Verifica se o download foi bem-sucedido
    if response.status_code == 200:
        # Grava o conteúdo em um ficheiro
        with open( TEST_RSS_URL, 'wb') as file:
            file.write(response.content)
        LOGGER.info(f"RSS feed gravado com sucesso:{TEST_RSS_URL}" )
    else:
        LOGGER.error(f"Erro ao acessar o RSS feed: {response.status_code}")
        LOGGER.error(f"URL: {RSS_URL}")
        LOGGER.error(f"Conteúdo: {response.content}")
        LOGGER.error(f"TEST_RSS_URL: {TEST_RSS_URL}")
# ---------------------------------------------------------------


    
    
