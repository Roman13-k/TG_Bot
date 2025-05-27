import telebot
from config import TOKEN
from handlers import register_all_handlers
from utils.currency.codes import get_currency_code
from utils.currency.rates import set_currency_codes
from commands.set_commands import set_bot_commands

bot = telebot.TeleBot(TOKEN)
set_bot_commands(bot)
register_all_handlers(bot)
set_currency_codes(get_currency_code())

if __name__ == '__main__':
    bot.polling(non_stop=True)