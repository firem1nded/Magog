import requests

def create_session():
    session = requests.session()
    session.headers.update({'User-Agent': 'Windows / IE 11: Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'})
    return session

def get(session, url):
    return session.get(url)
