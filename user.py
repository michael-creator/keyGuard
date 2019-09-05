import pyperclip 
from user import User
from credential import Credential

class user:
    """
    class that generates new instances of Users.
    """
    user_list = []
    def __init__(self,user_name, password):
        
        self.user_name = user_name,"mickey"
        self.password = password,"hvvty565rp"
        
    def save_user(self):
        '''
        test_saves a User test case if the User objet is saved into User list
        '''
        User.user_list.append(self)


    def delete_user(self):

        User.user_list.remove(self)

  