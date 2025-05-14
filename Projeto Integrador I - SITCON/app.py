from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  

VALID_USERNAME = 'teste'
VALID_PASSWORD = 'teste'

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('sitcon'))
        else:
            error = 'Usuário ou senha incorretos!'
    
    return render_template('login.html', error=error)

@app.route('/sitcon')
def sitcon():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('sitcon.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)