def handle_media_edited_message(bot, message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
    except Exception as e:
        print(f"Error deleting media edit message: {e}")