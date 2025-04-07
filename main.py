from flask import Flask, render_template, request
import json
from encryptor import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/authentication', methods=["POST", "GET"])
def check():
    if request.method == "POST":
        with open("static/data.json", "r") as contents:
            data=json.load(contents)
            try:
                if data[request.form["username"]] == enc(request.form["password"]):
                    return "lessgo"
                else:
                    return "wrong"
            except KeyError:
                return "wrong"
            except TypeError:
                return "wrong"


if __name__ == "__main__":
    app.run(debug=True)