from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
SECRET_KEY = "mysecretkey123"
DB_PASSWORD = "admin123"

def get_db():
    conn = sqlite3.connect("app.db")
    return conn

@app.route("/users", methods=["GET"])
def get_users():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return jsonify(users)

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO users (name, email) VALUES ('" + data["name"] + "', '" + data["email"] + "')"
    cursor.execute(query)
    db.commit()
    return jsonify({"status": "ok"})

@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM users WHERE id = " + id)
    db.commit()
    return jsonify({"status": "deleted"})

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    if data["password"] == DB_PASSWORD:
        return jsonify({"token": SECRET_KEY})
    return jsonify({"error": "bad password"})

if __name__ == "__main__":
    app.run(debug=True)
