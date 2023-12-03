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
       all_comments = connect_db.get_all_comments()
       print(all_posts)
       print(all_comments)
       newdata = []
       #match up posts with comments
       
       for post in all_posts:
            comments = []
            for comment in all_comments:
                if comment[1] == post[0]:
                    comments.append(comment)
            newdata.append((post, comments))
            
       print(newdata)       
       return render_template("home.html", user = user, data = newdata)
   else:
       return redirect(url_for("login"))
   

@app.route("/search", methods=["POST", "GET"])
def search():
    return render_template("search.html")


@app.route("/search_vibes", methods=["GET", "POST"])
def search_vibes():
    categories = ['All Vibes', 'Books', 'Entertainment', 'Miscellaneous', 'Music', 'Sports']
    return render_template("search_vibes.html", categories = categories)


@app.route("/all_vibes", methods=["GET", "POST"])
def all_vibes():
    vibes = connect_db.get_all_vibes()
   # print(vibes)
    comments = connect_db.get_all_comments()
    newdata = []
    #match up posts with comments
    for post in vibes:
        new_comments = []
        for comment in comments:
            if comment[1] == post[0]:
                new_comments.append(comment)
        newdata.append((post, new_comments))
    #print(newdata)
    
    return render_template("all_vibes.html", vibes=newdata)


@app.route("/books", methods=["GET", "POST"])
def books():
    vibes = connect_db.get_filtered_vibes("Books")
    category = "Books"
    
    all_comments = connect_db.get_all_comments()
    
    newdata = []
    #match up posts with comments
    for post in vibes:
        comments = []
        for comment in all_comments:
            if comment[1] == post[0]:
                comments.append(comment)
        newdata.append((post, comments))
        
    return render_template("books.html", vibes=newdata, category=category)


@app.route("/entertainment", methods=["GET", "POST"])
def entertainment():
    vibes = connect_db.get_filtered_vibes("Entertainment")
    category = "Entertainment"
    
    all_comments = connect_db.get_all_comments()
    
    newdata = []
    #match up posts with comments
    for post in vibes:
        comments = []
        for comment in all_comments:
            if comment[1] == post[0]:
                comments.append(comment)
        newdata.append((post, comments))
        
    return render_template("entertainment.html", vibes=newdata, category=category)


@app.route("/misc", methods=["GET", "POST"])
def misc():
    vibes = connect_db.get_filtered_vibes("Miscellaneous")
    category = "Miscellaneous"
    
    all_comments = connect_db.get_all_comments()
    
    newdata = []
    #match up posts with comments
    for post in vibes:
        comments = []
        for comment in all_comments:
            if comment[1] == post[0]:
                comments.append(comment)
        newdata.append((post, comments))
    return render_template("misc.html", vibes=newdata, category=category)


@app.route("/music", methods=["GET", "POST"])
def music():
    vibes = connect_db.get_filtered_vibes("Music")
    category = "Music"
    
    all_comments = connect_db.get_all_comments()
    
    newdata = []
    #match up posts with comments
    for post in vibes:
        comments = []
        for comment in all_comments:
            if comment[1] == post[0]:
                comments.append(comment)
        newdata.append((post, comments))
    
    return render_template("music.html", vibes=newdata, category=category)


@app.route("/sports", methods=["GET", "POST"])
def sports():
    vibes = connect_db.get_filtered_vibes("Sports")
    category = "Sports"
    
    all_comments = connect_db.get_all_comments()
    
    newdata = []
    #match up posts with comments
    for post in vibes:
        comments = []
        for comment in all_comments:
            if comment[1] == post[0]:
                comments.append(comment)
        newdata.append((post, comments))
    return render_template("sports.html", vibes=newdata, category=category)


@app.route("/users", methods=["GET", "POST"])
def users():
    
    user = session["user"]
    all_users = connect_db.get_all_users()

    requested = connect_db.get_sent_requests(user)
    friends = connect_db.get_user_friends(user)

    print(requested)

    requested_or_friends = []
    for usr in requested:
        requested_or_friends.append(usr[0])

    for usr in friends:
        requested_or_friends.append(usr[0])

    print(requested_or_friends)

    #List of the tuples of users who the current user is not already friends with or has already sent a request to
    filtered_users = []
    for usr in all_users:
        if usr[0] not in requested_or_friends and usr[0] != user:
            filtered_users.append(usr)

    return render_template("users.html", user = user, data = filtered_users)


@app.route("/profile", methods=["GET", "POST"])
def profile():
    if "user" in session:
        user = session["user"]

        user_posts = connect_db.get_user_posts(user)
        
        all_comments = connect_db.get_all_comments()
        
        newdata = []
        #match up posts with comments
        for post in user_posts:
            comments = []
            for comment in all_comments:
                if comment[1] == post[0]:
                    comments.append(comment)
            newdata.append((post, comments))
        return render_template("profile.html", user = user, data = newdata)
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
    user = session["user"]
    if request.method == "POST":
        category = request.form["categories"]
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


@app.route('/deletePost/<int:post_id>', methods=['GET', 'POST'])
def delete_post(post_id):
    connect_db.delete_post(post_id)
    
    return redirect(url_for("profile"))

#Routes to interact with the JavaScript
@app.route("/like_post", methods=["POST"])
def like_post():
    user = session["user"]
    post_id = request.json["post_id"]
    print(f"post id: {post_id}")
    result = connect_db.get_user_likepost(user, post_id)
    
    # get total post likes
    # homepage = connect_db.get_user_homepage(user)
    # print(homepage)
    
    
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

@app.route("/like_comment", methods=["POST"]) 
def like_comment():
    user = session["user"]
    comment_id = request.json["comment_id"]
    print(f"comment id: {comment_id}")    
    # get total post likes
    # homepage = connect_db.get_user_homepage(user)
    # print(homepage)
    
    
    result = connect_db.get_user_likecomment(user, comment_id)
    print(result)   
    
    if len(result) == 0:
        connect_db.add_like_comment(user, comment_id)
        connect_db.increment_likes_comment(comment_id)
        return jsonify({"result": "liked"})
    else:
        connect_db.remove_like_comment(user, comment_id)
        connect_db.decrement_likes_comment(comment_id)
        return jsonify({"result": "unliked"})
    
@app.route("/send_request", methods=["POST"])
def send_request():
    user1 = session["user"]
    user2 = request.json["user_name2"]

    connect_db.send_request(user1, user2)
    return jsonify({"result": "success"})


@app.route("/accept_request", methods=["POST"])
def accept_request():
    user1 = session["user"]
    user2 = request.json["requester"]

    connect_db.add_friends(user1, user2)
    connect_db.delete_request(user2, user1)

    return jsonify({"result": "success"})


@app.route("/reject_request", methods=["POST"])
def reject_request():
    user1 = request.json["requester"]
    user2 = session["user"]

    connect_db.delete_request(user1, user2)
    return jsonify({"result": "success"})


# I think there's a way to use something like this to have just one dynamic page for filtering posts,
# instead of a bunch of static ones. But I can't get it to work so it's just static for now. 
@app.route("/filter", methods=["POST"])
def filter():
    category = request.json["category"]
    
    if category == "All Vibes":
        vibes = connect_db.get_all_vibes()

    else:
        vibes = connect_db.get_filtered_vibes(category)

    jsonify({"result": "success"})

    return redirect("/vibes")

