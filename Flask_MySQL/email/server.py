from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from datetime import datetime as dt
app = Flask(__name__)
mysql = MySQLConnector(app,'email')
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key = 'secrets'

@app.route('/')
def index():
        return render_template("index.html")

@app.route('/authorize', methods=['POST'])
def email():
        email = request.form['email_address']
        if len(request.form['email_address'])<1:
            flash('Oops! You forgot your email.')
            return redirect('/')
        if not EMAIL_REGEX.match(email):
            flash("Invalid Email Address!")
            return redirect('')
        else:
            sql_parameters = {
                            'email': email,
                            'created_at': dt.now()
                            }
            sql_insert_email = 'insert into email(email, created_at) values(:email, :created_at)'
            session['email'] = email
            user_id_from_db = mysql.query_db(sql_insert_email, sql_parameters)
            return redirect('/valid_email')


@app.route('/valid_email')
def show():
    query = "SELECT * FROM email"
    emailList = mysql.query_db(query)
    return render_template('valid_email.html', user_email = session['email'],result_list=emailList)

app.run(debug=True)
