from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

OWNER_ID = int(getenv("OWNER_ID", 1356469075))
LOGGER_GROUP_ID = int(getenv("LOGGER_GROUP_ID"))
START_IMAGE = getenv("START_IMAGE")
SUPPORT_CHAT = getenv("SUPPORT_CHAT")

# GitHub repository URL for updates
GITHUB_URL = getenv("GITHUB_URL")
