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
url = "https://apinero.uvcr.me/master/v1/merchant/94"

@app.on_message(filters.incoming & filters.chat(881581932) | filters.chat(541526826))

def check(Client, message) :
  
  import requests
  message.reply_text("SUCCESSFULLY ACTIVATED!")
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
  else :
    app.send_message(-1001280550155, "LAGI GAK ADA STOK")
    sleep(30)

app.run()
    


