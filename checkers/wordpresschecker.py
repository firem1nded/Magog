import networking
from bs4 import BeautifulSoup as bs

def check(user, password):
    session = networking.create_session()

    payload = {
        'log' : user,
        'pwd' : password,
        'rememberme': 'forever',
        'wp-submit': 'Log in',
        'redirect_to' : 'https://wordpress.com/',
        'testcookie' : 0,
    }
    site = session.post('https://wordpress.com/wp-login.php', data=payload,
        cookies={'wordpress_test_cookie': 'WP Cookie check'})

    soup = bs(site.content, 'html.parser')
    if bs(site.content, 'html.parser').noscript:
        return True
    else:
        return False
