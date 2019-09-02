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

def find_user(number):
      '''
    Function that finds a user by number and returns the user
    '''
  return User.find_by_number(number)

def check_existing_users(number):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return User.User_exist(number)
 