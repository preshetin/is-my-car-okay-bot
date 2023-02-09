from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def home():
    result =  {
        "message": "Work in progress",
        "distance": 600000
    }
    return jsonify(result)
    return 'Hello, World bro'

@app.route('/about')
def about():
    return 'About'
