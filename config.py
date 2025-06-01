import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
CB_URL = os.getenv('CB_URL')
CB_DYNAMIC_URL = os.getenv('CB_DYNAMIC_URL')
DB_NAME = os.getenv('DB_NAME')
