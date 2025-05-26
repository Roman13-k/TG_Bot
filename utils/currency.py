import requests
import xml.etree.ElementTree as ET
from config import CB_URL, CB_DYNAMIC_URL
from datetime import datetime, timedelta

CURRENCY_CODES = {}

def set_currency_codes(codes: dict):
    global CURRENCY_CODES
    CURRENCY_CODES = codes

def get_currency_code():
    response = requests.get(CB_URL)
    tree = ET.fromstring(response.text)
    code = {}
    for valute in tree.findall('Valute'):
        char_code = valute.find('CharCode').text
        val_code = valute.attrib.get('ID')
        code[char_code] = val_code
    return code


def get_daily_currency(currency_code: str) -> dict | None:
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


def get_currency_history(currency_code: str, days: int = 7) -> dict | None:
    val_code = CURRENCY_CODES.get(currency_code)
    if not val_code:
        return None

    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    params = {
        "date_req1": start_date.strftime('%d/%m/%Y'),
        "date_req2": end_date.strftime('%d/%m/%Y'),
        "VAL_NM_RQ": val_code
    }

    r = requests.get(CB_DYNAMIC_URL, params=params)
    tree = ET.fromstring(r.content)
    records = {}

    for record in tree.findall('Record'):
        date = record.attrib["Date"]
        value = float(record.find("Value").text.replace(",", "."))
        nominal = int(record.find("Nominal").text)
        records[date] = round(value / nominal, 4)
    return records
