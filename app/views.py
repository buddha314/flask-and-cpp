from app import app
from app import clegs_ext
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Captain %s' % clegs_ext.get_captain_name()}
    return render_template('index.html', title='The Black Pearl', user=user)
