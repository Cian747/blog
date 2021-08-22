from app import db
import unittest
from app.models.user import User
from app.models.comment import Comment

class TestComment(unittest.TestCase):
    '''
    testing the comment class 
    '''

    def setUp(self):
        '''
        Set up the user and comment objects
        '''
        self.new_user = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_comment = Comment(id = 1,user = 2,blog_id = 15,posted = '1660-08-09',com_write='great work')

    def tearDown(self):
        '''
        for clearing the database every
        '''
        Comment.query.delete()

    def test_instance_variables(self):
        '''
        check if the data matches from the new object.
        '''
        self.assertEquals(self.new_comment.id,1)
        self.assertEquals(self.new_comment.user,2)
        self.assertEquals(self.new_comment.blog_id,15)
        self.assertEquals(self.new_comment.posted,'1660-08-09')
        self.assertEquals(self.new_comment.com_write,'great work')

    def test_instance(self):
        '''
        Assert that the object
        '''
        self.assertTrue(self.new_comment,Comment)

    
