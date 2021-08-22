from app.email import mail_message
from app.services import get_quote
from flask import render_template,request,redirect,url_for,abort
from app.models.user import User
from app.models.blog import Blog
from .forms import BlogForm,CommentForm,UpdateProfile,SubscriptionForm
from app.models.comment import Comment
from app.models.subscriber import Subscribe
from app import db,photos
from . import main
from flask_login import login_required,current_user
import markdown2 

@main.route('/', methods=['GET', 'POST'])
def landing():
    '''
    landig/welcoming page
    '''

    title = 'Dusk-App'
    return render_template('landing.html', title=title)

@main.route('/home', methods=['GET', 'POST'])
def home():
    '''
    User landing page/Welcome page
    '''
    quotes = get_quote()

    # first_blog = Blog.sort(reverse=True).all()

    blogs = Blog.query.all()

    blog_form = BlogForm()

    if blog_form.validate_on_submit():
            new_blog = Blog(author = blog_form.author.data,title = blog_form.title.data,blog_write = blog_form.blog.data,user = current_user)
            db.session.add(new_blog)
            db.session.commit()
            return redirect(url_for('main.landing'))

    title = "Dusk"
    return render_template('index.html',title = title, blog_form = blog_form, quotes = quotes,blogs = blogs)

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
    
    return render_template('blog-detail.html', com_form = com_form, one_blog = one_blog, one_com = one_com,user = current_user)


@main.route('/blogs/<int:id>', methods=['GET', 'POST'])
def delete_blog(id):
    '''
    Delete a blog
    '''
    the_blog = Blog.query.filter_by(id = id).first()

    db.session.delete(the_blog)
    db.session.commit()
    return redirect(url_for('main.blogs'))

@main.route('/blogs/comment/<int:id>')
def delete_comment(id):
    '''
    Delete a comment
    '''
    one_com = Comment.query.filter_by(id = id).first()
    db.session.delete(one_com)
    db.session.commit()

    return redirect(url_for('main.details', id = one_com.blog_id))

@main.route('/create-blog',methods=['GET', 'POST'])
@login_required
def create_blog():
    '''
    create blog
    '''
    blog_form = BlogForm()

    if blog_form.validate_on_submit():
            new_blog = Blog(author = blog_form.author.data,title = blog_form.title.data,blog_write = blog_form.blog.data,user = current_user)
            db.session.add(new_blog)
            db.session.commit()

            subscribers = Subscribe.query.all()

            for subscriber in subscribers:
                mail_message('New Blog Posted','email/postAlert/post_alert',subscriber.subscriber, blog = new_blog)


            return redirect(url_for('main.blogs'))

    sub_form = SubscriptionForm()

    if sub_form.validate_on_submit():
        new_subscriber = Subscribe(subscriber = sub_form.email.data)
        db.session.add(new_subscriber)
        db.session.commit()

        mail_message('Welcome to the Dusk Family','email/subscribe/new_subscribe',new_subscriber.subscriber,subscriber = new_subscriber)


    return render_template('create-blog.html', blog_form = blog_form,sub_form=sub_form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    blogs = Blog.query.filter_by(user = current_user).all()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,blogs = blogs)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))
    title = f'{current_user.username}'
    return render_template('profile/update.html',form =form, title=title)

@main.route('/user/<uname>/update/pic',methods= ['GET','POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()

    if request.method == 'POST':
        if request.files:
            if 'photo' in request.files:
                    filename = photos.save(request.files['photo'])
                    path = f'photos/{filename}'
                    user.profile_pic_path = path
                    print(user.profile_pic_path)
                    db.session.add(user)
                    db.session.commit()
                    
    return redirect(url_for('main.profile',uname=uname))



