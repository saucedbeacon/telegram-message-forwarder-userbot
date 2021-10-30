def apihandler():
  from flask import Flask
  from flask import request
  app = Flask(__name__)
  import os
  import urllib
  import requests
  import urllib 
  from urllib.parse import urlparse
  import re
  import requests


  @app.route('/')
  def index():
    return "OmegaApi Project"
    
  @app.route('/greet')
  def say_hello():
    return 'Hello from Server'

  @app.route('/https://tokopedia.link/<link>')
  def tokopedia(link) :
    heady = {
        "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "en-US,en;q=0.9",
        "sec-ch-ua": "\"Chromium\";v=\"94\", \"Google Chrome\";v=\"94\", \";Not A Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"
      }
    curl = 'https://tokopedia.link/' + str(link)

    r = requests.get(str(curl), headers = heady, allow_redirects = False)
    k = r.headers
    m = k['Location']
    d = requests.get(str(m), headers = heady, allow_redirects = False)
    ka = d.headers
    ma = ka['Location']
    oa = urlparse(ma)
    ca = oa.scheme + "://" + oa.netloc + oa.path
    print(ca)
    return f"""<a href="{ca}">{ca}</a>""" + """
    """ + """<a href="whatsapp://send?text={}" data-action="share/whatsapp/share">Share via Whatsapp</a>""".format(ca)

  def check_in():

      fqn = os.uname()[1]
      ext_ip = urllib.urlopen('http://whatismyip.org').read()
      print ("Asset: %s " % fqn, "Checking in from IP#: %s " % ext_ip)
  
  app.run(debug=True, host='0.0.0.0')
      
apihandler()
