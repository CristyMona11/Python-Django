from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendss')

@app.route('/')
def index():
    query = "SELECT * FROM friendss"
    friend_as = mysql.query_db(query)
    return render_template('index.html', all_friends=friendss)

@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friendss (first_name, last_name, email, created_at, updated_at) VALUES(:first_name, :last_name, :email, NOW(), NOW())"
    parameter = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email']
            }
    mysql.query_db(query, parameter)
        # add a friend to the database
    return redirect('/')

@app.route('/friends/<friend_id>')
def show(friend_id):
    query = "SELECT * FROM friends WHERE id = :specific_id"
    parameter = {'specific_id': friend_id}
    friendss = mysql.query_db(query, parameter)
    return render_template('index.html', one_friend=friendss[0])

@app.route('/update_friend', methods=['POST'])
def update():
    query = "UPDATE friendss SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
    parameter = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'email': request.form['email'],
             'id': request.form['id']
           }
    mysql.query_db(query, parameter)
    return redirect('/')

@app.route('/remove_friend/<friend_id>', methods=['POST'])
def delete(friend_id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': friend_id}
    mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True)
