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
        with open("static/data.json", "r") as datafile:
            data=json.load(datafile)
            try:
                if data[request.form["username"]]["password"] == enc(request.form["password"]):
                    return "lessgo"
                else:
                    return "wrong"
            except KeyError:
                return "wrong"
            except TypeError:
                return "wrong"

@app.route('/registration')
def registration_page():
    return render_template('registration.html')

@app.route('/registration', methods = ["POST", "GET"])
def register():
    if request.method == "POST":
        new_data = {request.form['username']: {"name": request.form['name'], "email": request.form['email'],
                                           "password": enc(request.form['password'])}}
        with open("static/data.json", "r") as datafile:
            try:
                data = json.load(datafile)
                data.update(new_data)
            except json.JSONDecodeError:
                data = {}
        with open("static/data.json", "w") as datafile:
            json.dump(data, datafile, indent=4)
        return render_template('login.html')




if __name__ == "__main__":
    app.run(debug=True)