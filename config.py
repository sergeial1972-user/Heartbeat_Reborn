#imports
import os
import logging
import sys
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

DEBUG = False

#load dotenv
if DEBUG:
    load_dotenv()
    logger.info("Debug mode enabled loading .env file")

#network constants
try:
    HOST = os.environ["HOST"]
    PORT = os.environ['PORT']
    WEB1 = os.environ['WEB1']
    WEB2 = os.environ['WEB2']
    RU1 = os.environ['RU1']
    RU2 = os.environ['RU2']
    ROUTER = os.environ['ROUTER']



    logger.info("Network constants loaded")
except Exception as e:
    logger.critical("Failed to load network constants")
    sys.exit(1)

INTERNET_LIST = [WEB1, WEB2]
RU_LIST = [RU1, RU2]
