import networking
from bs4 import BeautifulSoup as bs

def check(user, password):
    session = networking.create_session()

    site = session.get('https://accounts.google.com')
    soup = bs(site.content, 'html.parser')

    payload = {}
    for entry in soup.find_all('input'):
        if entry.get('name'):
            payload[entry.get('name')] = entry.get('value')
    payload['Email'] = user

    site = session.post('https://accounts.google.com/signin/v1/lookup', data=payload)

    payload = {}
    for entry in soup.find_all('input'):
        if entry.get('name'):
            payload[entry.get('name')] = entry.get('value')
    payload['Email'] = user
    payload['Passwd'] = password

    site = session.post('https://accounts.google.com/signin/challenge/sl/password', data=payload)

    return ('Wrong password' not in site.text) and ('2-Step Verification' not in site.text)
