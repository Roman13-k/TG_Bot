def register_fallback_handler(bot):
    @bot.message_handler(func=lambda m: True)
    def handle_unknown(message):
        bot.send_message(message.chat.id,
                         "Я вас не понял. Введите /start для получения списка команд.")
