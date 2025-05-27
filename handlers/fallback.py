def register_fallback_handler(bot):
    @bot.message_handler(func=lambda m: True)
    def handle_unknown(message):
        chat_type = message.chat.type
        if (chat_type == "group" or chat_type == "channel" or chat_type == "supergroup"):
            return
        else:
            bot.send_message(message.chat.id,
                             f"Я вас не понял {chat_type}. Введите /start для получения списка команд.")
