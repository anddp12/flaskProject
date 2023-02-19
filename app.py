from flask import Flask
from flask import url_for, render_template, send_file, redirect

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template("index.html", head1="head")


if __name__ == '__main__':
    app.run()
