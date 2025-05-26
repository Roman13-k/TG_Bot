import telebot
from config import TOKEN
from utils.handlers import register_handlers
from utils.currency import get_currency_code, set_currency_codes
from commands import commands

bot = telebot.TeleBot(TOKEN)
commands(bot)
register_handlers(bot)
set_currency_codes(get_currency_code())

if __name__ == '__main__':
    bot.polling(non_stop=True)