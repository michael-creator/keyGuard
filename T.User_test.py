import unittest # Importing the unittest module
# from person import Person # Importing the User class

class TestPerson(unittest.TestCase):

    '''
    Test class that defines test cases for the User class behaviours.

    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_contact =self("James","Muriuki","0712345678","james@ms.com") # create person object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_contact.first_name,"mickey")
        self.assertEqual(self.new_contact.last_name,"karije")
        self.assertEqual(self.new_contact.phone_number,"0712345678")
        self.assertEqual(self.new_contact.email,"mikelkarije@gmail.com")

import unittest # Importing the unittest module
# from person import Person # Importing the User class

class TestPerson(unittest.TestCase):

    '''
    Test class that defines test cases for the User class behaviours.

    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_contact =self("James","Muriuki","0712345678","james@ms.com") # create person object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_contact.first_name,"mickey")
        self.assertEqual(self.new_contact.last_name,"karije")
        self.assertEqual(self.new_contact.phone_number,"0712345678")
        self.assertEqual(self.new_contact.email,"mikelkarije@gmail.com")

   def test_save_Person(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_contact.save_contact() # saving the new contact
        self.assertEqual(len(Pmerson.Person_list),1)

if __name__ ==  '__main__':
    unittest.main()