from flask import Flask, render_template,request,flash,redirect,session
import re
app = Flask(__name__)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key = 'secret7s'


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/authorize', methods=['POST'])
def auth():
    is_valid = True
    if len(request.form['server_email'])<1:
        flash('Oops!You forgot your email.')
        is_valid = False
    if not EMAIL_REGEX.match(request.form['server_email']):
        flash("Invalid Email Address!")
        is_valid = False
    if len(request.form['server_fname'])<1:
        flash('Oops!You forgot your first name.')
        is_valid = False
    if str.isalpha(str(request.form['server_fname'])) is False:
        flash('Please make sure your first name does not contain any numbers.')
        is_valid = False
    if len(request.form['server_lname'])<1:
        flash('Oops!You forgot your last name.')
        is_valid = False
    if str.isalpha(str(request.form['server_lname'])) is False:
        flash('Please make sure your last name does not contain any numbers.')
        is_valid = False
    if len(request.form['server_password'])<1:
        flash('Oops!You forgot your password.')
        is_valid = False
    if len(request.form['server_password'])<=8:
        flash('Your password must be more than eight characters.')
        is_valid = False
    if len(request.form['server_rpassword'])<1:
        flash('Oops!You forgot to confirm your password.')
        is_valid = False
    if request.form['server_password'] != request.form['rserver_password']:
        flash ('Your passwords do not match!!!')
        is_valid = False

    if is_valid:
        flash('Perfect! You are all set, and good to go!')

    return redirect('/')

app.run(debug=True)
