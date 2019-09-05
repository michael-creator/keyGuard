import string
import pyperclip
from user import User
from random import choice


class Credential:
    credential_list = []

    def __init__(self, account, account_name, account_email,account_password):

        self.account = account
        self.account_name = account_name
        self.account_email = account_email
        self.account_password = account_password

    def save_credential(self):
        '''
        save_credential method saves credentials objects into credential_list
        '''
        Credential.credential_list.append(self)
    @classmethod
    def generate_password(cls):
        '''
        Method that generates a random alphanumeric password
        '''

        size = 4

        alphanum = string.ascii_uppercase + string.digits + string.ascii_lowercase

        password = ''.join(choice(alphanum) for num in range(size))

        return password
    @classmethod
    def display_credentials(cls):
        '''
        This function displays credentials after saving
        '''
        for credential in cls.credential_list:
             return credential
def find_user(number):
    '''
    Function that finds a user by number and returns the user
    '''
    return User.find_by_number(number)

def check_existing_user(number):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return User.user_exist(number)
def display_users():
    '''
    Function that returns all the saved Users
    '''
    return User.display_users()
