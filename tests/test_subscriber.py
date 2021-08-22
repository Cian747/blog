from app import db
import unittest
from app.models.user import User
from app.models.subscriber import Subscribe

class TestSubscribe(unittest.TestCase):
    '''
    test Subscribe class
    '''

    def setUp(self):
        '''
        Set up the class
        '''
        self.new_user = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_subscriber = Subscribe(id = 1,subscriber = 'jr@gmail.com')

    def tearDown(self):
        '''
        clear the database before  
        '''
        Subscribe.query.delete()
    
    def test_instance(self):
        '''
        check the object matching the class 
        '''
        self.assertTrue(self.new_subscriber,Subscribe)

    def test_instance_variables(self):
        '''
        check the variable match
        '''
        self.assertEquals(self.new_subscriber.id,1)
        self.assertEquals(self.new_subscriber.subscriber,'jr@gmail.com')

    def test_save_subscribe(self):
        '''
        check if a subscriber is saved
        '''
        self.new_subscriber.save_subscriber()
        self.assertTrue(len(Subscribe.query.all())>0)
