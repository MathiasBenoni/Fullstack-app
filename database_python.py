import mariadb
import sys

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
def database(query, params=None):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    if query.strip().upper().startswith("SELECT"):
        results = cur.fetchall()
    else:
        conn.commit()
        results = None
    cur.close()
    conn.close()
    return results

def get_password(login):
    result = database("SELECT password FROM users WHERE username = %s", (login,))


def insert_user_database(user, hashed_pass, privileges):
    database("INSERT INTO users (username, password, privileges) VALUES (%s, %s, %s)", (user, hashed_pass, privileges))

def insert_choaching_database(username, date):
    database("INSERT INTO coaching (username, date) VALUES (%s, %s)", (username, date))
    pass