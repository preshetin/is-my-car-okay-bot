from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World bro'

@app.route('/about')
def about():
    return 'About'
