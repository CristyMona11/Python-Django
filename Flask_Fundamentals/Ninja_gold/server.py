from flask import Flask, render_template, session, redirect, request
import random

app=Flask(__name__)
app.secret_key='secret'

@app.route('/')
def index():
    if 'total_gold' not in session:
        session['total_gold'] = 0
        # session['history'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def coins():
    if 'history' not in session:
        session['history'] = []
    if request.form['building']=='farm':
        farm_gold= random.randrange(10,21)
        session['total_gold'] += farm_gold
        history=session['history']
        history.insert(0,'You earned ' + str(farm_gold) +' !')
        session['history']=history
    elif request.form['building']=='cave':
        cave_gold= random.randrange(5,16)
        session['total_gold'] += cave_gold
        history=session['history']
        history.insert(0,'You earned ' + str(cave_gold) + ' !')
        session['history']=history
    elif request.form['building']=='house':
        house_gold= random.randrange(2,6)
        session['total_gold'] += house_gold
        history=session['history']
        history.insert(0,'You earned ' + str(house_gold) + ' !')
        session['history']=history
    elif request.form['building']=='casino':
        casino_gold= random.randrange(-50,51)
        session['total_gold'] += casino_gold
        if casino_gold < 0:
            history=session['history']
            history.insert(0,'You lost ' + str(casino_gold) + ' !')
            session['history']=history
        if casino_gold > 0:
            history=session['history']
            history.insert(0,'You earned ' + str(casino_gold) +  ' gold!')
            session['history']=history
    print session['history']
    print session['total_gold']
    return redirect('/')

@app.route('/reset', methods=['POST'])
def clear():
    session.clear()
    return redirect('/')

app.run(debug=True)
