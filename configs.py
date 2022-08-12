# (c) @berlinx

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "6309305"))
	API_HASH = os.environ.get("API_HASH", "8b0473750d327598c8585b0049f09e2d")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "5458768378:AAGrwPBrwpKtFdiHM3hwziCQChVJb56mfM4")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "FilesX_R0Bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001559968759"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1757568732"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://files:TxWRXcNulO6NFsi2@cluster0.xc8lluf.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001545325843")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001742695883")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
★ This is Permanent Files Store Bot!
Send me any file I will save it in my Database. 

**Powered by : @Tamil_MVs_Offl**

▬▬▬▬▬▬▬▬▬▬▬▬▬▬

 [Movies Search & Auto Filter BOT](https://t.me/Tamil_Mvs_Filter_bot), Search Movies in telegram...

Upto 132118+ Files in Database...

Bot is also working in groups...
"""
	ABOUT_DEV_TEXT = f"""
**📢 Our Official Main Channels & Groups📢
----------------------------------------------
⭕️ Tamil MVs Movies - 3.0 
  ➥ https://t.me/+AC2fLsEes9A1NDU1
----------------------------------------------
⭕️ Tamil Dubbed Movies
  ➥ https://t.me/+ZB2uIDoIDVs1YWJl
----------------------------------------------
⭕️ Web Series Channel 
  ➥ https://t.me/+kVEEFuW6bqJiZDk1
----------------------------------------------
⭕️ MX Cinemas (Watch Online)
  ➥ https://t.me/+w2rNCoE9JMBkYjc9
----------------------------------------------
⭕️ Theater Movies Channel
  ➥ https://t.me/+SLp0nh2GVQtiODhl
----------------------------------------------
⭕️ Marvel Movies Collection
  ➥ https://t.me/+47mqBFaDtpBlNTc1

▬▬▬▬▬▬▬▬▬▬▬▬▬▬

@Tamil_MVs_Offl**
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! 

Check **🌟 Official Channels** Button.
"""
