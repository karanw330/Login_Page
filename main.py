from json import JSONDecodeError
from flask import Flask, render_template, request
import json
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
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(25), nullable=False)
    username: Mapped[str] = mapped_column(String(15), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(25), unique=True ,nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)

'''with app.app_context():
    new_user = Auth(id=1, name="Karan", username="karanw" , email="karan@lolu.com", password="!!!!!!!!")
    db.session.add(new_user)
    db.session.commit()'''

@app.route('/')
def first():
    return render_template("login.html")

@app.route('/authentication', methods=["POST", "GET"])
def check():
    if request.method == "POST":
        '''try:
            with open("static/data.json", "r") as datafile:
                data=json.load(datafile)

            if data[request.form["username"]]["password"] == enc(request.form["password"]):
                return "lessgo"
            else:
                return "wrong"
        except KeyError:
            return "wrong"
        except TypeError:
            return "wrong"
        except JSONDecodeError:
            return "wrong"'''
        try:
            with app.app_context():
                result = db.session.execute(db.select(Auth).where(Auth.username == request.form["username"]))
                record = result.scalars().all()
                if record[0].password == enc(request.form["password"]):
                    return "lessgooo"
                else:
                    return "wrong"
        except IndexError:
            return "user not found. Please register."

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
                with open("static/data.json", "w") as file:
                    json.dump(data, file, indent=4)
        with open("static/data.json", "w") as datafile:
            json.dump(data, datafile, indent=4)
        return render_template('login.html')




if __name__ == "__main__":
    app.run(debug=True)