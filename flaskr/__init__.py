import os
import datetime
from dotenv import load_dotenv
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection
from flask import Flask, render_template, redirect, request, url_for
from flaskr.ebay import *

load_dotenv()
DEV_KEY = os.getenv('DEV_KEY')

app = Flask(__name__)

ebay = Ebay(DEV_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    keywords = request.form['keywords']
    parameters = request.form['parameters']
    print(keywords)
    print(parameters)
    data = ebay.query(keywords)
    return data

@app.route('/save', methods=['POST', 'GET'])
def storage():
    return  render_template('save.html')

if __name__ == '__main__':
    app.run(debug=True)
