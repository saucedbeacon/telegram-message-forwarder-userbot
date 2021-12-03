import os
import random
import datetime
import pymssql
import validate
from validate import vList
import waiting
import requests
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

waitingUsr= []
import pymssql

conn = pymssql.connect(server='owsapidb.mssql.somee.com', user='ows-api_SQLLogin_1', password='t22thz9g6w')  
cursor = conn.cursor(as_dict=True)


############################################################################################################
##################################### START MENFESS DISCOUNTFESS ###########################################
############################################################################################################

LISTEN_CHAT = int(-1001573969940)
THROW_CHAT = int(-1001183067327)

@app.on_message(filters.chat(LISTEN_CHAT) & (filters.incoming & (filters.text | filters.photo | filters.video | filters.animation)) & (filters.regex("#df") | filters.regex("#tanya") | filters.regex("#curhat") | filters.regex("#pamer")))


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
    import requests
    uid = message.forward_from.id
    r = requests.get('https://ns7.kukka.link/xVabfaHdbw/df/api/check/{}'.format(uid))
    print(r.status_code)
    if str(r.status_code) == str(200) :
      print("Pass mTwo")
      mThree(client, message)
    else :
      print("Sender Invalid")
      exTwo(client, message)
  except AttributeError :
      print("Sender Privacy")
      atTwo(client, message)

def mThree(Client, message):
  if message.forward_from.id in waitingUsr :
    message.reply_text("[429] Too Frequent")
  else :
    antiLink(Client, message)
    exThree(Client, message)
    
    
def exTwo(Client, message) :
  app.get_chat("Omega_Telegram")
  app.send_message(881581932, "Nama Pengirim > " + str(message.forward_from.first_name))
  app.send_message(881581932, "#FAIL ADA MENFESS GAGAL. UUID: " + str(message.forward_from.id) + """
                ref: SENDER_UUID_INVALID""")
  message.reply_text("""
                Verifikasi GAGAL. Hubungi @DiscountfessSupportBot untuk bantuan.
                
ref: SENDER_UUID_INVALID
UUID : """ + str(message.forward_from.id) + """
TIME : """ + str(datetime.now()))

def atTwo(Client, message) :
  app.get_chat("Omega_Telegram")
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
  if message.photo or message.video or message.animation :
    message.reply_text("Foto yang anda kirimkan akan diproses secara otomatis. Terimakasih")
    exPhoto(Client, message)
    global sender
    sender = message.forward_from.id
  else :
    exFr(Client, message)

def exPhoto(Client, message) :
  app.get_chat("OAHVDONWBWatermarkHandlerbot")
  a = message.copy(2056449872)

def exFr(Client, message):
  if message.caption:
    orSender = message.forward_from.id
    a = message.copy(THROW_CHAT)
    msgID = a.message_id
    print(a)
    cursor.execute("INSERT INTO [dbo].[deleteDump] VALUES ({}, {});".format(orSender, msgID))
    conn.commit()
  elif message.text:
    orSender = message.forward_from.id
    a = app.send_message(THROW_CHAT, message.text)
    msgID = a.message_id
    print(a)
    cursor.execute("INSERT INTO [dbo].[deleteDump] VALUES ({}, {});".format(orSender, msgID))
    conn.commit()

def exThree(Client, message):
  waitingUsr.append(message.forward_from.id)
  print(waitingUsr)
  sleep(180)
  waitingUsr.remove(message.forward_from.id)

def delay(Client, message):
  message.reply_text("MENFESS AKAN MEMERLUKAN WAKTU PROSES LEBIH LAMA DARI BIASANYA. MOHON MENUNGGU DAN TIDAK MENGIRIMKAN DOUBLEFESS")
  message.copy(-1001565220245)
  print("Delay Module")
  sleep(1)
  preFr(Client, message)
    
def antiLink(Client, message):
  if message.caption:
    if len(message.caption_entities) > 1 :
      r = message.caption_entities[0]
      k = message.caption_entities[1]
      typeOne = r['type']
      typeTwo = k['type']
      if typeOne == "url" or typeTwo == "url" or typeOne == 'text_link' or typeTwo == 'text_link':
        message.reply_text("Dilarang mengirimkan tautan. Links are forbidden.")
      else :
        delay(Client, message)
    elif len(message.caption_entities) == 1:
      delay(Client, message)
  elif message.text:
    if len(message.entities) > 1 :
      r = message.entities[0]
      k = message.entities[1]
      typeOne = r['type']
      typeTwo = k['type']
      if typeOne == "url" or typeTwo == "url" or typeOne == 'text_link' or typeTwo == 'text_link':
        message.reply_text("Dilarang mengirimkan tautan. Links are forbidden.")
      else :
        delay(Client, message)
    elif len(message.entities) == 1:
      delay(Client, message)

@app.on_message(filters.chat(2056449872) & filters.incoming & (filters.photo | filters.video | filters.animation) & (filters.regex("#df") | filters.regex("#tanya") | filters.regex("#curhat") | filters.regex("#pamer")))

def frPhoto(Client, message):
  a = message.copy(THROW_CHAT)
  r = a.message_id
  print("PHOTO SEND")
  cursor.execute("INSERT INTO [dbo].[deleteDump] VALUES ({}, {});".format(sender, r))
  conn.commit()

@app.on_message(filters.chat(LISTEN_CHAT) & filters.regex("#delete"))
def verify(Client, message):
  cursor.execute("SELECT * FROM [dbo].[phVerify] WHERE userID = {}".format(message.forward_from.id))
  row = cursor.fetchone()
  if row == None:
    message.reply_text("""
    ANDA BELUM MELAKUKAN VERIFIKASI. SILAKAN MELAKUKAN VERIFIKASI TERLEBIH DAHULU.""")
  else:
    pNum = row['phoneNum']
    delete(Client, message, pNum)

