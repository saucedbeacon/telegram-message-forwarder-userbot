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
from urllib.parse import parse_qs
import re
import requests
import json

@app.on_message(filters.service)
def antiservice(Client, message):
  app.delete_messages(message.chat.id, message.message_id)

@app.on_message(filters.chat(-1001494559873))
def antiaf(Client, message):
  if message.caption:
    rawurl = message.caption
  else:
    rawurl = message.text
  urls = re.findall(r'(https?://[^\s]+)', rawurl)
  print(urls)
  curl = urls[0]
  if len(urls) > 1:
    ncurl = urls[1]
  else :
    ncurl = None
  parse = urlparse(curl)
  domain = parse.netloc
  try:
    if domain == "tokopedia.link":
      checktokopedia(Client, message, curl)
    elif domain == "shp.ee":
      kick(Client, message)
      app.send_message(-1001747493889, f"{message.from_user.id} {message.from_user.first_name}, kicked because of SHOPEE AFFILIATE")
    elif domain == "u.jd.id":
      kick(Client, message)
      app.send_message(-1001747493889, f"{message.from_user.id} {message.from_user.first_name}, kicked because of JDID AFFILIATE")
  except:
    if ncurl:
      curl = ncurl
      if domain == "tokopedia.link":
        checktokopedia(Client, message, curl)
      elif domain == "shp.ee":
        kick(Client, message)
        app.send_message(-1001747493889, f"{message.from_user.id} {message.from_user.first_name}, kicked because of SHOPEE AFFILIATE")


@app.on_message(filters.chat(-1001333654036))
def antiaf(Client, message):
  if message.caption:
    rawurl = message.caption
  else:
    rawurl = message.text
  urls = re.findall(r'(https?://[^\s]+)', rawurl)
  print(urls)
  curl = urls[0]
  if len(urls) > 1:
    ncurl = urls[1]
  else :
    ncurl = None
  parse = urlparse(curl)
  domain = parse.netloc
  try:
    if domain == "tokopedia.link":
      checktokopedia(Client, message, curl)
    elif domain == "shp.ee":
      kick(Client, message)
      app.send_message(-1001747493889, f"{message.from_user.id} {message.from_user.first_name}, kicked because of SHOPEE AFFILIATE")
    elif domain == "u.jd.id":
      kick(Client, message)
      app.send_message(-1001747493889, f"{message.from_user.id} {message.from_user.first_name}, kicked because of JDID AFFILIATE")
  except:
    if ncurl:
      curl = ncurl
      if domain == "tokopedia.link":
        checktokopedia(Client, message, curl)
      elif domain == "shp.ee":
        kick(Client, message)
        app.send_message(-1001747493889, f"{message.from_user.id} {message.from_user.first_name}, kicked because of SHOPEE AFFILIATE")

def checktokopedia(Client, message, curl):
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
  r = requests.get(str(curl), headers = heady, allow_redirects = False)
  k = r.headers
  print(k)
  m = k['Location']
  d = requests.get(str(m), headers = heady, allow_redirects = False)
  ka = d.headers
  ma = ka['Location']
  oa = urlparse(ma)
  print(oa)
  incheck = parse_qs(oa[4])
  
  try:
    abn = incheck['aff_unique_id']
    kick(Client, message)
    app.send_message(-1001747493889, f"{message.from_user.id} {message.from_user.first_name}, kicked because of TOKOPEDIA AFFILIATE")
    print("KICK")
  except :
    print("SAFELINK")
  
def kick(Client, message):
  user_id = message.from_user.id
  cidbs = int(-1001494559873)
  ciddf = int(-1001333654036)
  ciddfch = int(-1001183067327)
  try:
    app.kick_chat_member(cidbs, user_id)
  except:
    print("KICK FAILED BECAUSE MEMBER DIDN/'T JOIN")
  try:
    app.kick_chat_member(ciddf, user_id)
  except:
    print("KICK FAILED BECAUSE MEMBER DIDN/'T JOIN")
  try:
    app.kick_chat_member(ciddfch, user_id)
  except:
    print("KICK FAILED BECAUSE MEMBER DIDN/'T JOIN")
  app.delete_messages(message.chat.id, message.message_id)
  print("KICKED")

app.run()
