import pyperclip 
from user import User
from credential import Credential

class user:
    """
    class that generates new instances of Users.
    """
    user_list = []
    def __init__(self, first_name, last_name, phone_number, email):
        
        self.first_name = first_name,"mickey"
        self.last_name = last_name,"karije"
        self.phone_number = phone_number,"0712345678"
        self.email = "mikelkarije@gmail.com"
        
    def save_user(self):
        '''
        test_saves a User test case if the User objet is saved into User list
        '''
        User.user_list.append(self)


    def delete_user(self):

        User.user_list.remove(self)

  