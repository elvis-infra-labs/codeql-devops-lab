import sqlite3

def get_user_data(username):
    # Connect to a dummy database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # VULNERABILITY (SQL Injection):
    # Raw user input is formatted directly into the SQL query string
    # without parameterized queries or sanitization.
    query = f"SELECT * FROM users WHERE username = '{username}'"
    
    print(f"Executing: {query}")
    cursor.execute(query)
    return cursor.fetchall()

if __name__ == "__main__":
    # Simulate untrusted user input
    user_input = "admin' OR '1'='1"
    get_user_data(user_input)
