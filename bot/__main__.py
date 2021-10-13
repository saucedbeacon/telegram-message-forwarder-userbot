import os
import random
import validate
from validate import vList
from time import sleep
from pyrogram import filters
from bot import LOG, app, advance_config, chats_data, from_chats, to_chats, \
                remove_strings, replace_string, sudo_users
from bot.helper.utils import get_formatted_chat

@app.on_message(filters.chat(-1001573969940) & filters.text & (filters.incoming & filters.regex("#df") | filters.regex("#tanya") | filters.regex("#curhat") | filters.regex("#pamer")))
  
def validator(client, message) :
    caption = None
    msg = None
    if remove_strings:
      if str(remove_strings) in str(message.caption):
        if message.media and not message.poll:
          message.reply_text("Failed")
        elif message.text:
          message.reply_text("Failed")
      else:
        if len(message.text) > int(34):
          try:
            hasBlacklisted = False
            if hasBlacklisted == False :
              print(message)
              print(str(remove_strings))
              if int(message.forward_from.id) in vList :
                message.reply_text("""
                Sukses Validasi. Validation Success.
                Menfess anda BERHASIL terkirim. 
                Terimakasih.
                #LawanCOVID19
                
                ref: MENFESS_SUCCESS_SENT""")
                if advance_config:
                  try:
                    for chat in chats_data[message.chat.id]:
                      if caption:
                        message.copy(chat, caption=caption)
                      elif msg:
                        app.send_message(chat, msg, parse_mode="html")
                      else:
                        message.copy(chat)
                  except Exception as e:
                    LOG.error(e)
                  else:
                    try:
                      for chat in to_chats:
                        if caption:
                          message.copy(chat, caption=caption)
                        elif msg:
                          app.send_message(chat, msg)
                      else:
                        message.copy(chat)
                    except Exception as e:
                      LOG.error(e)
                elif str(message.chat.id) == str(-1001373874456) : 
                  print("Has Hitted")
                  message.reply_text("FAILED > GAGAL")
              elif str(message.chat.id) == str(-1001373874456) :
                message.copy(int(1333654036))
                message.copy(int(1183067327))
                app.send_message(881581932, "#kukka Broadcast Successfull!")
              else: 
                app.send_message(881581932, "Nama Pengirim > " + str(message.forward_from.first_name))
                app.send_message(881581932, "#FAIL ADA MENFESS GAGAL. UUID: " + str(message.forward_from.id) + """
                ref: MENFESS_UUID_INVALID""")
                message.reply_text("""
                Verifikasi GAGAL. Hubungi @DiscountfessSupportBot untuk bantuan.
                
                ref: MENFESS_UUID_INVALID""" + str(message.forward_from.id))
          except AttributeError :
            app.send_message(881581932, "SENDER_PRIVACY_ISSUE > " + str(message.forward_sender_name))
            message.reply_text("""
            Sistem GAGAL memverifikasi. Lihat https://t.me/c/1183067327/247117
            
            ref: SENDER_PRIVACY_ISSUE""") 
        elif int(len(message.text)) < int(34) :
            message.reply_text("Jumlah karakter minimum tidak terpenuhi. Jumlah minimum adalah 35 karakter.")
            app.send_message(881581932, "ERROR_MINIMUM_CHAR")

@app.on_message(filters.chat(-1001573969940) & filters.caption & (filters.incoming & filters.regex("#df") | filters.regex("#tanya") | filters.regex("#curhat") | filters.regex("#pamer")))
  
def validator(client, message) :
    caption = None
    msg = None
    if remove_strings:
      if str(remove_strings) in str(message.caption):
        if message.media and not message.poll:
          message.reply_text("Failed")
        elif message.text:
          message.reply_text("Failed")
      else:
        if len(message.caption) > int(34) :
          try:
            hasBlacklisted = False
            if hasBlacklisted == False :
              print(message)
              print(str(remove_strings))
              if int(message.forward_from.id) in vList :
                message.reply_text("""
                Sukses Validasi. Validation Success.
                Menfess anda BERHASIL terkirim. 
                Terimakasih.
                #LawanCOVID19
                
                ref: MENFESS_SUCCESS_SENT""")
                if advance_config:
                  try:
                    for chat in chats_data[message.chat.id]:
                      if caption:
                        message.copy(chat, caption=caption)
                      elif msg:
                        app.send_message(chat, msg, parse_mode="html")
                      else:
                        message.copy(chat)
                  except Exception as e:
                    LOG.error(e)
                  else:
                    try:
                      for chat in to_chats:
                        if caption:
                          message.copy(chat, caption=caption)
                        elif msg:
                          app.send_message(chat, msg)
                      else:
                        message.copy(chat)
                    except Exception as e:
                      LOG.error(e)
                elif str(message.chat.id) == str(-1001373874456) : 
                  print("Has Hitted")
                  message.reply_text("FAILED > GAGAL")
              elif str(message.chat.id) == str(-1001373874456) :
                message.copy(int(1333654036))
                message.copy(int(1183067327))
                app.send_message(881581932, "#kukka Broadcast Successfull!")
              else: 
                app.send_message(881581932, "Nama Pengirim > " + str(message.forward_from.first_name))
                app.send_message(881581932, "#FAIL ADA MENFESS GAGAL. UUID: " + str(message.forward_from.id) + """
                ref: MENFESS_UUID_INVALID""")
                message.reply_text("""
                Verifikasi GAGAL. Hubungi @DiscountfessSupportBot untuk bantuan.
                
                ref: MENFESS_UUID_INVALID
                
                UUID : """ + str(message.forward_from.id))
          except AttributeError :
            app.send_message(881581932, "SENDER_PRIVACY_ISSUE > " + str(message.forward_sender_name))
            message.reply_text("""
            Sistem GAGAL memverifikasi. Lihat https://t.me/c/1183067327/247117
            
            ref: SENDER_PRIVACY_ISSUE""") 
        elif int(len(message.caption)) < int(34) :
         message.reply_text("Jumlah karakter minimum tidak terpenuhi. Jumlah minimum karakter adalah 35")

@app.on_message(filters.chat(-1001373874456) & filters.incoming)
def work(client, message) :
  message.copy(int(-1001333654036))
  message.copy(int(-1001183067327))
  app.send_message(881581932, "#kukka Broadcast Successfull!")

@app.on_message(filters.user(sudo_users) & filters.command(["fwd", "forward"]), group=1)
def forward(app, message):
    if len(message.command) > 1:
      chat_id = get_formatted_chat(message.command[1], app)
      if chat_id:
        try:
          offset_id = 0
          limit = 0
          if len(message.command) > 2:
            limit = int(message.command[2])
          if len(message.command) > 3:
            offset_id = int(message.command[3])
          for msg in app.iter_history(chat_id, limit=limit, offset_id=offset_id):
            msg.copy(message.chat.id)
            sleep(random.randint(1, 10))
        except Exception as e:
          message.reply_text(f"```{e}```")
      else:
        reply = message.reply_text("```Invalid Chat Identifier. Give me a chat id, username or message link.```")
        sleep(5)
        reply.delete()
    else:
      reply = message.reply_text("```Invalid Command ! Use /fwd {ChatID} {limit} {FirstMessageID}```")
      sleep(20)
      reply.delete()

app.run()

