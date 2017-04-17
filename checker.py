from checkers import wordpresschecker
from checkers import facebookchecker
from checkers import googlechecker

def check(user, password):
    sites = {}

    sites['wordpress.com'] = wordpresschecker.check(user, password)
    sites['facebook.com'] = facebookchecker.check(user, password)
    sites['google.com'] = googlechecker.check(user, password)

    return sites
