import os

from sqlalchemy import Column, ForeignKey, String
from flask_sqlalchemy import SQLAlchemy
from app import app
from flask_login import UserMixin

db = SQLAlchemy(app)

def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["POSTURI"]
    db.app = app
    db.init_app(app)

connect_to_db(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["POSTURI"]
# print (app.config['SQLALCHEMY_DATABASE_URI'])



class Users(db.Model,UserMixin):

    __tablename__ = "users"
    id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    username = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)
    engine_type = db.Column(db.String(64), nullable=True)
    home_airport = db.Column(db.String(64), nullable=True)

    def __repr__(self):
        return f"<Users user_id={self.id} username={self.username}>"



class Trip_planner(db.Model):

    trip_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id')
                        )
    date = db.Column(db.String, nullable=True)
    refuel = db.Column(db.String, nullable=True)
    hours = db.Column(db.Integer, nullable=True)
    miles = db.Column(db.Integer, nullable=True)
    startpoint = db.Column(db.String, nullable=True)
    endpoint = db.Column(db.String, nullable=True)
    def __repr__(self):
        return f"<Users id={self.miles}>"



class Flight_log(db.Model):

    flight_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id')
                        )
    date = db.Column(db.String, nullable=True)
    flight_hours = db.Column(db.Integer, nullable=True)
    flight_miles = db.Column(db.Integer, nullable=True)
    startpoint = db.Column(db.String, nullable=True)
    endpoint = db.Column(db.String, nullable=True)
    enginetype = db.Column(db.String, nullable=True)
    def __repr__(self):
        return f"<Users id={self.flight_miles} trip_id={self.flight_id}>"


if __name__ == "__main__":
    connect_to_db(app)
    print("Connected to Avcomptool database.")