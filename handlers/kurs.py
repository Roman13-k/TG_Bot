from utils.currency.rates import get_daily_currency
from utils.rate_limiter import rate_limited
from db.cache import get_cached_currency, set_cached_currency
from telebot import types

user_states = {}


def register_kurs_handler(bot):
    @bot.message_handler(commands=['kurs'])
    @rate_limited(bot)
    def ask_currency(message):
        parts = message.text.strip().split()
        if len(parts) == 2:
            currency_code = parts[1].upper()

            data = get_or_cache_currency(currency_code)

            if data:
                bot.send_message(message.chat.id,
                                 f"Курс: {data['nominal']} {currency_code} = {data['value']:.2f} ₽")
            else:
                bot.send_message(message.chat.id,
                                 "Не смог найти такую валюту. Попробуй USD, EUR, GBP и т.п.")
        else:
            markup = types.InlineKeyboardMarkup()
            markup.row(
                types.InlineKeyboardButton("USD", callback_data="kurs_USD"),
                types.InlineKeyboardButton("EUR", callback_data="kurs_EUR")
            )
            markup.row(
                types.InlineKeyboardButton("BYN", callback_data="kurs_BYN"),
                types.InlineKeyboardButton("CNY", callback_data="kurs_CNY")
            )
            bot.reply_to(message, "Пожалуйста, выбери валюту или напиши её код вручную:", reply_markup=markup)
            user_states[message.chat.id] = 'waiting_for_currency'

    @bot.callback_query_handler(func=lambda callback: callback.data.startswith("kurs_"))
    def kurs_callback(callback):
        currency_code = callback.data.split("_")[1]

        data = get_or_cache_currency(currency_code)

        if data:
            response = f"Курс: {data['nominal']} {currency_code} = {data['value']:.2f} ₽"
        else:
            response = "Не удалось получить курс. Попробуй позже или укажи другую валюту."

        bot.edit_message_text(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            text=response
        )
        bot.answer_callback_query(callback.id)

    @bot.message_handler(func=lambda m: user_states.get(m.chat.id) == 'waiting_for_currency')
    @rate_limited(bot)
    def handle_currency_input(message):
        currency_code = message.text.strip().upper()

        data = get_or_cache_currency(currency_code)

        if data:
            bot.send_message(message.chat.id,
                             f"Курс: {data['nominal']} {currency_code} = {data['value']:.2f} ₽")
        else:
            bot.send_message(message.chat.id,
                             "Не смог найти такую валюту. Попробуй USD, EUR, GBP и т.п.")
        user_states[message.chat.id] = None


def get_or_cache_currency(code: str):
    data = get_cached_currency(code)
    if not data:
        data = get_daily_currency(code)
        if data:
            set_cached_currency(code, data)
    return data
