from flask import render_template
from . import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/manage/')
def manage():
    return render_template('manage.html')

@app.route('/about/')
def about():
    return render_template('about.html')
