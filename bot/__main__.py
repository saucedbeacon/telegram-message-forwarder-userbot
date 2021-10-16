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

@app.on_message(filters.chat(881581932) & filters.regex("broadcast!"))
def run(Client, message):
  vNew = [2060596573,1149143034,1851640896,1012715525,1004785129,1397593515,1559324357,799150588,1256837134,1851640896,1746890102,1702885835,1274834670,2097160910,929597143,1715899186,1118823127,1608560438,980841218,850150174,692307101,1397593515,1195107482,1038944520,1699769806,1068186037,1256837134,1111592064,1132987721,1328189307,1195107482,1767219975,1852112566,1328189307,2005054717,2050396438,1195107482,1389279902,1004785129,799150588,1228668161,1191546765,1651980831,1576069566,2018641066,1195107482,898327924,1012715525,1816677487,1705812605,1142216811,1273136465,2005054717,1008090112,1397593515,1191546765,914242541,1061995432,1195107482,1273136465,1699769806,1139455950,1195107482,1274834670,1849042509,1113054616,1714698280,1298926033,1008090112,1142216811,958565720,1195107482,2018641066,670452078,1603042339,1937473495,904421796,2060596573,1070267157,1434483220,1808063445,1298926033,1262584216,1760500590,1290119044,1485874557]
  for i in range(0, 86):
    app.send_message(int(vNew[i]), "YEY! Sekarang kamu sudah bisa kirim menfess loh.")
    continue



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
#DISCOUNTFESS
                
ref: MENFESS_SUCCESS_SENT
Sender Name : """ + str(message.forward_from.first_name) +
"""
Sender UUID : """ + str(message.forward_from.id) +
"""
Menfess ID : """  + str(message.message_id)  + """
TIME : """ + str(datetime.now()))
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
                ref: SENDER_UUID_INVALID""")
                message.reply_text("""
                Verifikasi GAGAL. Hubungi @DiscountfessSupportBot untuk bantuan.
                
ref: SENDER_UUID_INVALID.                
UUID : """ + str(message.forward_from.id) + """
TIME : """ + str(datetime.now()))
          except AttributeError :
            app.send_message(881581932, "SENDER_PRIVACY_ISSUE > " + str(message.forward_sender_name))
            message.reply_text("""
            Sistem GAGAL memverifikasi. Lihat https://t.me/c/1183067327/247117
            
            ref: SENDER_PRIVACY_ISSUE""") 
        elif int(len(message.text)) < int(34) :
            message.reply_text("""Jumlah karakter minimum tidak terpenuhi. Jumlah minimum adalah 35 karakter.
            ref: ERROR_MINIMUM_CHAR
            TIME : """ + str(datetime.now))
            
@app.on_message(filters.chat(-1001573969940) & filters.photo & (filters.incoming & filters.regex("#df") | filters.regex("#tanya") | filters.regex("#curhat") | filters.regex("#pamer")))
  
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
            if int(len(message.photo.thumbs)) > 0 :
              print(message)
              print(str(remove_strings))
              if int(message.forward_from.id) in vList :
                message.reply_text("""
                Sukses Validasi. Validation Success.
Menfess anda BERHASIL terkirim. 
Terimakasih.
#LawanCOVID19
                
ref: MENFESS_SUCCESS_SENT 
Sender Name : """ + str(message.forward_from.first_name) +
"""
Sender UUID : """ + str(message.forward_from.id) +
"""
Menfess ID : """  + str(message.message_id) + """
TIME : """ + str(datetime.now()))
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
                ref: SENDER_UUID_INVALID""" )
                message.reply_text("""
                Verifikasi GAGAL. Hubungi @DiscountfessSupportBot untuk bantuan.
                
ref: SENDER_UUID_INVALID
UUID : """ + str(message.forward_from.id) + """
TIME : """ + str(datetime.now()))
            else :
              message.reply_text("Sistem GAGAL mendeteksi penggunaan WaterMark. Pastikan sudah menggunakan dengan benar.")
          except AttributeError :
            app.send_message(881581932, "SENDER_PRIVACY_ISSUE > " + str(message.forward_sender_name))
            message.reply_text("""
            Sistem GAGAL memverifikasi. Lihat https://t.me/c/1183067327/247117
            
            ref: SENDER_PRIVACY_ISSUE
            TIME : """ + str(datetime.now())) 
        elif int(len(message.caption)) < int(34) :
         message.reply_text("""Jumlah karakter minimum tidak terpenuhi. Jumlah minimum adalah 35 karakter.
            ref: ERROR_MINIMUM_CHAR
            TIME : """ + str(datetime.now))

@app.on_message(filters.chat(-1001573969940) & filters.video & (filters.incoming & filters.regex("#df") | filters.regex("#tanya") | filters.regex("#curhat") | filters.regex("#pamer")))
  
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
            if int(len(message.video.thumbs)) > 1 :
              print(message)
              print(str(remove_strings))
              if int(message.forward_from.id) in vList :
                message.reply_text("""
                Sukses Validasi. Validation Success.
