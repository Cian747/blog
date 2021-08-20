from flask import render_template,request,redirect,url_for,abort
from app.models.user import User
from app.models.blog import Blog
from .forms import BlogForm
from app.models.comment import Comment
from app import db,photos
from . import main
from flask_login import login_required,current_user
import markdown2 

@main.route('/', methods=['GET', 'POST'])
def landing():
    '''
    landig/welcoming page
    '''

    blogs = Blog.query.all()

    blog_form = BlogForm()

    if blog_form.validate_on_submit():
            new_blog = Blog(author = blog_form.author.data,title = blog_form.title.data,blog_write = blog_form.blog.data)
            db.session.add(new_blog)
            db.session.commit()
            return redirect(url_for('main.landing'))

    title = 'Dusk-App'
    return render_template('index.html', title=title,blogs=blogs,blog_form=blog_form)

@main.route('/home', methods=['GET', 'POST'])
def home():
    '''
    User landing page/Welcome page
    '''

    title = "Dusk"
    return render_template('index.html',title = title)

@main.route('/blogs/', methods=['GET', 'POST'])
def blogs():
    '''
    Query for all the blogs
    '''
    blogs = Blog.query.all()

    blog_form = BlogForm()

    if blog_form.validate_on_submit():
            new_blog = Blog(author = blog_form.author.data,title = blog_form.title.data,blog_content = blog_form.blog.data)
            db.session.add(new_blog)
            db.session.commit()
            return redirect(url_for('main.blogs'))


    title = 'Dusk - Blog posts'

    return render_template('blog.html',blog_form = blog_form , blogs = blogs , title = title)