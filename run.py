#!/usr/bin/env python3.6
# from user import User
from credential import Credential

def create_user(fname,lname,phone,email):
    '''
    Function to create a new user
    '''
    User =(fname,lname,phone,email)
    return User

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
 