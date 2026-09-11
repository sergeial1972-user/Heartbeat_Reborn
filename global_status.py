#imports

from config import RU_LIST, INTERNET_LIST, ROUTER
import httpx

def check_url(url: str) -> bool:
    with httpx.Client() as client:
        resp = client.get(url, follow_redirects=True, timeout=4.0)

        if not resp.is_success:
            return False
    return True



def check_internet() -> bool:
    for url in INTERNET_LIST:
        if check_url(url):
            return True
            break
    return False

def check_runet() -> bool:
    for url in RU_LIST:
        if check_url(url):
            return True
            break
    return False

def check_local() -> bool:
    if check_url(ROUTER):
        return True
    return False


def global_status():
    if check_internet():
        return 3;

    if check_runet():
        return 2;

    if check_local():
        return 1;

    return 0;
