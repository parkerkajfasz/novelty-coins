# import os
# import datetime
# from dotenv import load_dotenv
# from ebaysdk.exception import ConnectionError
# from ebaysdk.finding import Connection
# from ebay import *

# load_dotenv()
# DEV_KEY = os.getenv('DEV_KEY')

# ebay = Ebay()

# try:
#     api = Connection(appid=DEV_KEY, config_file=None)
    # response = api.execute('findItemsAdvanced', {'keywords': 'Coin 1967 Canada 1 Cent', 'categoryId': ['11116']})

#     for item in response.reply.searchResult.item:
#         pass
        
# except ConnectionError as e:
#     print(e)
#     print(e.response.dict())

