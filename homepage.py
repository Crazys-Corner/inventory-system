from util.session import getSession, setSession
import os
from account import login, register
def homepage():
    os.system('cls' if os.name == 'nt' else 'clear')
    if getSession('username') is None:
        print("""
        Welcome to the homepage 
        1. Login
        2. Register
        """)
        answer = input("Your Choice: ")
        if answer == '1':
            login.loginPage()
        elif answer == '2':
            register.registerPage()
        else:
            print('Invalid Choice')
            homepage()
    else: 
        print(f"""
        Welcome to the homepage - Logged in as {getSession('username')}
        1. Logout
        2. Show all users
        3. Inventory
        """)
        answer = input("Your Choice: ")
        if answer == '2':
            login.loginPage()
        elif answer == '3':
            register.registerPage()
        elif answer == '1':
            setSession('username', None)
            homepage()
        else:
            print('Invalid Choice')
            homepage()