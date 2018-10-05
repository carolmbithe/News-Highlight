import unittest
from models import newssource
Newssource = newssource.Newssource


class NewssourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Newssource class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_newssource = Newssource('Tuko news')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_newssource,Newssource))


if __name__ == '__main__':
    unittest.main()
