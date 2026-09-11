#imports
import sys
from dotenv import load_dotenv
from fastapi import FastAPI
import logging
import sys
import os
from global_status import global_status
from config import HOST, PORT

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

logger.info("Starting server")
app = FastAPI()

#health
@app.get("/health")
async def health_check():
    logger.info("called health endpoint")
    return {"health": "ok"}

@app.get("/status")
def get_status():
    status = global_status();
    return {"status":status}

if __name__ == "__main__":
    import uvicorn

    logger.info(f"server started on {HOST}:{PORT}")

    uvicorn.run(
        "app:app",
        host=HOST,
        port=int(PORT),
        reload=True,
    )
