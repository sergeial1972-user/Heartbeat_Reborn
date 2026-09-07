#imports
from starlette import responses

from app import RU_LIST, INTERNET_LIST, ROUTER
import bs4 as bs
import httpx

def check_url(url: str) -> bool:
    client = httpx.Client

    with httpx.Client() as client:
        resp = client.get(url, follow_redirects=True, timeout=4.0)

        if not resp.is_success:
            return False
