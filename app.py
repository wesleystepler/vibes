from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def potd5():
    return render_template("simpleform.html")
