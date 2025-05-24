import requests
import xml.etree.ElementTree as ET
from config import CB_URL

def get_currency(currency_code: str) ->dict|None:
    r = requests.get(CB_URL)
    tree = ET.fromstring(r.content)
    for valute in tree.findall('Valute'):
        if valute.find('CharCode').text == currency_code:
            nominal = int(valute.find('Nominal').text)
            value_str = valute.find('Value').text
            value = float(value_str.replace(',', '.'))

            return {
                "nominal": nominal,
                "value": value
            }
    return None