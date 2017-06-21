from flask import Flask, render_template, request, redirect, session
import random

app=Flask(__name__)
app.secret_key='secret'

@app.route('/')
def index():
    if 'message' not in session:
        session['message']=""
    if 'num' not in session:
        session['num']= random.randrange(0, 101)
    return render_template('index.html',message=session['message'])

@app.route('/guess', methods=['POST'])
def guess():
    guess=int(request.form['num'])
    if guess==session['num']:
        session['message'] = 'You Win!'
    if guess>session['num']:
        session['message'] = 'Too High! Close, but not close enough. Guess again!'
    elif guess<session['num']:
        session['message'] ='Too Low! Close, but not close enough. Guess again!'
    return render_template('index.html', message=session['message'])

@app.route('/reset')
def reset():
    session['num']
    session.pop('num')
    session.pop('message')
    return redirect('/')

app.run(debug=True)
