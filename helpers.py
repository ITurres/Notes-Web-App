from cs50 import SQL
from flask import redirect, session
from functools import wraps

db = SQL("sqlite:///notes.db")


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


def check_username(username):
    user_name = db.execute(
        "SELECT username FROM users WHERE username = ?", username)
    if user_name:
        return True
    return False
