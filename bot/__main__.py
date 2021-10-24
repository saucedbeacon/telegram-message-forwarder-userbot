import os
import random
import datetime
import validate
from validate import vList
import waiting
from waiting import waitingUsr
from datetime import datetime
from time import sleep
from pyrogram import filters
from bot import LOG, app, advance_config, chats_data, from_chats, to_chats, \
                remove_strings, replace_string, sudo_users
from bot.helper.utils import get_formatted_chat


import os
import random
import datetime
import validate
from validate import vList
import waiting
from waiting import waitingUsr
from datetime import datetime
from time import sleep
from pyrogram import filters
from bot import LOG, app, advance_config, chats_data, from_chats, to_chats, \
                remove_strings, replace_string, sudo_users
from bot.helper.utils import get_formatted_chat

############################################################################################################
##################################### START MENFESS DISCOUNTFESS ###########################################
############################################################################################################

@app.on_message(filters.chat(-1001573969940) & (filters.incoming & filters.regex("#df") | filters.regex("#tanya") | filters.regex("#curhat") | filters.regex("#pamer")))


def mOne(client, message):
  caption = None
  msg = None
  if message.caption:
    if len(message.caption) > int(34):
      print("PassmOne")
      mTwo(client, message)
    else :
      print("PasseOne")
      exOne(client, message)
  elif message.text:
    if len(message.text) > int(34):
      print("PassmOne")
      mTwo(client, message)
    else :
      print("PasseOne")
      exOne(client, message)
  
    
def exOne(client, message) :
  print("PassaeOne")
  message.reply_text("""
         Jumlah karakter minimum tidak terpenuhi. Jumlah minimum karakter adalah 35
         ref: MENFESS_ERR_UNSUFFICENTCHAR
         TIME : """ + str(datetime.now()))
  
def mTwo(client, message):
  try:
    if int(message.forward_from.id) in vList :
      print("Pass mTwo")
      mThree(client, message)
    else :
      print("Sender Invalid")
      exTwo(client, message)
  except AttributeError :
      print("Sender Privacy")
      atTwo(client, message)

def exTwo(client, message) :
  app.send_message(881581932, "Nama Pengirim > " + str(message.forward_from.first_name))
  app.send_message(881581932, "#FAIL ADA MENFESS GAGAL. UUID: " + str(message.forward_from.id) + """
                ref: SENDER_UUID_INVALID""")
  message.reply_text("""
                Verifikasi GAGAL. Hubungi @DiscountfessSupportBot untuk bantuan.
                
ref: SENDER_UUID_INVALID
UUID : """ + str(message.forward_from.id) + """
TIME : """ + str(datetime.now()))

def atTwo(client, message) :
  app.send_message(881581932, "SENDER_PRIVACY_ISSUE > " + str(message.forward_sender_name))
  message.reply_text("""
            Sistem GAGAL memverifikasi. Lihat https://t.me/c/1183067327/247117
            ref: SENDER_PRIVACY_ISSUE""") 
  
def preFr(Client, message):
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
  exFr(Client, message)

def exFr(Client, message):
  if message.caption:
    message.copy(-1001183067327)
  elif message.text:
    app.send_message(-1001183067327, message.text)

def exThree(client, message):
  waitingUsr.append(message.forward_from.id)
  print(waitingUsr)
  sleep(180)
  waitingUsr.remove(message.forward_from.id)

def delay(client, message):
  message.reply_text("Menfess anda sedang dalam antrian dan menunggu verifikasi.")
  message.copy(-1001565220245)
  sleep(600)
  preFr(client, message)
  
def mThree(client, message):
  if int(message.forward_from.id) in waitingUsr :
    message.reply_text("Mohon menunggu 3 menit untuk mengirimkan menfess kembali.")
  else :
    delay(client, message)

@app.on_message(filters.chat(-1001573969940) & filters.incoming & ~filters.regex("#df") & ~filters.regex("#tanya") & ~filters.regex("#curhat") & ~filters.regex("#pamer"))

def work(client, message) :
  message.reply_text("""
  Gagal mendeteksi trigger. Gunakan #tanya | #pamer | #df | #curhat.
  ref: MENFESS_ERR_NOTRIGGER
  TIME : """ + str(datetime.now()))


