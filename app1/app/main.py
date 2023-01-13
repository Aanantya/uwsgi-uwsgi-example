from app import app
from flask import jsonify
import requests


@app.route('/')
def index():
    return jsonify({"message": "Hello World"})


@app.route('/sayHi')
def sayHi():
    url = 'http://app2:8081/sayHi'

    data = {'message': 'Hi from app1!'}

    headers = {'Content-type': 'text/html; charset=UTF-8'}

    res = requests.post(url, data=data, headers=headers)

    return jsonify({"message": res.text})
