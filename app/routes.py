from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'wushuzh'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Wanderland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
