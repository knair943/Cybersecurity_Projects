# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 10:58:03 2024

@author: knair
"""

import hashlib as hs
import getpass as gp

password_manager = {}

def create_account():
    username = input("Enter a username: ")
    password = gp.getpass("Enter a password: ")
    hashed_password = hs.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("Account created successfully!")
    
def login():
    username = input("Enter your username: ")
    password = gp.getpass("Enter your password: ")
    hashed_password = hs.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login successful!")
    else:
        print("invalid username or password.")
        
def main():
    while True:
        choice = input("Enter 1 to create an account, 2 to login, or 0 to exit: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "0":
            break
        else:
            print("Invalid choice")
        
if __name__ == "__main__":
    main()
    