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
    password = input()
    save_users(create_user(user,password)
    print(f"Welcome {user} you have created an account with us, please enjoy")

    while True:
        print("use this short code:cc-to create an account, dc-to display user_accounts, fc -to find user credentials") 
        short_code = input().lower()

        if short_code == 'cc':
        print("New Account")
        print("-"*25)
        print ("user_name ....")
        User_name = input()

        print("password ..."
        password = input()
        save_users(create_user("User_name,password")) # create and save new user Account.

        elif short_code == 'dc':
        if display_users():
                            

  if __name__ == "__main__":
    main()