from flask import render_template,request,redirect,url_for,abort
from app.models.user import User
from app.models.blog import Blog
from .forms import BlogForm,CommentForm
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
            new_blog = Blog(author = blog_form.author.data,title = blog_form.title.data,blog_write = blog_form.blog.data,user = current_user)
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
            new_blog = Blog(author = blog_form.author.data,title = blog_form.title.data,blog_content = blog_form.blog.data,user = current_user)
            db.session.add(new_blog)
            db.session.commit()
            return redirect(url_for('main.blogs'))


    title = 'Dusk - Blog posts'

    return render_template('blog.html',blog_form = blog_form , blogs = blogs , title = title)

@main.route('/blogs/details/<int:id>', methods=['GET', 'POST'])
@login_required
def details(id):
    '''
    View a full blog article and see the user and author that wrote it
    '''
    # add the edit functionality

    one_blog = Blog.query.filter_by(id = id).first()

    one_com = Comment.query.filter_by(blog_id = id).all()

    com_form = CommentForm()

    if com_form.validate_on_submit():
        comment = Comment(com_write = com_form.comment.data,blog_id = one_blog.id, user = current_user.get_id())
        comment.save_comment()

        return redirect(url_for('main.details', id = one_blog.id))
    
    return render_template('blog-detail.html', com_form = com_form, one_blog = one_blog, one_com = one_com)


@main.route('/blogs/<int:id>', methods=['GET', 'POST'])
def delete_blog(id):
    '''
    Delete a blog
    '''
    the_blog = Blog.query.filter_by(id = id).first()

    db.session.delete(the_blog)
    db.session.commit()
    return redirect(url_for('main.blogs'))

@main.route('/blogs/delete/comment')
def delete_comment(id):
    '''
    Delete a comment
    '''
    one_com = Comment.query.filter_by(blog_id = id).first()
    db.session.delete(one_com)
    db.session.commit()

    return redirect(url_for('main.details',id = id))

