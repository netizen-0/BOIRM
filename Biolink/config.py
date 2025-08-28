import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", 20536459))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", 7538572906))
MONGO_URI = os.getenv("MONGO_URI")
