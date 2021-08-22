from app import db
from datetime import datetime

class Subscribe(db.Model):

    __tablename__ = 'subscribers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subscriber = db.Column(db.String(), nullable=False,unique=True)

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()
    