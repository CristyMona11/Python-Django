from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key='this'

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/tamarind')
def costa():
    history=session['trip_history']
    history.insert(0,'Surfed up!')
    session['trip_history']=history
    return render_template('Tamarindo.html')

@app.route('/thai')
def bang():
    history=session['trip_history']
    history.insert(0,'Rode an elephant!')
    session['trip_history']=history
    return render_template('Thailand.html')

@app.route('/barce')
def espan():
    history=session['trip_history']
    history.insert(0,'Juggled with Messi!')
    session['trip_history']=history
    return render_template('Spain.html')

@app.route('/login')
def log():
    return render_template('login.html')

@app.route('/authenticate', method=['POST'])
def auth():
    server_email=request.form['html_email']
    server_password=request.form['html_password']
    if server_email=='user@gmail.com' and server_password=="asdfasdf":
        session['user_name']='Some User'
        session['email']=server_email
        session['trip_history']=[]
        return render_template('success.html', template_email=server_email, template_password=server_password)
    else:
        return redirect('/login')
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
app.run(debug=True)
