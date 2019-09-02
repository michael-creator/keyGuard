import pyperclip 

class User:

    """
    class that generates new instances of Users.
    """
    pass


    User_list = []
    def __init__(self, first_name, last_name, phone_number, email):
        
        self.first_name = first_name,"mickey"
        self.last_name = last_name,"karije"
        self.phone_number = phone_number,"0712345678"
        self.email = "mikelkarije@gmail.com"
        
    def test_save_User(self):
        '''
        test_saves a User test case if the User objet is saved into User list
        '''
        User.User_list.append(self)