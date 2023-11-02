from flask import Flask, render_template, redirect, url_for, session, request
from flask_bcrypt import Bcrypt
from datetime import timedelta
import connect_db


app = Flask(__name__)
app.secret_key = "hello" # This can be anything (and maybe should be more secure), I was just following my boy Tim's tutorial.


# Store session data for one week
app.permanent_session_lifetime = timedelta(days=7)

#initialize the bcrypt
bcrypt = Bcrypt(app)

@app.route('/', methods=["POST", "GET"])
def login():
    # SECURITY UPDATES NEEDED, ESPECIALLY FOR PASSWORD STORING AND CHECKING
    #connect_db.update_password()
    # Get the username and password from the front end.
    if request.method == "POST":
        session.permanent = True
        user = request.form["usr"]
        password = request.form["pwd"]

        # Make sure this username and password exist together in some user instance.
        # If not, redirect user to bad login page, which will ask either for different credentials
        # or for the user to create a new account.
        if connect_db.get_user(user):
            user_pwd = connect_db.get_password(user)
            if bcrypt.check_password_hash(user_pwd[0][0], password):
                session["user"] = user
                return redirect(url_for("user"))
            else:
                error_message = "Invalid username or password."
                return render_template("home.html", error_message=error_message)
        error_message = "Invalid username or password."
        return render_template("home.html", error_message=error_message)
    
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

        if connect_db.get_user(user):
            error_message = "Username already exists, Please use a different username."
            return render_template("signup.html", error_message=error_message)

        session["user"] = user
        email = request.form["email"]
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Execute the SQL Query to add a new user with the above arguments
        connect_db.add_new_user(user, hashed_password, first_name, last_name, email)

        return redirect(url_for("user"))

        # ADD CHECKS TO MAKE SURE EVERYTHING INPUTTED IS VALID

    return render_template('signup.html')

# @app.route("/bad_login")
# def bad_login():
#     return render_template("bad_login.html")

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

