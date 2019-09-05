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
    print("press (a)login into an account, or (b) exit the program")
        option = input()
        if option == "a":
          print("_"*25)
          print("username:")
            inputed_username = input()
            print("Password:")
            inputedpassword = input()
if inputpassword == userpassword and input_username == user:
                print(f"welcome {user} Welcome to your password portal")
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
          if display_credentials():
           print("Here is a list of your credentials")
          print('\n')
          for credential in display_credentials():
          print(f"Site:{credential.site}\n UserName:{credential.user_name}\n Password:{credential.account_password}")
          print('\n')
          else:
          print('\n')
          print(" sorry credentials not found")
          print('\n')
          elif code == "dc":
          print("Are you sure you want to delete this credentials y for Yes or n for No?.they will be deleted permanently!")
              answer = input()
              if answer == "y":                         
          elif short_code == "ex":
            print("Bye .......")
            break
            else:
                print("I really didn't get that. Please use the short codes")
  if __name__ == "__main__":
    main()