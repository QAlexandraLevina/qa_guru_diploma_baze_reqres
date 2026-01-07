import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv('REQRES_BASE_URL')
API_KEY = {'x-api-key': os.getenv('REQRES_API_KEY')}
