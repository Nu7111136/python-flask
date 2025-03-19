from flask import Flask, session, redirect, url_for, request
import secrets  # For generating a secure secret key

app = Flask(__name__)

# Generate a secure secret key
app.secret_key = secrets.token_hex(16)  # 16 bytes = 32-character hexadecimal string

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return f"Welcome back, {username}! <a href='/logout'>Logout</a>"
    return "You are not logged in. <a href='/login'>Login</a>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username  # Save username in session
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type="text" name="username" placeholder="Enter Username">
            <p><input type="submit" value="Login">
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove username from session
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
