from flask import Flask, render_template,request,redirect,flash,session
app = Flask(__name__)
app.secret_key = 'secrets'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/authorize', methods=['POST'])
def auth():
    if len(request.form['server_name'])<1:
        flash('Oops!You forgot your name.')
        return redirect('/')
    else:
        flash("{}, beautiful name.".format(request.form['server_name']))
    server_name = request.form['server_name']
    server_location = request.form['location']
    server_fave_language = request.form['fave_language']
    if len(request.form['description'])<1:
        flash('Wait! You forgot a comment!')
        return redirect('/')
    elif len(request.form['description'])>120:
        flash('Eeeeek! Too many thoughts!')
        return redirect('/')
    else:
        flash("Hip hip! Your thoughts are awesome!".format(request.form['description']))
    server_description = request.form['description']
    return render_template('/submit.html', name=server_name, location= server_location, fave_language=server_fave_language, description=server_description )

app.run(debug=True)
