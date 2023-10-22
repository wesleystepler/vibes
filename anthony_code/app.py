from flask import Flask, render_template, request
#from sqlalchemy import text, create_engine
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    data = get_friends()
    return render_template('home.html', friends=data)

@app.route('/add_friend', methods=['POST'])
def add_friend():
    conn = get_db_connection()
    name = request.form['name']
    major = request.form['major']
    year = int(request.form['year'])

    query = 'INSERT INTO friend (name, major, year) VALUES (:name, :major, :year)'
    conn.execute(query, {'name': name, 'major': major, 'year': year})
    conn.commit()
    conn.close()
    
    data = get_friends()

    return render_template('home.html', friends=data)

@app.route('/delete_friend', methods=['POST'])
def delete_friend():
    conn = get_db_connection()
    name = request.form['name']

    query = 'DELETE FROM friend WHERE name = :name'
    conn.execute(query, {'name': name})
    conn.commit()
    conn.close()
    
    data = get_friends()

    return render_template('home.html', friends=data)

@app.route('/update_friend', methods=['POST'])
def update_friend():
    conn = get_db_connection()
    name = request.form['name']
    major = request.form['major']
    year = int(request.form['year'])

    query = 'UPDATE friend SET major = :major, year = :year WHERE name = :name'
    conn.execute(query, {'name': name, 'major': major, 'year': year})
    conn.commit()
    conn.close()
    
    data = get_friends()

    return render_template('home.html', friends=data)


def get_friends():
    conn = get_db_connection()
    query = 'SELECT * FROM friend'
    friends = conn.execute(query).fetchall()
    conn.close()
    return friends


if __name__ == '__main__':
    app.run(debug=True)
