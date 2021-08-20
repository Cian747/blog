from app import db
from datetime import datetime



class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    user = db.Column(db.Integer,db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    com_write = db.Column(db.String(255))  

    def save_comment(self):
        db.session.add(self)
        db.session.commit()  

    def __repr__(self):
        return f'User {self.name}'