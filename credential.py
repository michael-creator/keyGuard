import string
import pyperclip
from random import choice

class credential:
    Credential_list = []

    def __init__(self, account,account_name, account_number,account_password)


    self.account = account
    self.account_name = name
    self.account_number = number
    self.account_password =account_password

    def save_credential(self):
                 '''
        save_credential method saves credentials objects into credential_list
        '''
 credential.Credential_list.append(self)
 