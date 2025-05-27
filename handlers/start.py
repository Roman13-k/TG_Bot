def register_start_handler(bot):
    @bot.message_handler(commands=['start'])
    def start(message):
        first_name = (message.from_user.first_name or "").capitalize()
        last_name = (message.from_user.last_name or "").capitalize()

        text = (
            f"Привет, {first_name} {last_name}! 👋\n\n"
            "Вот список доступных команд:\n"
            "• /kurs <валюта> — узнать курс валюты\n"
            "• /graph <валюта> <дни> — график курса валюты за указанное количество дней\n"
        )

        bot.send_message(message.chat.id, text)
