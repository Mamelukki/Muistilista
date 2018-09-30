from application import db
from application.models import Base

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

