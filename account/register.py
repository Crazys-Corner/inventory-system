import homepage
import time
def registerAccount(username, password, email):
    import sqlite3
    from util.hash import hash_password
    newpass = hash_password(password)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, newpass))
    conn.commit()
    conn.close()
    return True

def registerPage():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Register Page')
    username = input('Username: ')
    email = input('Email: ')
    password = input('Password: ')
    if (registerAccount(username, password, email) is True): 
        print("Account created successfully! Redirecting shortly...")
        time.sleep(2)
        homepage.homepage()
    else:
        print('Account not created, please retry')
        return False
    