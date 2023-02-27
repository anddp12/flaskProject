import requests
import json
from flask import render_template


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
