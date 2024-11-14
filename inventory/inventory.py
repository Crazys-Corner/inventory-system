from util.session import getSession, setSession
import homepage
import os
from account import login, register
def inventory():
    os.system('cls' if os.name == 'nt' else 'clear')
    if getSession('username') is None:
        homepage.homepage()
    else: 
        print(f"""
        Welcome to the Inventory - Logged in as {getSession('username')}
        1. Add to inventory
        2. See all inventory
        3. Back to Home
        """)
        answer = input("Your Choice: ")
        if answer == '1':
            login.loginPage()
        elif answer == '2':
            register.registerPage()
        elif answer == '3':
            homepage.homepage()
        else:
            print('Invalid Choice')
            homepage()