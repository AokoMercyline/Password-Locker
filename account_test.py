import unittest#Importing the unittest module
import pyperclip
from account import Account  #Importing the contact class

class TestContact(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
        # Items up here .......
        def setUp(self):
    '''
    Set up method to run before each test cases.
    '''
    self.new_contact = Contact("Aoko","Mercyline","0712345678","aokomercyline@,mercy1234") # create contact object


def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_contact.first_name,"Aoko")
    self.assertEqual(self.new_contact.last_name,"Mercyline")
    self.assertEqual(self.new_contact.phone_number,"0712345678")
    self.assertEqual(self.new_contact.email,"aokomerycline@")
    self.assertEqual(self.new_contact.password,"mercy1234")


if __name__ == '__main__':
    # unittest.main()
   