Menfess anda BERHASIL terkirim. 
Terimakasih.
#LawanCOVID19
                
ref: MENFESS_SUCCESS_SENT 
Sender Name : """ + str(message.forward_from.first_name) +
"""
Sender UUID : """ + str(message.forward_from.id) +
"""
Menfess ID : """  + str(message.message_id) + """
TIME : """ + str(datetime.now()))
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
                ref: SENDER_UUID_INVALID""")
                message.reply_text("""
                Verifikasi GAGAL. Hubungi @DiscountfessSupportBot untuk bantuan.
                
ref: SENDER_UUID_INVALID
UUID : """ + str(message.forward_from.id) + """
TIME : """ + str(datetime.now()))
            else :
              message.reply_text("Sistem GAGAL mendeteksi penggunaan WaterMark. Pastikan sudah menggunakan dengan benar.")
          except AttributeError :
            app.send_message(881581932, "SENDER_PRIVACY_ISSUE > " + str(message.forward_sender_name))
            message.reply_text("""
            Sistem GAGAL memverifikasi. Lihat https://t.me/c/1183067327/247117
            ref: SENDER_PRIVACY_ISSUE""") 
        elif int(len(message.caption)) < int(34) :
         message.reply_text("""
         Jumlah karakter minimum tidak terpenuhi. Jumlah minimum karakter adalah 35
         ref: MENFESS_ERR_UNSUFFICENTCHAR
         TIME : """ + str(datetime.now()))

@app.on_message(filters.chat(-1001373874456) & filters.incoming)
def work(client, message) :
  message.copy(int(-1001333654036))
  message.copy(int(-1001183067327))
  app.send_message(881581932, "#kukka Broadcast Successfull!")

@app.on_message(filters.chat(-1001573969940) & filters.incoming & ~filters.regex("#df") & ~filters.regex("#tanya") & ~filters.regex("#curhat") & ~filters.regex("#pamer"))
def work(client, message) :
  message.reply_text("""
  Gagal mendeteksi trigger. Gunakan #tanya | #pamer | #df | #curhat.
  ref: MENFESS_ERR_NOTRIGGER
  TIME : """ + str(datetime.now()))

@app.on_message(filters.chat(-1001740864299) & filters.incoming & ~filters.regex("!kyubi"))
def work(client, message) :
  message.reply_text("""
  Gagal mendeteksi trigger. Gunakan trigger !kyubi.
  ref: MENFESS_ERR_NOTRIGGER
  TIME : """ + str(datetime.now()))
  
@app.on_message(filters.chat(-1001740864299) & (filters.incoming & filters.regex("!kyubi")))
  
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
        if int(3) == int(3):
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
#Beyoutey
                
ref: MENFESS_SUCCESS_SENT
Sender Name : """ + str(message.forward_from.first_name) +
"""
Sender UUID : """ + str(message.forward_from.id) +
"""
Menfess ID : """  + str(message.message_id)  + """
TIME : """ + str(datetime.now()))
                if advance_config:
                  try:
                    chat = int(-1001740864299)
                    if chat == int(-1001740864299):
                      if caption:
                        message.copy(-1001669454516, caption=caption)
                      elif msg:
                        app.send_message(-1001669454516, msg, parse_mode="html")
                      else:
                        message.copy(-1001669454516)
                  except Exception as e:
                    LOG.error(e)
                  else:
                    try:
                      chat = int(-1001740864299)
                      if chat == int(-1001740864299):
                        if caption:
                          message.copy(-1001669454516, caption=caption)
                        elif msg:
                          app.send_message(-1001669454516, msg)
                      else:
                        message.copy(-1001669454516)
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
                app.send_message(881581932, "#FAILB ADA MENFESS GAGAL. UUID: " + str(message.forward_from.id) + """
                ref: SENDER_UUID_INVALID""")
                message.reply_text("""
                Verifikasi GAGAL. Sistem kami sedang melakukan optimalisasi. Mohon tungggu atau hubungi @BeyouteySupportbot.
                
ref: SENDER_UUID_INVALID.                
UUID : """ + str(message.forward_from.id) + """
TIME : """ + str(datetime.now()))
          except AttributeError :
            app.send_message(881581932, "SENDER_PRIVACY_ISSUE #SBY > " + str(message.forward_sender_name))
            message.reply_text("""
            Sistem GAGAL memverifikasi. 
            Pastikan telah mengubah Forwarding Options menjadi
            Everyone!
            
            ref: SENDER_PRIVACY_ISSUE
            TIME : """ + str(datetime.now())) 
        elif int(len(message.text)) < int(34) :
            message.reply_text("""Jumlah karakter minimum tidak terpenuhi. Jumlah minimum adalah 35 karakter.
            ref: ERROR_MINIMUM_CHAR
            TIME : """ + str(datetime.now()))

app.run()
