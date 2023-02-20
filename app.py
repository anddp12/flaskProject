from flask import Flask
from flask import url_for, render_template, send_file, redirect
import json
import requests
import random

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template("index.html", head1="head")


@app.route('/temp')
def temp():  # put application's code here
    response = requests.get("http://localhost:5000/api")
    json_data = json.loads(response.text)
    temperature = json_data.get('temperature')
    return render_template("temperature.html", temperature=temperature)


@app.route('/humidity')
def hum():  # put application's code here
    response = requests.get("http://localhost:5000/api")
    json_data = json.loads(response.text)
    humidity = json_data.get('humidity')
    return render_template("humidity.html", humidity=humidity)


@app.route('/meter')
def meter():  # put application's code here
    return render_template("meter.html")


@app.route('/boiler')
def boiler():  # put application's code here
    return render_template("boiler.html")


@app.route('/api')
def api():
    obj = None
    with open('static/example.json', 'r') as file:
        obj = json.load(file)

    obj['temperature'] = random.randint(18, 25)
    obj['humidity'] = random.randint(40, 100)
    obj['meter']['electricity']['reading'] = round(random.uniform(12345.9, 12347.9), 3)
    obj['meter']['electricity']['consumption'] = round(random.uniform(0.1, 2.0), 1)
    obj['meter']['gas']['reading'] = round(random.uniform(2367.9, 2369.9), 3)
    obj['meter']['gas']['consumption'] = round(random.random(), 1)
    obj['meter']['water']['reading'] = round(random.uniform(1212.9, 1214.9), 3)
    obj['meter']['water']['consumption'] = round(random.uniform(0.1, 1.0), 1)
    obj['boiler']['isRun'] = random.choice([True, False])
    obj['boiler']['temperature'] = random.randint(60, 80)
    obj['boiler']['pressure'] = round(random.uniform(1.0, 2.0), 1)

    return json.dumps(obj)


if __name__ == '__main__':
    app.run()
