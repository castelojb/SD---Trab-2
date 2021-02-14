import os
from dotenv import load_dotenv

load_dotenv()

SERVERIP = os.getenv('SERVERIP')
SERVERPORT = int(os.getenv('SERVERPORT'))
