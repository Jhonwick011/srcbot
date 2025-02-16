# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "25129557"))
API_HASH = getenv("API_HASH", "83c9546cfdee154fd2d16759c4d0582a")
BOT_TOKEN = getenv("BOT_TOKEN", "7508106908:AAHStuuR8POHVOtCNOuSMshp_NdZZFI8YjY")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1923238241").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://jhonwickpk01:ZrMM6aWtOh7os2eR@cluster0.icxrg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002247795848"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
