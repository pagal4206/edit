import telebot
from config import BOT_TOKEN, OWNER_ID, LOGGER_GROUP_ID
from rudra.start import send_start_message
from rudra.delete_edits import handle_edited_message
from rudra.delete_media_edits import handle_media_edited_message
from rudra.logging import log_event, log_bot_start, log_user_join, log_bot_added_to_group, log_bot_removed_from_group
from rudra.user import get_all_groups, get_all_users, get_group_count, get_user_count, add_group, add_user
from rudra.broadcast import send_broadcast_message

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def handle_start(message):
    send_start_message(bot, message)

@bot.edited_message_handler(func=lambda message: True)
def on_message_edited(message):
    handle_edited_message(bot, message)

@bot.edited_message_handler(content_types=["photo", "video", "audio", "document", "voice"])
def on_media_edited(message):
    handle_media_edited_message(bot, message)

@bot.message_handler(commands=["user"])
def handle_user_count(message):
    if str(message.from_user.id) == OWNER_ID:
        user_count = get_user_count()
        bot.send_message(message.chat.id, f"Total users: {user_count}")
    else:
        bot.send_message(message.chat.id, "You are not authorized to use this command.")

@bot.message_handler(commands=["group"])
def handle_group_count(message):
    if str(message.from_user.id) == OWNER_ID:
        group_count = get_group_count()
        bot.send_message(message.chat.id, f"Total groups: {group_count}")
    else:
        bot.send_message(message.chat.id, "You are not authorized to use this command.")

@bot.message_handler(content_types=["new_chat_members"])
def on_new_member(message):
    for new_member in message.new_chat_members:
        add_user(new_member.id)
        add_group(message.chat.id)
        log_user_join(bot, new_member, message.chat.title)

@bot.message_handler(content_types=["left_chat_member"])
def on_left_member(message):
    log_bot_removed_from_group(bot, message.chat.title, message.chat.id)

@bot.message_handler(content_types=["new_chat_members"])
def on_new_chat_member(message):
    log_bot_added_to_group(bot, message.chat.title, message.chat.id)

@bot.message_handler(commands=['broadcast'])
def handle_broadcast(message):
    if str(message.from_user.id) == OWNER_ID:
        message_text = message.text[11:]
        if message_text:
            send_broadcast_message(message_text)
            bot.reply_to(message, "Broadcast message sent to all users and groups!")
        else:
            bot.reply_to(message, "Please provide a message to broadcast.")
    else:
        bot.reply_to(message, "You are not authorized to use this command.")

if __name__ == "__main__":
    log_bot_start(bot)
    bot.infinity_polling()
