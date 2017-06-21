from flask import Flask, render_template,request,flash,redirect,session,url_for
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja')
def ninjas():
    src= (url_for('static', filename='tmnt.png'))
    return render_template("ninja.html", src = src)

@app.route('/ninja/<color>')
def handler_function(color):
    src=""
    if color == 'purple':
        src= (url_for('static', filename='donatello.jpg'))
    elif color == 'blue':
        src= (url_for('static', filename='leonardo.jpg'))
    elif color == 'orange':
        src= (url_for('static', filename='michelangelo.jpg'))
    elif color == 'red':
        src= (url_for('static', filename='raphael.jpg'))
    else:
        src= (url_for('static', filename='notapril.jpg'))
    return render_template('ninja.html', src = src)
app.run(debug=True)
