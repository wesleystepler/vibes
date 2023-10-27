from flask import Flask, render_template, redirect, url_for, session, request
from datetime import timedelta
import connect_db

app = Flask(__name__)
app.secret_key = "hello"
#Store session data for one week
app.permanent_session_lifetime = timedelta(days=7)

@app.route('/', methods=["POST", "GET"])
def login():

    #SECURITY UPDATES NEEDED, ESPECIALLY FOR PASSWORD STORING AND CHECKING
    if request.method == "POST":
        session.permanent = True
        user = request.form["usr"]
        password = request.form["pwd"]

        #Make sure this username and password exist together in some user instance
        validate_request = connect_db.get_all_users()
        for user_creds in validate_request:
            if user in user_creds and password in user_creds:
                session["user"] = user
                return redirect(url_for("user"))
        return redirect(url_for("bad_login"))
    
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template('home.html')

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        session.permanent = True
        user = request.form["usr"]
        password = request.form["pwd"]
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]

        session["user"] = user
        email = request.form["email"]

        connect_db.add_new_user(user, password, first_name, last_name, email)

        return redirect(url_for("user"))

        # ADD CHECKS TO MAKE SURE EVERYTHING INPUTTED IS VALID

    return render_template('signup.html')

@app.route("/bad_login")
def bad_login():
    return render_template("bad_login.html")

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

