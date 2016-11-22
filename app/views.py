from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Captain Jack Sparrow'}
    return render_template('index.html', title='The Black Pearl', user=user)
