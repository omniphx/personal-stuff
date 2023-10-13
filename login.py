from flask import Flask, url_for, app, request, session, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = b'27e08319c94814a9116248be5cae18ff41581c2dacc3bb2608e2f5b0661ab1e8'

# @app.route("/")
# def hello_world():
#     return url_for('static', filename='index.html')

# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}!"

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username /></p>
            <p><input type=submit value=Login /></p>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))