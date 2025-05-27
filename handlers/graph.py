from utils.currency.rates import get_currency_history
from utils.graphs.currency_graph import draw_currency_graph
from UI.loading import show_loading, hide_loading
from utils.rate_limiter import rate_limited


def register_graph_handler(bot):
    @bot.message_handler(commands=['graph'])
    @rate_limited(bot)
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
            if days <= 0 or days > 365:
                raise ValueError
        except ValueError:
            bot.send_message(message.chat.id, "Неверное количество дней (от 1 до 365).")
            return

        loading_msg = show_loading(bot, message.chat.id)
        try:
            records = get_currency_history(currency_code, days)
            if not records:
                bot.send_message(
                    message.chat.id,
                    "Не удалось получить данные по валюте. Убедитесь, что указали правильный код."
                )
                return

            image_stream = draw_currency_graph(records, currency_code)
            bot.send_photo(message.chat.id, image_stream)
        finally:
            hide_loading(bot, message.chat.id, loading_msg)
