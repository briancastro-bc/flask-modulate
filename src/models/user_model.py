#from flask_sqlalchemy.model import Model
from src.database import db
#from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(350), nullable=False)
    fullname = db.Column(db.String(80), nullable=False)
    tasks = relationship('Task', backref='user', lazy=True)
    
    def __init__(self, username=None, password=None, fullname=None) -> None:
        self.username = username
        self.password = password
        self.fullname = fullname