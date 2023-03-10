import requests
import json
from flask import render_template
import random


def temp():
    title = 'Temperature'
    response = requests.get("http://localhost:5000/api")
    json_data = json.loads(response.text)
    temperature = json_data.get('temperature')
    return render_template("temperature.html", temperature=temperature, title=title)


def hum():
    title = 'Humidity'
    response = requests.get("http://localhost:5000/api")
    json_data = json.loads(response.text)
    humidity = json_data.get('humidity')
    return render_template("humidity.html", humidity=humidity, title=title)


def meter():  # put application's code here
    title = 'Meter'
    response = requests.get("http://localhost:5000/api")
    json_data = json.loads(response.text)
    electricity1 = json_data['meter']['electricity']['reading']
    electricity2 = json_data['meter']['electricity']['consumption']
    gas1 = json_data['meter']['gas']['reading']
    gas2 = json_data['meter']['gas']['consumption']
    water1 = json_data['meter']['water']['reading']
    water2 = json_data['meter']['water']['consumption']
    return render_template("meter.html", electricity1=electricity1, electricity2=electricity2, gas1=gas1,
                           gas2=gas2,
                           water1=water1, water2=water2, title=title)


def boiler():
    title = 'Boiler'
    response = requests.get("http://localhost:5000/api")
    json_data = json.loads(response.text)
    boiler1 = json_data['boiler']['isRun']
    boiler2 = json_data['boiler']['temperature']
    boiler3 = json_data['boiler']['pressure']
    return render_template("boiler.html", boiler1=boiler1, boiler2=boiler2, boiler3=boiler3, title=title)


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
