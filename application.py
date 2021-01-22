from flask import Flask, request, jsonify
import requests
import json

import config

app = Flask(__name__)


@app.route('/')
def index():
    return 'OK'

@app.route('/api/new_order', methods=['GET', 'POST'])
def new_order():
    data = request.json
    receive_url = config.receive_urls['new_order']
    print(data)
    print(requests.post(receive_url, data).text)
    return 'OK'

@app.route('/api/order_paid', methods=['GET', 'POST'])
def new_order():
    data = request.json
    receive_url = config.receive_urls['order_paid']
    print(data)
    print(requests.post(receive_url, data).text)
    return 'OK'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8181, debug=False)
