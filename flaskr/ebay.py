import os
import datetime
from dotenv import load_dotenv
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection
from flask import Flask, render_template, redirect, request, url_for
import requests
from flaskr.ebay import *

class Ebay():
    def __init__(self, DEV_KEY):
        self.DEV_KEY = DEV_KEY
        pass
    def query(self, keywords):
        try:
            # api = Connection(appid=self.DEV_KEY, config_file=None)
            # response = api.execute('findItemsAdvanced', {'keywords': {keywords}, 'categoryId': ['11116']})
            URL = "https://svcs.ebay.com/services/search/FindingService/v1?"
            OPERATION = "Operation-Name=findItemsAdvanced"
            SERVICE_VERSION = "&Service-Version=1.0.0"
            SECURITY_APPNAME = f"&Security-AppName={self.DEV_KEY}"
            RESPONSE_FORMAT = "&Response-Data-Format=JSON&REST-Payload"
            KEYWORDS = "&keywords=Coin%201967%20Canada%201%20Cent&categoryId=11116"
            # ASPECT_FILTER = "&aspectFilter.aspectName=Color&aspectFilter.aspectValueName=RB&aspectFilter.aspectName=Color&aspectFilter.aspectValueName=RD"
            ASPECT_FILTER = ""

            url = URL + OPERATION + SERVICE_VERSION + SECURITY_APPNAME + RESPONSE_FORMAT + KEYWORDS + ASPECT_FILTER

            response = requests.get(url)

                # Check if the request was successful
            if response.status_code == 200:
                # Process the JSON response
                data = response.json()
                return data
            else:
                # Handle errors
                print(f"Error: {response.status_code}")
                return None
                
        except ConnectionError as e:
            print(e)
            print(e.response.dict())
    def parse(self, response):
        pass
