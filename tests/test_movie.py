import unittest
from app.model import movie

class MovieTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before evry Test
        '''
        self.new_movie = movie(1234,'Python must be crazy','A thrilling new Python Series','/khsjha27hbs',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,movie))    