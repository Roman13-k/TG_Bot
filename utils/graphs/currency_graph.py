import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from io import BytesIO
from datetime import datetime


def draw_currency_graph(records: dict, currency_code: str) -> BytesIO:
    dates = [datetime.strptime(date_str, "%d.%m.%Y") for date_str in records.keys()]
    values = list(records.values())

    plt.figure(figsize=(10, 5))
    plt.plot(dates, values, marker='o', linestyle='-', color='blue')
    plt.title(f"Курс {currency_code} к рублю")
    plt.xlabel("Дата")
    plt.ylabel("Курс, ₽")

    if len(dates) > 90:
        locator = mdates.WeekdayLocator(interval=4)
        formatter = mdates.DateFormatter("%d.%m.%Y")
    elif len(dates) > 30:
        locator = mdates.WeekdayLocator(interval=1)
        formatter = mdates.DateFormatter('%d/%m')
    else:
        locator = mdates.AutoDateLocator()
        formatter = mdates.DateFormatter('%d/%m')

    plt.gca().xaxis.set_major_locator(locator)
    plt.gca().xaxis.set_major_formatter(formatter)

    plt.xticks(rotation=45)
    plt.tight_layout()

    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    plt.close()

    image_stream.seek(0)
    return image_stream
