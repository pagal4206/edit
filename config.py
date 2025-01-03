import os
DB_NAME = os.getenv("DB_NAME", "edit")
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URL")
OWNER_ID = os.getenv("OWNER_ID")
LOGGER_GROUP_ID = int(os.getenv("LOGGER_GROUP_ID"))