from application import db
from application.models import Base
from sqlalchemy.sql import text
from application.categories.models import Category

tasks_and_categories = db.Table('tasks_and_categories',
    db.Column('task_id', db.Integer, db.ForeignKey('task.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)

class Task(Base):
    __tablename__ = 'task'
    name = db.Column(db.String(144), nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    tasks_and_categories = db.relationship('Category', secondary=tasks_and_categories, lazy='subquery',
backref=db.backref('Task', lazy=True))

    def __init__(self, name, priority, tasks_and_categories):
        self.name = name
        self.priority = priority
        self.done = False
        self.tasks_and_categories = tasks_and_categories

    def get_id(self):
      return self.id

    @staticmethod
    def categories_of_a_task(help_id):

        string = ()
        stmt = text('SELECT category.name FROM task, category, tasks_and_categories'
        ' WHERE tasks_and_categories.task_id = ' + str(help_id) +
        ' AND tasks_and_categories.category_id = category.id'
        ' AND tasks_and_categories.task_id = task.id')

        res = db.engine.execute(stmt)
        categories = []
        for row in res:
            categories.append(row[0])
        return categories
