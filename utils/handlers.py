from telebot import TeleBot
from telebot import types
from utils.currency import get_currency
def register_handlers(bot: TeleBot):
    @bot.message_handler(commands=['start'])
    def start(message):
        first_name = (message.from_user.first_name or "").capitalize()
        last_name = (message.from_user.last_name or "").capitalize()

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add("/kurs USD", "/kurs EUR", "/kurs GBP")

        text = f"Привет, {first_name} {last_name}! 👋\n\n" \
               "Вот список доступных команд:\n" \
               "• /kurs USD — курс доллара\n" \
               "• /kurs EUR — курс евро\n" \
               "• /kurs GBP — курс фунта\n\n" \
               "Выберите команду снизу ⬇️"

        bot.send_message(
            message.chat.id,
            text,
            reply_markup=keyboard
        )

    @bot.message_handler(commands=['kurs'])
    def currency(message):
        parts=message.text.split(' ')
        if len(parts) != 2:
            bot.send_message(message.chat.id,
       "Пожалуйста, укажи валюту, например: /kurs USD")
            return

        currency = parts[1].upper()
        data= get_currency(currency)
        if data:
            bot.send_message(message.chat.id,
        f"Курс: {data['nominal']} {currency} к рублю: {data['value']:.2f} ₽")
        else:
            bot.send_message(message.chat.id,
        "Не смог найти такую валюту. Попробуй USD, EUR, GBP и т.п.")
