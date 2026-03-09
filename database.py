import mariadb
import sys

from requests import get

def get_connection():
    try:
        conn = mariadb.connect(
            user = "pythonuser",
            password = "pythonpass",
            host = "127.0.0.1",
            port = 3306,
            database = "fullstack"
        )
        return conn
    
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform")
        sys.exit(1)

def database(string):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(string)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def get_password(login):
    results = database(f"SELECT password FROM users WHERE username = '{login}'")
    print(results)

def insert_database(user, hashed_pass, privigeges):
    pass

get_password("Mathias")