import telebot
from config import BOT_TOKEN, OWNER_ID
from rudra.start import send_start_message
from rudra.user import get_user_count, get_group_count, add_user, add_group

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



if __name__ == "__main__":
    bot.infinity_polling()