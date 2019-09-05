#!/usr/bin/env python3.6
# from user import User
import pyperclip
from credential import Credential
from user import User

def create_user(fname,lname,phone,email):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,phone,email)

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()


  
def main():

  print("Hello welcome to password locker")

  if __name__ == "__main__":
    main()