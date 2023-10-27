from flask import Flask, render_template, redirect, url_for, session, request
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
#Store session data for one week
app.permanent_session_lifetime = timedelta(days=7)

@app.route('/', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template('home.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route("/user")
def user():
   if "user" in session:
       user = session["user"]
       return f"<h1>{user}</h1>" 
   else:
       return redirect(url_for("login"))
   
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

