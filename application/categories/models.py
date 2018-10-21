from application import db
from application.models import Base
from sqlalchemy.sql import text

class Category(Base):
    __tablename__ = "category"

    name = db.Column(db.String(144), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
nullable=False)

    def __init__(self, name):
        self.name = name

    @staticmethod
    def all_by_id(ids):
        ret = []
        for c in db.session().query(Category).filter(Category.id.in_(ids)):
            print(c)
            ret.append(c)
        return ret

    @staticmethod
    def tasks_of_a_category(help_id):
        stmt = text('SELECT task.name FROM task, category, tasks_and_categories'
        ' WHERE tasks_and_categories.category_id = ' + str(help_id) +
        ' AND tasks_and_categories.category_id = category.id'
        ' AND tasks_and_categories.task_id = task.id'
        ' ORDER BY task.name ASC')

        res = db.engine.execute(stmt)
        tasks = []
        for row in res:
            tasks.append(row[0])
        return tasks
