from flask import Flask, render_template, redirect, url_for, session, request

app = Flask(__name__)
app.secret_key = "hello"

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    return render_template('login.html')

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
