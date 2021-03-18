from app import app
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
    user = { 'username':'Victor'}
    posts = [
        {'author' : {'username': 'Maria'}, 'body': 'Olá Murta'},
        {'author' : {'username': 'Murta'}, 'body': 'Olá Maria'},
    ]
    return render_template("index.html", user=user, posts=posts)
