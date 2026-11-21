from flask import Flask, request
import sqlite3

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

if __name__ == "__main__":
    app.run(port=5000)
