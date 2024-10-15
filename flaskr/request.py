import os
from dotenv import load_dotenv
from ebay import *

load_dotenv()
print(os.getenv('DEV_KEY'))

ebay = Ebay()