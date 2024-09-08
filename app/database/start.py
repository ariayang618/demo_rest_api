import sqlite3


async def create_db():
    conn = sqlite3.connect('api_demo.db')

    # Create a cursor object to interact with the database
    cursor = conn.cursor()
    with open('database/main.sql', 'r') as sql_file:
        sql_script = sql_file.read()
    # SQL query to create a schema (table)
    cursor.executescript(sql_script)

    conn.commit()
    conn.close()
    print('database is ready')