def delete(Client, message, pNum):
  print(message)
  x = message.forward_from.id
  try:
    cursor.execute("SELECT * FROM [dbo].[deleteDump] WHERE senderId = {}".format(x))
    row = cursor.fetchall()
    print(row)
    a = int(len(row))
    print(a)
    fessID = int(row[a-1]['fessMsgID'])
    app.delete_messages(THROW_CHAT, fessID)
    message.reply_text(
    f"""
    PENGHAPUSAN BERHASIL !
    Ingat! Jika menfess yang dihapus melanggar rules, maka akan tetap dikenakan sanksi.

    Menfess ID : {a}
    Menfess Sender : {x}
    Time : {datetime.now()}
    Sender Phone Number : {pNum}
    """)
  except:
    message.reply_text("Penghapusan GAGAL")

@app.on_message(filters.chat(LISTEN_CHAT) & filters.incoming & (~filters.regex("#df") | ~filters.regex("#tanya") | ~filters.regex("#curhat") | ~filters.regex("#pamer") | ~filters.regex("#delete")))

def work(Client, message) :
  if message.contact != None :
    pnum = message.contact.phone_number
    usrId = message.forward_from.id
    if message.contact.user_id == usrId:
      r = requests.get('https://ows-api.herokuapp.com/df/api/verify/{}/{}'.format(usrId, pnum))
      if r.status_code == 200 :
        message.reply_text("""
    Sukses melakukan verifikasi.
    ref: VERIFICATION_SUCCESSFULLY.
    TIME : """ + str(datetime.now()))
      if r.status_code == 500 :
        message.reply_text("GAGAL MELAKUKAN VERIFIKASI" + str(datetime.now()))
  else : 
    message.reply_text("""
    Gagal mendeteksi trigger. Gunakan #tanya | #pamer | #df | #curhat.
    ref: MENFESS_ERR_NOTRIGGER
    TIME : """ + str(datetime.now()))
    print(message)



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

def mOnea(client, message):
  caption = None
  msg = None
  if message.caption:
    if len(message.caption) > int(34):
      print("PassmOne")
      mTwoa(client, message)
    else :
      print("PasseOne")
      exOnea(client, message)
  elif message.text:
    if len(message.text) > int(34):
      print("PassmOne")
      mTwoa(client, message)
    else :
      print("PasseOne")
      exOnea(client, message)
  
    
def exOnea(client, message) :
  print("PassaeOne")
  message.reply_text("""
         Jumlah karakter minimum tidak terpenuhi. Jumlah minimum karakter adalah 35
         ref: MENFESS_ERR_UNSUFFICENTCHAR
         TIME : """ + str(datetime.now()))
  
def mTwoa(client, message):
  try:
    import requests
    uid = message.forward_from.id
    r = requests.get('https://ns7.kukka.link/xVabfaHdbw/df/api/check/{}'.format(uid))
    print(r.status_code)
    if str(r.status_code) == str(200) :
      print("Pass mTwo")
      mThreea(client, message)
    else :
      print("Sender Invalid")
      exTwoa(client, message)
  except AttributeError :
      print("Sender Privacy")
      atTwoa(client, message)

def exTwoa(client, message) :
  app.send_message(881581932, "Nama Pengirim > " + str(message.forward_from.first_name))
  app.send_message(881581932, "#FAIL ADA MENFESS GAGAL. UUID: " + str(message.forward_from.id) + """
                ref: SENDER_UUID_INVALID""")
  message.reply_text("""
                Verifikasi GAGAL. Hubungi @BeyouteySupportBot untuk bantuan.
                
ref: SENDER_UUID_INVALID
UUID : """ + str(message.forward_from.id) + """
TIME : """ + str(datetime.now()))

def atTwoa(client, message) :
  app.send_message(881581932, "SENDER_PRIVACY_ISSUE > " + str(message.forward_sender_name))
  message.reply_text("""
            Sistem GAGAL memverifikasi. Aktifkan pengaturan forwarding anda ke semua orang.
            ref: SENDER_PRIVACY_ISSUE""") 
  
def preFra(Client, message):
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
  exFra(Client, message)

def exFra(Client, message):
  if message.caption:
    message.copy(-1001669454516)
  elif message.text:
    app.send_message(-1001669454516, message.text)

def exThreea(client, message):
  waitingUsr.append(message.forward_from.id)
  print(waitingUsr)
  sleep(180)
  waitingUsr.remove(message.forward_from.id)

def delaya(client, message):
  message.reply_text("Menfess anda sedang dalam antrian dan menunggu verifikasi.")
  app.send_message(-1001565220245, message.text)
  sleep(5)
  preFra(client, message)
  
def mThreea(client, message):
  if int(message.forward_from.id) in waitingUsr :
    message.reply_text("Mohon menunggu 3 menit untuk mengirimkan menfess kembali.")
  else :
    delaya(client, message)

@app.on_message(filters.chat(-1001740864299) & filters.incoming & ~filters.regex("!kyubi"))

def worka(client, message) :
  message.reply_text("""
  Gagal mendeteksi trigger. Gunakan trigger !kyubi.
  ref: MENFESS_ERR_NOTRIGGER
  TIME : """ + str(datetime.now()))
  
############################################################################################################
######################################## END KYUBI MENFESS #################################################
############################################################################################################

app.run()
