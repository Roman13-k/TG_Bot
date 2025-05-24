from telebot.types import BotCommand

def commands(bot):
    bot.set_my_commands([
        BotCommand("start", "Начать работу с ботом"),
        BotCommand("kurs", "Узнать курс валюты (например: /курс USD)")
    ])