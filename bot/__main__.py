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

import requests
import json
url = "https://apinero.uvcr.me/master/v1/merchant/148"
@app.on_message
def check(Client) :
  import requests
  response = requests.get(url)
  d = response.json()
  f = d['data']
  g = f['product_vouchers']
  h = g[0]
  i = h['stock']
  j = i['stock_available_to_reserve']

  if int(j) > 0 :
    app.send_message("Omega_Telegram", "RESTOCK WOY")
    check()
  else :
    app.send_message("Omega_Telegram", "LAGI GAK ADA STOK")
   
  

app.run()
check()

