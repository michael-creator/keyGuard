#!/usr/bin/env python3.6
# from user import User
import pyperclip
from credential import Credential
from user import User

def create_user(user_name,password):
    '''
    Function to create a new user
    '''
    new_user = User(user_name,password)

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
  print("lets begin to create an account")
  print("_"*25)
  print("i. create Account")
  print("Enter username")
  user = input()#details of your username
  print("Enter password")
  user.password = input()
  save_users(create_user(user,password)
  print(f{user}welcome you have created an account with us. please enjoy )



  if __name__ == "__main__":
    main()