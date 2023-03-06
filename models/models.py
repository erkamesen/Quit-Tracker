from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import time 

db = SQLAlchemy()


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    smoked_cigarettes_per_day = db.Column(db.Integer, nullable=False)
    cigarettes_in_pack = db.Column(db.Integer, nullable=False)
    years_of_smoking = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)
    price = db.Column(db.String, nullable=False)
    currency = db.Column(db.String, nullable=False)

    
