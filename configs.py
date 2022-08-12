# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "0"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-100"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1445283714"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
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
