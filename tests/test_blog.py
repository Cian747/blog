from app import db
import unittest
from app.models.user import User
from app.models.blog import Blog


class TestBlog(unittest.TestCase):
    '''
    Testing the blog class
    '''

    def setUp(self):
        '''
        creating an object
        '''
        self.new_user = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.blog = Blog(id = 15,user_id = 1,title='sports',author = 'cyan',blog_write='I am great',date ='1990-08-09')

    def tearDown(self):
        '''
        Refresh  the db
        '''
        Blog.query.delete()

    def test_instance(self):
        '''
        test object and class
        ''' 
        self.assertTrue(self.blog,Blog)

    def test_instance_variables(self):
        '''
        Assert that details in the set up match
        '''
        self.assertEquals(self.blog.id,15)
        self.assertEquals(self.blog.user_id,1)
        self.assertEquals(self.blog.title,'sports')
        self.assertEquals(self.blog.author,'cyan')
        self.assertEquals(self.blog.blog_write,'I am great')
        self.assertEquals(self.blog.date,'1990-08-09')

    def test_save_blog(self):
        '''
        Check if blog is saved
        '''
        self.blog.save_blog()
        self.assertTrue(len(Blog.query.all())>0)

