from socket import gethostbyaddr, herror

from requests import ConnectionError, get


def hostname(IP):
    try:
        return gethostbyaddr(IP)[0]
    
    except herror:
        return None
    

def ip():
    try:
        return get(
            'https://ipapi.co/ip'
        ).text
    
    except ConnectionError:
        return None
