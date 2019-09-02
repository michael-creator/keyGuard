import pyperclip 

class User:

    """
    class that generates new instances of Users.
    """
    pass


    User_list = []
    def __init__(self, first_name, last_name, full_name, phone_number, email):
        
        self.first_name = first_name,"mickey"
        self.last_name = last_name,"karije"
        self.full_name = full_name,"mickey_karije"
        self.phone_number = phone_number,"0712345678"
        self.email = "mikelkarije@gmail.com"
        
    def test_save_User(self):
        '''
        test_saves a User test case if the User objet is saved into User list
        '''
        User.User_list.append(self)


    def delete_user(self):

        User.user_list.remove(self)

    @classmethod
    def find_by_name(cls,name):


        for user in cls.User_list:
            if user.full_name == name:
                return 
    @classmethod       
    def user_exist(cls,name):
        for user in class.user_list:
            if user.full_name == name:
                return user