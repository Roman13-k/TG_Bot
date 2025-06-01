import time
from functools import wraps

user_last_request = {}

RATE_LIMIT_SECONDS = 1.5


def rate_limited(bot):
    def decorator(func):
        @wraps(func)
        def wrapper(message, *args, **kwargs):
            user_id = message.from_user.id
            now = time.time()
            last = user_last_request.get(user_id)

            if last and now - last < RATE_LIMIT_SECONDS:
                msg = bot.send_message(message.chat.id, "⏱ Пожалуйста, не так быстро!")
                time.sleep(3)
                bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
                return

            user_last_request[user_id] = now
            return func(message, *args, **kwargs)

        return wrapper

    return decorator
