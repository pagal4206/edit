import telebot
from config import BOT_TOKEN, OWNER_ID
from rudra.start import send_start_message
from rudra.delete_media_edits import handle_media_edited_message
from rudra.user import get_group_count, get_user_count, add_group, add_user
from rudra.warn import warn_user
from rudra.broadcast import send_broadcast_message

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def handle_start(message):
    user_id = message.from_user.id
    add_user(user_id)
    send_start_message(bot, message)

@bot.edited_message_handler(func=lambda message: True)
def on_message_edited(message):
    warn_user(bot, message)

@bot.edited_message_handler(content_types=["photo", "video", "audio", "document", "voice"])
def on_media_edited(message):
    warn_user(bot, message)
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
    bot.infinity_polling()
