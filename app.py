#imports
from pickle import TRUE
import sys
from dotenv import load_dotenv
from fastapi import FastAPI
import logging
import sys
import os

#DEBUG
DEBUG = TRUE

#logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    #datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

if DEBUG:
    load_dotenv(verbose=True)
    logger.info("Debug mode enabled loading .env file")

#network constants
try:
    HOST = os.environ["HOST"]
    PORT = os.environ['PORT']
    WEB1 = os.environ['WEB1']
    WEB2 = os.environ['WEB2']
    RU1 = os.environ['RU1']
    RU2 = os.environ['RU2']
    ROUTER = os.environ['Router']



    logger.info("Network constants loaded")
except Exception as e:
    logger.critical("Failed to load network constants")
    sys.exit(1)


INTERNET_LIST = [WEB1, WEB2]
RU_LIST = [RU1, RU2]


logger.info("Starting server")
app = FastAPI()

#health
@app.get("/health")
async def health_check():
    logger.info("called health endpoint")
    return {"health": "ok"}

@app.get("/status")
def get_status():
    pass
