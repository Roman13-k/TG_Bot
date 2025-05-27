from .start import register_start_handler
from .kurs import register_kurs_handler
from .graph import register_graph_handler
from .fallback import register_fallback_handler


def register_all_handlers(bot):
    register_start_handler(bot)
    register_kurs_handler(bot)
    register_graph_handler(bot)
    register_fallback_handler(bot)
