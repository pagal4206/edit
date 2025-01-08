import logging
import telebot
from datetime import datetime
from config import LOGGER_GROUP_ID, BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def log_message(chat_id, message, photo=None):
    try:
        if photo:
            bot.send_photo(chat_id=chat_id, photo=photo, caption=message, parse_mode="Markdown")
        else:
            bot.send_message(chat_id=chat_id, text=message, parse_mode="Markdown")
    except Exception as e:
        logging.error(f"Error sending log message: {e}")

def log_user_activity(user_id, username=None, first_name=None):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_profile_photos = bot.get_user_profile_photos(user_id)
    profile_photo = user_profile_photos.photos[0][0].file_id if user_profile_photos.total_count > 0 else None
    
    mention = f"[{first_name}](tg://user?id={user_id})" if first_name else f"[User](tg://user?id={user_id})"
    username_display = f"@{username}" if username else "Not Set"

    message = (
        f"✨ *User Activity Log*\n"
        f"━━━━━━━━━━━━━━━━━━━\n"
        f"👤 *User ID:* `{user_id}`\n"
        f"🙋 *Name:* {mention}\n"
        f"🔗 *Username:* {username_display}\n"
        f"🔄 *Action:* Started the bot\n"
        f"⏰ *Time:* `{current_time}`\n"
        f"📡 *Bot Status:* Active\n"
        f"━━━━━━━━━━━━━━━━━━━\n"
        f"💎 _Welcome to our bot!_\n"
    )

    log_message(LOGGER_GROUP_ID, message, photo=profile_photo)

def log_group_activity(group_id, group_title, action):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    group_photo = None

    try:
        chat = bot.get_chat(group_id)
        if chat.photo:
            group_photo = bot.get_file(chat.photo.big_file_id).file_id
    except Exception as e:
        logging.error(f"Error fetching group photo: {e}")

    action_emoji = "➕" if action.lower() == "added" else "➖"
    message = (
        f"✨ *Group Activity Log*\n"
        f"━━━━━━━━━━━━━━━━━━━\n"
        f"👥 *Group ID:* `{group_id}`\n"
        f"🏷️ *Group Name:* {group_title}\n"
        f"{action_emoji} *Action:* {action.capitalize()}\n"
        f"⏰ *Time:* `{current_time}`\n"
        f"📡 *Bot Status:* Active\n"
        f"━━━━━━━━━━━━━━━━━━━\n"
        f"🌟 _Your group is now connected!_\n"
    )

    log_message(LOGGER_GROUP_ID, message, photo=group_photo)
