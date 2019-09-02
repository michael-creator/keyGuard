import unittest # Importing the unittest module
# from user import user # Importing the User class
class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the User class behaviours.

    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_contact =self("Mickey","karije","0712345678","mikelkarije@gmail.com","mickey_karije") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_contact.first_name,"mickey")
        self.assertEqual(self.new_contact.last_name,"karije")
        self.assertEqual(self.new_contact.full_name,"mickey karije")
        self.assertEqual(self.new_contact.phone_number,"0712345678")
        self.assertEqual(self.new_contact.email,"mikelkarije@gmail.com")
        

    def test_save_contact(self):
        
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_contact.save_User() # saving the new user
        self.assertEqual(len(self),1)

   def test_delete_user(self):

                    '''

    test_delete_user to test if we can remove a user from our user list

                '''

        self.new_user.save_user()
                test_user = User("Test","users","mickey","mikelkarije@.com") 

                     test_user.save_user()
                    self.new_user.delete_user()
                        self.assertEqual(len(User.user_list),1)







if __name__ ==  '__main__':
    unittest.main()