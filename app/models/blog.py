from app import db
from datetime import datetime


class Blog(db.Model):

    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    title = db.Column(db.String(50))
    author = db.Column(db.String(50))
    blog_write = db.Column(db.String())
    date = db.Column(db.DateTime,default=datetime.now())
    comments = db.relationship('Comment', backref='blog',lazy="dynamic")

    def save_blog(self):
        db.session.add(self)
        db.session.commit()
    
    