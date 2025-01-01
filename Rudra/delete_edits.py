import time

def handle_edited_message(bot, message):
    original_time = message.date
    current_time = int(time.time())
    time_diff = current_time - original_time

    if time_diff > 60:
        try:
            bot.delete_message(message.chat.id, message.message_id)
        except Exception as e:
            print(f"Error deleting message: {e}")