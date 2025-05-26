from telebot import TeleBot
from utils.currency import get_daily_currency, get_currency_history
from utils.graph import draw_currency_graph

user_states = {}


def register_handlers(bot: TeleBot):
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

    @bot.message_handler(commands=['kurs'])
    def ask_currency(message):
        parts = message.text.strip().split()
        if len(parts) == 2:
            currency_code = parts[1].upper()
            data = get_daily_currency(currency_code)
            if data:
                bot.send_message(message.chat.id,
                                 f"Курс: {data['nominal']} {currency_code} = {data['value']:.2f} ₽")
            else:
                bot.send_message(message.chat.id,
                                 "Не смог найти такую валюту. Попробуй USD, EUR, GBP и т.п.")
        else:
            user_states[message.chat.id] = 'waiting_for_currency'
            bot.send_message(message.chat.id,
                             "Пожалуйста, укажи код валюты (например: USD, EUR, GBP):")

    @bot.message_handler(func=lambda m: user_states.get(m.chat.id) == 'waiting_for_currency')
    def handle_currency_input(message):
        currency_code = message.text.strip().upper()
        data = get_daily_currency(currency_code)

        if data:
            bot.send_message(message.chat.id,
                             f"Курс: {data['nominal']} {currency_code} = {data['value']:.2f} ₽")
        else:
            bot.send_message(message.chat.id,
                             "Не смог найти такую валюту. Попробуй USD, EUR, GBP и т.п.")
        user_states[message.chat.id] = None

    @bot.message_handler(commands=['graph'])
    def graph(message):
        parts = message.text.strip().split()

        if len(parts) != 3:
            bot.send_message(
                message.chat.id,
                "Неверный формат команды.\nПример: /graph USD 7 (где 7 — количество дней)"
            )
            return

        currency_code = parts[1].upper()

        try:
            days = int(parts[2])
            if days <= 0:
                raise ValueError
        except ValueError:
            bot.send_message(message.chat.id, "Количество дней должно быть положительным числом.")
            return

        records = get_currency_history(currency_code, days)
        if not records:
            bot.send_message(message.chat.id,
                             "Не удалось получить данные по валюте. Убедитесь, что указали правильный код.")
            return

        image_stream = draw_currency_graph(records, currency_code)

        bot.send_photo(message.chat.id, image_stream)

    @bot.message_handler(func=lambda m: True)
    def handle_unknown(message):
        bot.send_message(message.chat.id,
                         "Я вас не понял. Введите /start для получения списка команд.")
