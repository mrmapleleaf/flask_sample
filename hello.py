from flask import Flask
from markupsafe import escape 

app = Flask(__name__)

@app.route('/')
def hello():
    return '<p>Index Page</p>'

@app.route('/hello')
def hello_world():
    return '<p>Hello, World!</p>'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'<p>User: {username}</p>'

# int型のパラメータを受け取るルート
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post ID: {post_id}'

# /path型のパラメータを受け取るルート
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath: {escape(subpath)}'

