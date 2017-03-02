from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", title="Index page")


if __name__ == '__main__':
    app.run()
