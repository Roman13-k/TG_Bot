import telebot
from config import TOKEN
from utils.handlers import register_handlers
from commands import commands

bot = telebot.TeleBot(TOKEN)
commands(bot)
register_handlers(bot)

if __name__ == '__main__':
    bot.polling(non_stop=True)