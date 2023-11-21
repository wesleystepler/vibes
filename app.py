from flask import Flask, render_template, redirect, url_for, session, request, jsonify
from flask_bcrypt import Bcrypt
from datetime import timedelta, datetime
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
                return render_template("login.html", error_message=error_message)
        error_message = "Invalid username or password."
        return render_template("login.html", error_message=error_message)
    
    else:
        # If there are saved login credentials, just go to the user's page.
        if "user" in session:
            return redirect(url_for("user"))
        return render_template('login.html')

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

@app.route("/home", methods=["POST", "GET"])
def user():
   # Very basic user page. This will eventually be the user's home page.
   if "user" in session:
       user = session["user"]

       if request.method == "POST":
           if "Create Post" in request.form:
               print()

       all_posts = connect_db.get_user_homepage(user)
       return render_template("home.html", user = user, data = all_posts)
   else:
       return redirect(url_for("login"))
   

@app.route("/search", methods=["POST", "GET"])
def search():
    return render_template("search.html")

@app.route("/users", methods=["GET", "POST"])
def users():
    if "user" in session:
        user = session["user"]
        all_users = connect_db.get_all_users()

        print(request.form.get("data"))
        if request.method == "POST":
            for tup in request.form:
                if "Add Friend" in request.form[tup]:
                    user = request.form["username"]
                    print(user)

        return render_template("users.html", user = user, data = all_users)


@app.route("/profile", methods=["GET", "POST"])
def profile():
    if "user" in session:
        user = session["user"]

        user_posts = connect_db.get_user_posts(user)
        return render_template("profile.html", user = user, data = user_posts)
    return render_template("profile.html")


@app.route("/friends", methods=["POST", "GET"])
def friends():
    if "user" in session:
        user = session["user"]
        num_friends = connect_db.get_user_friends(user)
        return render_template("friends.html", data = num_friends, num = len(num_friends))
    
@app.route("/requests", methods=["GET", "POST"])
def requests():
    user = session["user"]
    reqs = connect_db.get_user_requests(user)

    return render_template("requests.html", data=reqs, num_reqs = len(reqs))
   

@app.route("/create_post", methods=["POST", "GET"])
def create_post():
    if "user" in session:
        user = session["user"]
    if request.method == "POST":
        category = request.form["category"]
        content = request.form["content"]
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        likes = 0
        connect_db.create_new_post(category, time, likes, content, user)
        return redirect(url_for("user"))

    return render_template("create_post.html")


@app.route("/logout")
def logout():
    # Currently no page or button for this.
    session.pop("user", None)
    return redirect(url_for("login"))


#Routes to interact with the JavaScript
@app.route("/like_post", methods=["POST"])
def like_post():
    connect_db.drop_procedure()
    user = session["user"]
    post_id = request.json["post_id"]
    print(f"post id: {post_id}")
    result = connect_db.get_user_likepost(user, post_id)
    
    # get total post likes
    homepage = connect_db.get_user_homepage(user)
    print(homepage)
    
    
    result = connect_db.get_user_likepost(user, post_id)
    print(result)   
    
    if len(result) == 0:
        connect_db.add_like(user, post_id)
        connect_db.increment_likes(post_id)
        return jsonify({"result": "liked"})
    else:
        connect_db.remove_like(user, post_id)
        connect_db.decrement_likes(post_id)
        return jsonify({"result": "unliked"})
    
    
@app.route("/send_request", methods=["POST"])
def send_request():
    user1 = session["user"]
    user2 = request.json["user_name2"]

    connect_db.send_request(user1, user2)
    return jsonify({"result": "success"})


