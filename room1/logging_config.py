# - This file is part of the project "bio_data_data_extraction_ipma" 
# and was created by the project organization.


import logging
import inspect
import os


# ----------------- LOG CONFIGURATION -----------------
#
# Config here the logging level
# Just uncomment the desired level and comment the others

LOG_LEVEL_GLOBAL = logging.DEBUG
#LOG_LEVEL_GLOBAL = logging.INFO
#LOG_LEVEL_GLOBAL = logging.WARNING
#LOG_LEVEL_GLOBAL = logging.ERROR
#LOG_LEVEL_GLOBAL = logging.CRITICAL

LOG_LEVEL_FILE = logging.DEBUG
#LOG_LEVEL_FILE = logging.INFO
#LOG_LEVEL_FILE = logging.WARNING
#LOG_LEVEL_FILE = logging.ERROR
#LOG_LEVEL_FILE = logging.CRITICAL

#LOG_LEVEL_CONSOLE = logging.DEBUG
#LOG_LEVEL_CONSOLE = logging.INFO
LOG_LEVEL_CONSOLE = logging.WARNING
#LOG_LEVEL_CONSOLE = logging.ERROR
#LOG_LEVEL_CONSOLE = logging.CRITICAL

LOG_OUTPUT_FILE = 'app.log'

#LOG_FORMAT_FILE = '%(asctime)s - %(levelname)s - %(message)s - [%(filename)s - %(funcName)s]' 
# The prefix "<<mpls>>" is a custom string that can be used to identify the beginning 
# of a log messages of this application. This helps the bulk analysis of log files
# preventing the confusion with date and time information
# It stands for "My Python Logging System"
LOG_FORMAT_FILE = '<<mpls>> %(asctime)s - %(name)s - %(levelname)s - %(message)s'.encode('utf-8').decode('utf-8')
LOG_FORMAT_CONSOLE = '<<mpls>> %(levelname)s - %(message)s'.encode('utf-8').decode('utf-8')

# ULTRA_DEBUG mode
# This mode will reinforce the debug messages with a different format
# to add more information to the log in case of extreme debugging
# This mode is useful when you need to debug a specific part of the code
# and you need more information than the usual debug mode
# To enable this mode, just change the following lines

# Change to True to enable the ultra debug mode
FILE_ULTRA_DEBUG = True
CONSOLE_ULTRA_DEBUG = True

# Configure the format of the ultra debug mode
LOG_FORMAT_FILE_ULTRA_DEBUG = LOG_FORMAT_FILE + ' - [%(filename)s - %(funcName)s - %(lineno)d]'
LOG_FORMAT_CONSOLE_ULTRA_DEBUG = LOG_FORMAT_CONSOLE + ' - [%(filename)s - %(funcName)s - %(lineno)d]'
# ----------------- END OF LOG CONFIGURATION -----------------


LOGGER = logging.getLogger(__name__)

def ini_logging():
    
    # GLOBAL LOGGING CONFIGURATION
    LOGGER.setLevel(LOG_LEVEL_GLOBAL) 
    
    # FILE HANDLER LOGGING CONFIGURATION
    file_handler = logging.FileHandler(LOG_OUTPUT_FILE)
    file_handler.setLevel(LOG_LEVEL_FILE)
    file_handler_formatter = logging.Formatter(LOG_FORMAT_FILE)  
    
    if FILE_ULTRA_DEBUG:
        class CustomDebugFormatteFile(logging.Formatter):
            def format(self, record):
                if record.levelno == logging.DEBUG:
                    self._style._fmt = LOG_FORMAT_FILE_ULTRA_DEBUG  # Formato de debug
                else:
                    self._style._fmt = LOG_FORMAT_FILE  # Formato normal
                return super().format(record)        
        file_handler.setFormatter(CustomDebugFormatteFile())
    else:
        file_handler.setFormatter(console_handler_formatter)
        
        
    LOGGER.addHandler(file_handler)
    
    
    # CONSOLE HANDLER LOGGING CONFIGURATION
    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOG_LEVEL_CONSOLE)
    console_handler_formatter = logging.Formatter(LOG_FORMAT_CONSOLE)    
    
    
    if CONSOLE_ULTRA_DEBUG:
        class CustomDebugFormatter(logging.Formatter):
            def format(self, record):
                if record.levelno == logging.DEBUG:
                    self._style._fmt = LOG_FORMAT_CONSOLE_ULTRA_DEBUG  # Formato de debug
                else:
                    self._style._fmt = LOG_FORMAT_CONSOLE  # Formato normal
                return super().format(record)        
        console_handler.setFormatter(CustomDebugFormatter())
    else:
        console_handler.setFormatter(console_handler_formatter)
        
    
    LOGGER.addHandler(console_handler)
    
    LOGGER.debug('1 - Debug message')
    #LOGGER.info('1 - Info message')
    #LOGGER.warning('1 - Warning message')
    #LOGGER.error('1 - Error message')
    #LOGGER.critical('1 - Critical message')
    

    ## Criar um manipulador específico para logs de debug
    #debug_handler = logging.StreamHandler()
    #debug_formatter = logging.Formatter(LOG_FORMAT_DEBUG)
    #debug_handler.setFormatter(debug_formatter)  # Aplicar formato de debug
    #debug_handler.setLevel(logging.DEBUG)
    #LOGGER.addHandler(debug_handler)
    #
    #LOGGER.debug('2 - Debug message')
    #LOGGER.info('2 - Info message')
    #LOGGER.warning('2 - Warning message')
    #LOGGER.error('2 - Error message')
    #LOGGER.critical('2 - Critical message')
        
    return LOGGER


