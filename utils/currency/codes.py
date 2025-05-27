import requests
import xml.etree.ElementTree as ET
from config import CB_URL


def get_currency_code():
    response = requests.get(CB_URL)
    tree = ET.fromstring(response.text)
    code = {}
    for valute in tree.findall('Valute'):
        char_code = valute.find('CharCode').text
        val_code = valute.attrib.get('ID')
        code[char_code] = val_code
    return code
