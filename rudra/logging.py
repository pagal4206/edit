import logging
import telebot
from config import LOGGER_GROUP_ID, BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def log_message(message):
    try:
        bot.send_message(chat_id=LOGGER_GROUP_ID, text=message)
    except Exception as e:
        logging.error(f"Error sending log message: {e}")

def log_user_activity(user_id):
    log_message(f"User {user_id} has started the bot.")

def log_group_activity(group_id, action):
    log_message(f"Bot has been {action} to group {group_id}.")
