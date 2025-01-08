import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_TOKEN, LOGGER_GROUP_ID

bot = telebot.TeleBot(BOT_TOKEN)

def create_solution_button():
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton("🚀 Solution", callback_data="start_solution")
    keyboard.add(button)
    return keyboard

def warn_user(message):
    user = message.from_user
    if "edited" in message.text.lower():
        try:
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(
                message.chat.id,
                f"⚠️ <b>{user.first_name}</b>, your message was deleted because it contained an <b>edited message</b>.",
                parse_mode="HTML",
                reply_markup=create_solution_button()
            )
            bot.send_message(
                LOGGER_GROUP_ID,
                f"⚠️ <b>{user.first_name}</b> (<code>{user.id}</code>) had their message deleted in <b>{message.chat.title}</b> because it was an edited message.",
                parse_mode="HTML"
            )
        except Exception as e:
            print(f"Error deleting message: {e}")

@bot.callback_query_handler(func=lambda call: call.data == "start_solution")
def handle_solution_button(call):
    bot.send_message(call.message.chat.id, "🔄 Bot started successfully! Enjoy the features.")

def start_bot():
    print("Bot is running...")
    bot.polling(none_stop=True)

if __name__ == "__main__":
    start_bot()
