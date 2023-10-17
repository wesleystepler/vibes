from flask import Flask, redirect, url_for, render_template, request
from getpass import getpass
from mysql.connector import connect, Error
from connect_db import add_friend, select_all_friends

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def potd5():
    if request.method == "POST":
        friend_name = request.form["friendname"]
        friend_major = request.form["major"]
        friend_year = int(request.form["year"])
        #print(friend_name, type(friend_name))
        #print(friend_major, type(friend_major))
        #print(friend_year, type(friend_year))

        add_friend(friend_name, friend_major, friend_year)
    data = select_all_friends()    
    return render_template("simpleform.html", data=data)
