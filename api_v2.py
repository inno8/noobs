"""Improved user API - fixing security issues from api.py"""
import os
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Fixed: use environment variables instead of hardcoded secrets
SECRET_KEY = os.environ.get("SECRET_KEY", "change-me-in-production")
DB_PATH = os.environ.get("DB_PATH", "app.db")


def get_db():
    """Get database connection with row factory."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/users", methods=["GET"])
def get_users():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, name, email FROM users")
    users = [dict(row) for row in cursor.fetchall()]
    db.close()
    return jsonify(users)


@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    if not data or not data.get("name") or not data.get("email"):
        return jsonify({"error": "name and email are required"}), 400

    db = get_db()
    cursor = db.cursor()
    # Fixed: use parameterized queries instead of string concatenation
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        (data["name"], data["email"])
    )
    db.commit()
    db.close()
    return jsonify({"status": "created", "id": cursor.lastrowid}), 201


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    db = get_db()
    cursor = db.cursor()
    # Fixed: use parameterized query and proper type
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    db.commit()
    deleted = cursor.rowcount > 0
    db.close()
    if not deleted:
        return jsonify({"error": "user not found"}), 404
    return jsonify({"status": "deleted"})


if __name__ == "__main__":
    debug_mode = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=debug_mode)
