from flask import Flask, render_template, redirect, url_for, session, request
from datetime import timedelta
import connect_db

app = Flask(__name__)
app.secret_key = "hello" # This can be anything (and maybe should be more secure), I was just following my boy Tim's tutorial.

# Store session data for one week
app.permanent_session_lifetime = timedelta(days=7)

@app.route('/', methods=["POST", "GET"])
def login():

    # SECURITY UPDATES NEEDED, ESPECIALLY FOR PASSWORD STORING AND CHECKING

    # Get the username and password from the front end.
    if request.method == "POST":
        session.permanent = True
        user = request.form["usr"]
        password = request.form["pwd"]

        # Make sure this username and password exist together in some user instance.
        # If not, redirect user to bad login page, which will ask either for different credentials
        # or for the user to create a new account.
        validate_request = connect_db.get_all_users()
        for user_creds in validate_request:
            if user in user_creds and password in user_creds:
                session["user"] = user
                return redirect(url_for("user"))
        return redirect(url_for("bad_login"))
    
    else:
        # If there are saved login credentials, just go to the user's page.
        if "user" in session:
            return redirect(url_for("user"))
        return render_template('home.html')

@app.route('/signup', methods=["GET", "POST"])
def signup():
    # Get new user credentials from the front end.
    if request.method == "POST":
        session.permanent = True
        user = request.form["usr"]
        password = request.form["pwd"]
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]

        session["user"] = user
        email = request.form["email"]

        # Execute the SQL Query to add a new user with the above arguments
        connect_db.add_new_user(user, password, first_name, last_name, email)

        return redirect(url_for("user"))

        # ADD CHECKS TO MAKE SURE EVERYTHING INPUTTED IS VALID

    return render_template('signup.html')

@app.route("/bad_login")
def bad_login():
    return render_template("bad_login.html")

@app.route("/user")
def user():
   # Very basic user page. This will eventually be the user's home page.
   if "user" in session:
       user = session["user"]
       return f"<h1>{user}</h1>" 
   else:
       return redirect(url_for("login"))
   
@app.route("/logout")
def logout():
    # Currently no page or button for this.
    session.pop("user", None)
    return redirect(url_for("login"))

