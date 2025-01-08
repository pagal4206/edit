from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import LOGGER_GROUP_ID

def create_solution_button():
    """
    Creates an inline keyboard with the "Solution" button.
    """
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton("🚀 Solution", callback_data="start_solution")
    keyboard.add(button)
    return keyboard

def warn_user(bot, message):
    """
    Warns the user for sending an edited message and logs the event.
    """
    user = message.from_user
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

def handle_solution_button(bot, call):
    """
    Handles the "Solution" button callback.
    """
    bot.send_message(call.message.chat.id, "🔄 Bot started successfully! Enjoy the features.")
