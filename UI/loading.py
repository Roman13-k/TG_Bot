def show_loading(bot, chat_id, text="Загрузка..."):
    return bot.send_message(chat_id, text)


def hide_loading(bot, chat_id, message):
    try:
        bot.delete_message(chat_id=chat_id, message_id=message.message_id)
    except Exception:
        return
