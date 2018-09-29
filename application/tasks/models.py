from application import db
from application.models import Base

class Task(Base):
    __tablename__ = 'task'
    name = db.Column(db.String(144), nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.done = False

    def get_id(self):
      return self.id
