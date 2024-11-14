import os
import sqlite3
from util.hash import verify_password 
import homepage
from util.session import setSession
import time

def login(username, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    
    if user and verify_password(user[0], password):
        setSession('username', username)

        return True
    else:
        print("Login failed")
        time.sleep(2)
        homepage.homepage()
        return False

def loginPage():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Login Page')
    username = input('Username: ')
    password = input('Password: ')
    
    # Call login function with user inputs
    if login(username, password):
        print("Welcome!")
        print("Login successful")
        time.sleep(2)
        homepage.homepage()
        return True
    else:
        print("Incorrect username or password.")
        time.sleep(2)
        homepage.homepage()
        return False
