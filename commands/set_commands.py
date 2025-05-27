from telebot.types import BotCommand


def set_bot_commands(bot):
    bot.set_my_commands([
        BotCommand("start", "Начать работу с ботом"),
        BotCommand("kurs", "Узнать курс валюты (например: /kurs <валюта>)"),
        BotCommand("graph", "Построить график /graph <валюта> <дни>")
    ])
