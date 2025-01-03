from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def send_start_message(bot, message):
    """Sends the start message with inline buttons."""
    full_name = f"{message.from_user.first_name} {message.from_user.last_name or ''}".strip()
    start_text = (
        f"Hello {full_name} 👋, I'm your 𝗘𝗱𝗶𝘁 𝗚𝘂𝗮𝗿𝗱𝗶𝗮𝗻 𝗕𝗼𝘁, here to maintain a secure environment for our discussions.\n\n"
        "🚫 𝗘𝗱𝗶𝘁𝗲𝗱 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 𝗗𝗲𝗹𝗲𝘁𝗶𝗼𝗻: 𝗜'𝗹𝗹 𝗿𝗲𝗺𝗼𝘃𝗲 𝗲𝗱𝗶𝘁𝗲𝗱 𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀 𝘁𝗼 𝗺𝗮𝗶𝗻𝘁𝗮𝗶𝗻 𝘁𝗿𝗮𝗻𝘀𝗽𝗮𝗿𝗲𝗻𝗰𝘆.\n\n"
        "📣 𝗡𝗼𝘁𝗶𝗳𝗶𝗰𝗮𝗻𝗰𝗲𝘀: 𝗬𝗼𝘂'𝗹𝗹 𝗯𝗲 𝗶𝗻𝗳𝗼𝗿𝗺𝗲𝗱 𝗲𝗮𝗰𝗵 𝘁𝗶𝗺𝗲 𝗮 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝗶𝘀 𝗱𝗲𝗹𝗲𝘁𝗲𝗱.\n\n"
        "🌟 𝗚𝗲𝘁 𝗦𝘁𝗮𝗿𝘁𝗲𝗱:\n"
        "1. Add me to your group.\n"
        "2. I'll start protecting instantly.\n\n"
        "➡️ Click on 𝗔𝗱𝗱 𝗚𝗿𝗼𝘂𝗽 to add me and keep our group safe!"
    )

    markup = InlineKeyboardMarkup(row_width=2)  
    markup.add(
        InlineKeyboardButton("Add Group", url="https://t.me/SARKAR_CHEAT_HACK_BOT?startgroup=s&admin=delete_messages+invite_users"),
        InlineKeyboardButton("Update Group", url="https://t.me/Mat_Dek_Bura_Man_Jye_Ga")
    )
    markup.add(InlineKeyboardButton("Update Channel", url="https://t.me/Mat_Dek_Bura_Man_Jye_Ga"))

    bot.send_message(message.chat.id, start_text, reply_markup=markup)