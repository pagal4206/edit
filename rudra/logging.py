from config import LOGGER_GROUP_ID

def log_event(bot, message):
    """
    Sends a log message to the logger group.
    """
    try:
        bot.send_message(
            chat_id=LOGGER_GROUP_ID,
            text=message,
            parse_mode="HTML"
        )
    except Exception as e:
        print(f"Logging failed: {e}")

def log_bot_start(bot):
    """
    Logs when the bot starts.
    """
    log_event(bot, "🚀 <b>Bot has been started or restarted.</b>")

def log_user_join(bot, new_member, chat_title):
    """
    Logs when a new user joins a group.
    """
    log_event(
        bot,
        f"👤 New user joined: <b>{new_member.first_name}</b> "
        f"(<code>{new_member.id}</code>) in group <b>{chat_title}</b>."
    )

def log_bot_added_to_group(bot, chat_title, chat_id):
    """
    Logs when the bot is added to a group.
    """
    log_event(
        bot,
        f"➕ Bot added to group: <b>{chat_title}</b> (<code>{chat_id}</code>)."
    )

def log_bot_removed_from_group(bot, chat_title, chat_id):
    """
    Logs when the bot is removed from a group.
    """
    log_event(
        bot,
        f"❌ Bot removed from group: <b>{chat_title}</b> (<code>{chat_id}</code>)."
    )