import matplotlib.pyplot as plt
from io import BytesIO


def draw_currency_graph(records: dict, currency_code: str) -> BytesIO:
    dates = list(records.keys())
    values = list(records.values())

    plt.figure(figsize=(10, 5))
    plt.plot(dates, values, marker='o', linestyle='-', color='blue')
    plt.title(f"Курс {currency_code} к рублю")
    plt.xlabel("Дата")
    plt.ylabel("Курс, ₽")
    plt.xticks(rotation=45)
    plt.tight_layout()

    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')

    image_stream.seek(0)
    return image_stream
