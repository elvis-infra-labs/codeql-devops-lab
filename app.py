from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

@app.route("/user")
def get_user():
    # SOURCE: Untrusted user input from an HTTP query parameter (?username=...)
    username = request.args.get("username")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # SINK: Untrusted data concatenated directly into SQL execution without sanitization
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    return f"Query executed: {query}"

@app.route("/ping")
def ping():
    # NEW VULNERABILITY: Command Injection (CWE-78)
    host = request.args.get("host")
    os.system("ping -c 1 " + host)
    return f"Pinged {host}"

if __name__ == "__main__":
    app.run(port=5000)
