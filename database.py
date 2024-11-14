def init():
    import sqlite3
    print('Initializing Database')

    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,   
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
    );
    """

    create_inventory_table = """
    CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    amount INTEGER NOT NULL,
    price REAL NOT NULL
    );
    """

    conn.execute(create_users_table)
    print('Table users created')
    conn.execute(create_inventory_table)
    print('Table inventory created')
