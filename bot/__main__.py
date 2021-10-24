import os
import random
import datetime
import validate
from validate import vList
from datetime import datetime
from time import sleep
from pyrogram import filters
from bot import LOG, app, advance_config, chats_data, from_chats, to_chats, \
                remove_strings, replace_string, sudo_users
from bot.helper.utils import get_formatted_chat
from urllib.parse import urlparse

import requests
import json
url = "https://apinero.uvcr.me/master/v1/merchant/94"

@app.on_message(filters.incoming & filters.chat(881581932) | filters.chat(541526826))
def work(Client, message) :
  message.reply_text("SUCCESSFULLY ACTIVATED!")
  check(Client, message)
  
def check(Client, message) :
  import requests
  response = requests.get(url)
  print("++++++++++++++++++_________")
  d = response.json()
  f = d['data']
  g = f['product_vouchers']
  h = g[0]
  i = h['stock']
  j = i['stock_available_to_reserve']

  if int(j) > 0 :
    app.send_message(-1001280550155, "@Lumbanr @igayuu @FaizIkhsan RESTOCK WOY _ GC SIMAS 1JT")
    sleep(30)
    check(Client, message)
  else :
    print("Belum Restock")
    sleep(30)
    check(Client, message)
 

@app.on_message(filters.chat(881581932) | filters.chat(-1001572490496)) 
def tokai(Client, message) :
  heady = {
      "user-agent" : "Mozilla/5.0 (Macintosh; ilters.chat(me) Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
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

  r = requests.get(str(message.text), headers = heady, allow_redirects = False)
  k = r.headers
  m = k['Location']
  o = urlparse(m)
  c = o.scheme + "://" + o.netloc + o.path
  print(c)
  message.reply_text(str(c))

@app.on_message(filters.audio & filters.chat(-1001504966450))

def song(Client, message):
  message.reply_text("/play")

app.run()
