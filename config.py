import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
CB_URL = os.getenv('CB_URL')