from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>🚗🧑🏼‍🔧</h1><h1>Is My Car Okay?</h1><p>Track your car health by adding milage and periodic maintence.</p>'

@app.route('/check', methods=["POST"])
def check():
    data = request.json 

    # Текущий пробег
    probeg = data.get("probeg")

    # Сравнить текущий пробег с запланированными задачами

    result =  {
        "message": "Work in progress",
        "probeg": probeg
    }
    return jsonify(result)

@app.route('/about')
def about():
    return 'About'