############################################################################################################
##################################### END MENFESS DISCOUNTFESS #############################################
############################################################################################################

############################################################################################################
####################################### START KUKKA BROADCAST ##############################################
############################################################################################################

@app.on_message(filters.chat(-1001373874456) & filters.incoming)

def work(client, message) :
  message.copy(int(-1001333654036))
  message.copy(int(-1001183067327))
  app.send_message(881581932, "#kukka Broadcast Successfull!")

############################################################################################################
####################################### END KUKKA BROADCAST ################################################
############################################################################################################

############################################################################################################
####################################### START KYUBI MENFESS ################################################
############################################################################################################

@app.on_message(filters.chat(-1001740864299) & (filters.incoming & filters.regex("!kyubi")))

def mOnek(client, message):
  caption = None
  msg = None
  if message.caption:
    if len(message.caption) > int(34):
      print("PassmOne")
      mTwok(client, message)
    else :
      print("PasseOne")
      exOnek(client, message)
  elif message.text:
    if len(message.text) > int(34):
      print("PassmOne")
      mTwok(client, message)
    else :
      print("PasseOne")
      exOnek(client, message)
  
    
def exOnek(client, message) :
  print("PassaeOne")
  message.reply_text("""
         Jumlah karakter minimum tidak terpenuhi. Jumlah minimum karakter adalah 35
         ref: MENFESS_ERR_UNSUFFICENTCHAR
         TIME : """ + str(datetime.now()))
  
def mTwok(client, message):
  try:
    if int(message.forward_from.id) in vList :
      print("Pass mTwo")
      mThreek(client, message)
    else :
      print("Sender Invalid")
      exTwok(client, message)
  except AttributeError :
      print("Sender Privacy")
      atTwok(client, message)

def exTwok(client, message) :
  app.send_message(881581932, "Nama Pengirim > " + str(message.forward_from.first_name))
  app.send_message(881581932, "#FAIL ADA MENFESS GAGAL. UUID: " + str(message.forward_from.id) + """
                ref: SENDER_UUID_INVALID""")
  message.reply_text("""
                Verifikasi GAGAL. Hubungi @BeyouteySupportBot untuk bantuan.
                
ref: SENDER_UUID_INVALID
UUID : """ + str(message.forward_from.id) + """
TIME : """ + str(datetime.now()))

def atTwok(client, message) :
  app.send_message(881581932, "SENDER_PRIVACY_ISSUE > " + str(message.forward_sender_name))
  message.reply_text("""
            Sistem GAGAL memverifikasi. Aktifkan pengaturan forwarding anda ke semua orang.
            ref: SENDER_PRIVACY_ISSUE""") 
  
def preFrk(Client, message):
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
Menfess ID : """  + str(message.message_id) + """
TIME : """ + str(datetime.now()))
  exFrk(Client, message)

def exFrk(Client, message):
  if message.caption:
    message.copy(-1001669454516)
  elif message.text:
    app.send_message(-1001669454516, message.text)

def exThreek(client, message):
  waitingUsr.append(message.forward_from.id)
  print(waitingUsr)
  sleep(180)
  waitingUsr.remove(message.forward_from.id)

def delayk(client, message):
  message.reply_text("Menfess anda sedang dalam antrian dan menunggu verifikasi.")
  app.send_message(-1001565220245, message.text)
  sleep(5)
  preFr(client, message)
  
def mThreek(client, message):
  if int(message.forward_from.id) in waitingUsr :
    message.reply_text("Mohon menunggu 3 menit untuk mengirimkan menfess kembali.")
  else :
    delay(client, message)

@app.on_message(filters.chat(-1001740864299) & filters.incoming & ~filters.regex("!kyubi"))

def workka(client, message) :
  message.reply_text("""
  Gagal mendeteksi trigger. Gunakan trigger !kyubi.
  ref: MENFESS_ERR_NOTRIGGER
  TIME : """ + str(datetime.now()))
  
############################################################################################################
######################################## END KYUBI MENFESS #################################################
############################################################################################################

app.run()
