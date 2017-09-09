from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
# session['someKey'] = 50
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    # ON RESET
    if not 'someKey' in session:
        # session['someKey'] = 1
        session['someKey'] = random.randrange(0, 101)
        someKey = session['someKey']
        win = False

    else:
        # print session['counter']
        session['someKey'] = session['someKey']
        someKey = session['someKey']
        win = False
        # print session['someKey']
    return render_template("index.html", someKey = someKey)

@app.route('/num_guess', methods = ['POST'])
def guess():

    guess = int(request.form['number'])



    # guess = int(guess)
    someKey = session['someKey']


    if guess == someKey:
        win = True

    else:
        win = False


    return render_template("index.html", guess = guess, win = win, someKey = someKey)


@app.route('/signout',methods= ['POST'])
def sign_out():
    # button = request.form['button']
    # session['counter']=0
    session.pop('someKey')
    # session.pop(someKey)
    return redirect('/')
# def hello_world():
#     return render_template('index.html')
#
# @app.route('/projects')
# def success():
#     return render_template('projects.html')
#
# @app.route('/about')
# def hello():
#     return render_template('about.html')


app.run(debug=True)
