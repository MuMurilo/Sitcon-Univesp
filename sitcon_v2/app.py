from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'univesp'  # Altere para produção

# Credenciais válidas
USUARIO = 'teste'
SENHA = 'teste'

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    erro = None
    
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        
        if usuario == USUARIO and senha == SENHA:
            session['logado'] = True
            return redirect(url_for('sitcon'))
        else:
            erro = 'Credenciais inválidas!'
    
    return render_template('login.html', erro=erro)

@app.route('/sitcon')
def sitcon():
    if not session.get('logado'):
        return redirect(url_for('login'))
    return render_template('sitcon.html')

@app.route('/amv')
def amv():
    if not session.get('logado'):
        return redirect(url_for('login'))
    amvs = ['AMV 3 LUZ', 'AMV 7 LUZ', 'AMV 9 LUZ', 'AMV 11 LUZ', 'AMV 25 LUZ', 'AMV 27 LUZ', 'AMV 29 LUZ', 'AMV 31 LUZ', 'AMV 39 LUZ','AMV 43 LUZ', 'AMV 47 LUZ']
    return render_template('amv.html', amvs=amvs, titulo='Aparelhos de Mudança de Via')

@app.route('/cdv')
def cdv():
    if not session.get('logado'):
        return redirect(url_for('login'))
    cdvs = ['1N08T LUZ', '1N09T LUZ', '1N10T LUZ', '1N11T LUZ', '1S06T LUZ', '1S07T LUZ', '1S09T LUZ', '1S11T LUZ', '1S12T LUZ', '1S13T LUZ', '1S14T LUZ', '2N06T LUZ', '2N07T LUZ', '2N08T LUZ', '2N09T LUZ', '2N10T LUZ', '2S08T LUZ', '2S09T LUZ', '2S10T LUZ', '2S11T LUZ', '2S12T LUZ', '2S13T LUZ', '2S14T LUZ', '2S15T LUZ']
    return render_template('cdv.html', cdvs=cdvs, titulo='Circuitos de Via')

@app.route('/sinais')
def sinais():
    if not session.get('logado'):
        return redirect(url_for('login'))
    sinais = ['Sinal-4 LUZ', 'Sinal-6 LUZ', 'Sinal-12 LUZ', 'Sinal-16 LUZ', 'Sinal-20 LUZ', 'Sinal-22LUZ', 'Sinal-28LUZ', 'Sinal-30LUZ', 'Sinal-52LUZ', 'Sinal-54LUZ', 'Sinal-56LUZ', 'Sinal-62 LUZ', 'Sinal-64 LUZ', 'Sinal-66 LUZ', 'Sinal-68 LUZ', 'Sinal-70 LUZ', 'Sinal-72 LUZ', 'Sinal-78 LUZ', 'Sinal-80 LUZ']
    return render_template('sinais.html', sinais=sinais, titulo='Sinais')

@app.route('/logout')
def logout():
    session.pop('logado', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)