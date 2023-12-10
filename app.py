import helpers

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///notes.db")


@app.route("/")
@helpers.login_required
def index():
    current_user_id = session["user_id"]

    user_notes = db.execute("""SELECT *
                             FROM user_notes
                              WHERE user_id = ?""",
                            current_user_id)

    return render_template("index.html", user_notes=user_notes)


@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username:
            return render_template("login.html",
                                   password=password,
                                   username_failure="please provide an username")
        elif not password:
            return render_template("login.html",
                                   username=username,
                                   password_failure="please provide a password")

        users = db.execute(
            "SELECT * FROM users WHERE username = ?",
            username)

        # Ensure username exists and password is correct
        if len(users) != 1 or not check_password_hash(
            users[0]["hash"], password
        ):
            return render_template("login.html",
                                   username=username,
                                   password=password,
                                   password_failure="either username or password do not match")

        # Remember which user has logged in
        session["user_id"] = users[0]["id"]

        flash(f"Hey {username.capitalize()} you are back, welcome!")
        return redirect("/")
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        password_confirmation = request.form.get("confirmation")

        if not username:
            return render_template("register.html",
                                   username_failure="please provide an username")
        elif helpers.check_username(username):
            return render_template("register.html",
                                   username=username,
                                   username_failure="username already exists")

        if not password:
            return render_template("register.html",
                                   username=username,
                                   password_failure="please provide a password")
        elif password != password_confirmation:
            return render_template("register.html",
                                   username=username,
                                   password=password,
                                   confirmation=password_confirmation,
                                   confirmation_failure="passwords do not match")

        db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)",
            username,
            generate_password_hash(password),
        )

        user_data = db.execute(
            "SELECT * FROM users WHERE username = ?", username)

        session["user_id"] = user_data[0]["id"]

        flash(
            f"Hello {username.capitalize()}!, you were successfully Registered!")
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/add-new-note", methods=["GET", "POST"])
@helpers.login_required
def add_new_note():
    if request.method == "POST":
        current_user_id = session["user_id"]

        note_content = request.form.get("note-content")

        if note_content:
            db.execute("""INSERT INTO user_notes (user_id, note_content)
                        VALUES (?, ?)""",
                       current_user_id, note_content)

        return redirect("/")


@app.route("/update-note", methods=["GET", "POST"])
@helpers.login_required
def update_note():
    if request.method == "POST":
        note_content = request.form.get("note-content")
        note_id = request.form.get("note-id")

        if note_content:
            db.execute("""UPDATE user_notes
                        SET note_content = ?
                        WHERE id = ?""",
                       note_content, note_id)

        return redirect("/")


@app.route("/delete-note", methods=["GET", "POST"])
@helpers.login_required
def delete_note():
    if request.method == "POST":
        note_id = request.form.get("note-id")
        db.execute("""DELETE FROM user_notes
                        WHERE id = ?""", note_id)
        return redirect("/")


@app.route("/search-notes", methods=["GET", "POST"])
@helpers.login_required
def search_notes():
    if request.method == "POST":
        current_user_id = session["user_id"]
        value_searched = request.form.get("q")
        value_searched = f"%{value_searched}%"

        if value_searched:
            notes_found = db.execute("""SELECT *
                                  FROM user_notes
                                  WHERE user_id = ?
                                  AND note_content LIKE ?""",
                                     current_user_id,
                                     value_searched)
        results = len(notes_found)
        return render_template("search-results.html",
                               results=results,
                               notes_found=notes_found)
