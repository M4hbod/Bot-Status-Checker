from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
SESSION_STRING = getenv("SESSION_STRING")
TIME_ZONE = getenv("TIME_ZONE")
BOT_LIST = list(getenv("BOT_LIST").split())
CHANNEL_OR_GROUP_ID = int(getenv("CHANNEL_OR_GROUP_ID"))
MESSAGE_ID = int(getenv("MESSAGE_ID"))
BOT_ADMIN_IDS = list(map(str, getenv("BOT_ADMIN_IDS").split()))
CHECK_DELAY = int(getenv("CHECK_DELAY"))