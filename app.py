from flask import Flask, redirect, url_for, render_template, request
from getpass import getpass
from mysql.connector import connect, Error
from connect_db import add_friend, select_all_friends

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def potd5():
    if request.method == "POST":
        print(request.form)
        for tup in request.form:
            if "Add friend" in request.form[tup]:
                print(tup)
                friend_name = request.form["friendname"]
                friend_major = request.form["major"]
                friend_year = int(request.form["year"])
                add_friend(friend_name, friend_major, friend_year)
                break

            elif "Update" in request.form[tup]:
                print(tup)

            elif "Delete" in request.form[tup]:
                print(tup)
                
    data = select_all_friends()
    #for i in data:
    #    print(i)    
    return render_template("simpleform.html", data=data)
