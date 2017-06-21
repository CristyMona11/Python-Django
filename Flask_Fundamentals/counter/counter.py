from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def count():
    if 'counter' not in session:
        session['counter']=0
    else:
        session['counter']+=1
        return render_template('index.html', counter=session['counter'])

@app.route('/ninja')
def ninja():
    session['counter']+=1
    return redirect('/')

@app.route('/reset')
def logout():
    session['counter']=0
    return redirect('/')


app.run (debug=True)
