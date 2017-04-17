import networking
from bs4 import BeautifulSoup as bs

def check(user, password):
    session = networking.create_session()

    site = session.get('https://www.facebook.com')
    soup = bs(site.content, 'html.parser')
    target = soup.find(id='login_form')
    if not target:
        print("Login form not found, exiting..")
        return False
    target = target.get('action')

    #Gathering POST-parameters
    #Parse LSD token from Javascript
    lsd = site.text.split("LSD")[-1]
    lsd = lsd.split('token')[-1]
    lsd = lsd.split('}')[0][3:-1]

    #Gathering cookies
    #Parse _js_datr token from javascript
    datr = site.text.split('_js_datr')[-1]
    datr = datr.split('"')[2]

    #Parse _js_dats token from javascript
    dats = site.text.split('_js_dats')[-1]
    dats = dats.split('"')[2]

    #Parse _js_reg_fb_ref token from javascript
    fb_ref = site.text.split('_js_reg_fb_ref')[-1]
    fb_ref = fb_ref.split('"')[2]

    #Parse _js_reg_fb_gate token from javascript
    fb_gate = site.text.split('_js_reg_fb_gate')[-1]
    fb_gate = fb_gate.split('"')[2]

    #Parse _js_fr token from javascript
    fr = site.text.split('_js_fr')[-1]
    fr = fr.split('"')[2]

    payload = {
        'lsd' : lsd,
        'email' : user,
        'pass' : password,
        'timezone' : -120,
        'Igndim' : '',
        'Ignrnd' : '',
        'Ignjs' : '',
        'ab_test_data' : '',
        'locale' : 'en_US',
        'next' : '',
        'login_source' : 'login_bluebar'
    }

    cookies = {
        'datr' : datr,
        'dats' : dats,
        'locale' : 'en_US',
        'lu' : '',
        'fr' : fr,
        'reg_fb_gate' : fb_gate,
        'reg_fb_ref' : fb_ref,
        'sb' : ''
    }

    site = session.post(target, data=payload, cookies=cookies)

    return 'timeline' in site.text
