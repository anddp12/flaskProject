from flask import Flask
from flask import url_for, render_template, send_file, redirect

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template("index.html", head1="head")


@app.route('/temp')
def temp():  # put application's code here
    return render_template("temperature.html")


@app.route('/humidity')
def humidity():  # put application's code here
    return render_template("humidity.html")


@app.route('/meter')
def meter():  # put application's code here
    return render_template("meter.html")


@app.route('/boiler')
def boiler():  # put application's code here
    return render_template("boiler.html")


if __name__ == '__main__':
    app.run()
