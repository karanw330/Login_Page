from json import JSONDecodeError
from flask import Flask, render_template, request, jsonify
import json

from sqlalchemy.exc import IntegrityError

from encryptor import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float



class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user_data.db"
db.init_app(app)

class Auth(db.Model):
    username: Mapped[str] = mapped_column(String(15), nullable=False, unique=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(25), nullable=False)
    email: Mapped[str] = mapped_column(String(25), unique=True ,nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)

@app.route('/')
def first():
    return render_template("login.html")

@app.route('/authentication', methods=["POST", "GET"])
def check():
    if request.method == "POST":
        try:
            result = db.session.execute(db.select(Auth).where(Auth.username == request.form["username"]))
            record = result.scalars().all()
            '''if record[0].password == enc(request.form["password"]):
                return "landing page"
            else:
                return "no"
        except IndexError:
            return "dne"'''
            if record[0].password == enc(request.form["password"]):
                return jsonify({"confirmation": "OK"})
            else:
                return jsonify({"confirmation": "NO"})
        except IndexError:
            return jsonify({"confirmation": "DNE"})

@app.route('/registration')
def registration_page():
    return render_template('registration.html')

@app.route('/registration', methods = ["POST", "GET"])
def register():
    if request.method == "POST":
        try:
            new_user = Auth(name=request.form["name"], username=request.form["username"], email=request.form["email"], password=enc(request.form["password"]))
            db.session.add(new_user)
            db.session.commit()
        except IntegrityError:
            pass
        return render_template('login.html')

@app.route('/Dashboard')
def landing_page():
    return "landing page"



if __name__ == "__main__":
    app.run(debug=True)