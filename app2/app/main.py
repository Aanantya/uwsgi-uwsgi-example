from app import app
from flask import request, jsonify


@app.route('/sayHi', methods=['GET', 'POST'])
def sayHi():
    r = request.data
    print(r)

    return 'Hi from app2'