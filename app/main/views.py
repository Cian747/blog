from flask import render_template,request,redirect,url_for,abort
from app.models.user import User
from app.models.blog import Blog
from app.models.comment import Comment
from app import db,photos
from . import main
from flask_login import login_required,current_user
import markdown2 

@main.route('/')
def landing():
    '''
    landig/welcoming page
    '''
    title = 'Dusk-App'
    return render_template('index.html', title=title)
