from app import create_app,db
from flask_script import Manager,Server
from app.models.user import User
from app.models.blog import Blog
from app.models.comment import Comment
from app.models.subscriber import Subscribe
from  flask_migrate import Migrate, MigrateCommand

# Creating app instance
app = create_app('production')

@app.before_first_request
def create_tables():
    db.create_all()

manager = Manager(app)

manager.add_command('server',Server)

@manager.command
def test():
    """
    Run the unit tests.
    """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Comment = Comment, Blog = Blog,Subscribe = Subscribe)


if __name__ == '__main__':
    manager.run()
