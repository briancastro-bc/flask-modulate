from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import ForeignKey
from src.database import db
from sqlalchemy import Column, Integer, String

class Task(db.Model):
    __tablename__ = 'Tasks'
    id = Column(Integer(), primary_key=True)
    title = Column(String(40), nullable=False)
    description = Column(String(300), nullable=False)
    user_owner = Column(Integer(), ForeignKey('Users.id'), nullable=False)
    
    def __init__(self, title=None, description=None, user_owner=None) -> None:
        self.title = title
        self.description = description
        self.user_owner = user_owner