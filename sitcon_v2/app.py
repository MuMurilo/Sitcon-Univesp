from flask import Flask, render_template, request, redirect, url_for, session
from sqlalchemy import inspect
from models import db, AMV, Sinais, Usuario, MatriculasValidas
import csv
from werkzeug.security import generate_password_hash
from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory, flash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sitcon.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'univesp'  # Altere para produção

db.init_app(app)



# Criação das tabelas
with app.app_context():
    db.create_all()
    print("Tabelas criadas com sucesso!")

@app.route('/importar_csv', methods=['GET', 'POST'])
def importar_csv():
    if request.method == 'POST':
        if 'arquivo' not in request.files:
            return "Nenhum arquivo enviado", 400
            
        arquivo = request.files['arquivo']
        if not arquivo.filename.endswith('.csv'):
            return "Formato inválido. Envie um arquivo .csv", 400

        try:
            # Processa o arquivo
            stream = arquivo.stream.read().decode("utf-8-sig")
            lines = stream.splitlines()
            
            # Configura leitor CSV para campos entre aspas
            leitor = csv.DictReader(
                lines,
                delimiter=',',
                quotechar='"',
                skipinitialspace=True
            )
            
            criados = 0
            atualizados = 0
            
            for linha in leitor:
                # Remove aspas extras dos cabeçalhos
                linha = {k.strip('"'): v for k, v in linha.items()}
                
                # Busca registro existente
                existente = AMV.query.filter_by(
                    idamv=int(linha['idamv']),
                    tipofuncao=linha['tipofuncao']
                ).first()
                
                if existente:
                    # Atualiza campos (exceto chaves primárias)
                    existente.L1 = linha.get('L1')
                    existente.L2 = linha.get('L2')
                    existente.L3 = linha.get('L3')
                    existente.L4 = linha.get('L4')
                    existente.L5 = linha.get('L5')
                    existente.L6 = linha.get('L6')
                    existente.L7 = linha.get('L7')
                    existente.L9 = linha.get('L9')
                    existente.L10 = linha.get('L10')
                    existente.tower = linha.get('tower')
                    existente.interface = linha.get('interface')
                    existente.L14 = linha.get('L14')
                    existente.L15 = linha.get('L15')
                    existente.L16 = linha.get('L16')
                    existente.L17 = linha.get('L17')
                    existente.L18 = linha.get('L18')
                    existente.L20 = linha.get('L20')
                    existente.L21 = linha.get('L21')
                    existente.L22 = linha.get('L22')
                    existente.L23 = linha.get('L23')
                    atualizados += 1
                else:
                    # Cria novo registro
                    novo_registro = AMV(
                        idamv=int(linha['idamv']),
                        tipofuncao=linha['tipofuncao'],
                        L1=linha.get('L1'),
                        L2=linha.get('L2'),
                        L3=linha.get('L3'),
                        L4=linha.get('L4'),
                        L5=linha.get('L5'),
                        L6=linha.get('L6'),
                        L7=linha.get('L7'),
                        L9=linha.get('L9'),
                        L10=linha.get('L10'),
                        tower=linha.get('tower'),
                        interface=linha.get('interface'),
                        L14=linha.get('L14'),
                        L15=linha.get('L15'),
                        L16=linha.get('L16'),
                        L17=linha.get('L17'),
                        L18=linha.get('L18'),
                        L20=linha.get('L20'),
                        L21=linha.get('L21'),
                        L22=linha.get('L22'),
                        L23=linha.get('L23')
                    )
                    db.session.add(novo_registro)
                    criados += 1
            
            db.session.commit()
            return f"""
                <h3>Importação concluída!</h3>
                <p>✅ {criados} novos registros criados</p>
                <p>🔄 {atualizados} registros atualizados</p>
                <a href="/importar_csv">Voltar</a>
            """
            
        except KeyError as e:
            db.session.rollback()
            return f"Erro: Campo faltando no CSV - {str(e)}", 400
        except Exception as e:
            db.session.rollback()
            return f"Erro na linha {criados+atualizados+1}: {str(e)}", 500
    
    # GET: Mostra formulário
    return '''
    <h2>Importar CSV</h2>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="arquivo" accept=".csv" required>
      <p>Formato esperado: "idamv","tipofuncao","L1",... (com aspas)</p>
      <button type="submit">Importar</button>
    </form>
    '''

# Rotas para a tabela Sinais
@app.route('/importar_sinais_csv', methods=['GET', 'POST'])
def importar_sinais_csv():
    if request.method == 'POST':
        if 'arquivo' not in request.files:
            return "Nenhum arquivo enviado", 400
            
        arquivo = request.files['arquivo']
        if not arquivo.filename.endswith('.csv'):
            return "Formato inválido. Envie um arquivo .csv", 400

        try:
            stream = arquivo.stream.read().decode("utf-8-sig")
            lines = stream.splitlines()
            
            leitor = csv.DictReader(
                lines,
                delimiter=',',
                quotechar='"',
                skipinitialspace=True
            )
            
            criados = 0
            atualizados = 0
            
            for linha in leitor:
                linha = {k.strip('"'): v for k, v in linha.items()}
                
                # Verifica registro existente
                existente = Sinais.query.filter_by(
                    idSinais=int(linha['idSinais']),
                    tipoAspecto=linha['tipoAspecto']
                ).first()
                
                if existente:
                    # Atualiza campos
                    existente.L1 = linha.get('L1')
                    existente.L2 = linha.get('L2')
                    existente.L3 = linha.get('L3')
                    existente.L4 = linha.get('L4')
                    existente.L5 = linha.get('L5')
                    existente.L6 = linha.get('L6')
                    existente.L7 = linha.get('L7')
                    existente.L9 = linha.get('L9')
                    existente.L10 = linha.get('L10')
                    existente.tower = linha.get('tower')
                    existente.interface = linha.get('interface')
                    existente.L14 = linha.get('L14')
                    existente.L15 = linha.get('L15')
                    existente.L16 = linha.get('L16')
                    existente.L17 = linha.get('L17')
                    existente.L18 = linha.get('L18')
                    existente.L20 = linha.get('L20')
                    existente.L21 = linha.get('L21')
                    existente.L22 = linha.get('L22')
                    existente.L23 = linha.get('L23')
                    atualizados += 1
                else:
                    # Cria novo registro
                    novo_registro = Sinais(
                        idSinais=int(linha['idSinais']),
                        tipoAspecto=linha['tipoAspecto'],
                        L1=linha.get('L1'),
                        L2=linha.get('L2'),
                        L3=linha.get('L3'),
                        L4=linha.get('L4'),
                        L5=linha.get('L5'),
                        L6=linha.get('L6'),
                        L7=linha.get('L7'),
                        L9=linha.get('L9'),
                        L10=linha.get('L10'),
                        tower=linha.get('tower'),
                        interface=linha.get('interface'),
                        L14=linha.get('L14'),
                        L15=linha.get('L15'),
                        L16=linha.get('L16'),
                        L17=linha.get('L17'),
                        L18=linha.get('L18'),
                        L20=linha.get('L20'),
                        L21=linha.get('L21'),
                        L22=linha.get('L22'),
                        L23=linha.get('L23')
                    )
                    db.session.add(novo_registro)
                    criados += 1
            
            db.session.commit()
            return f"""
                <h3>Importação de Sinais concluída!</h3>
                <p>✅ {criados} novos registros criados</p>
                <p>🔄 {atualizados} registros atualizados</p>
                <a href="/importar_sinais_csv">Voltar</a>
            """
            
        except Exception as e:
            db.session.rollback()
            return f"Erro: {str(e)}", 500
    
    return '''
    <h2>Importar CSV - Sinais</h2>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="arquivo" accept=".csv" required>
      <p>Formato esperado: "idSinais","tipoAspecto","L1",... (com aspas)</p>
      <button type="submit">Importar</button>
    </form>
    '''

@app.route('/verificar_sinais')
def verificar_sinais():
    registros = Sinais.query.order_by(Sinais.idSinais, Sinais.tipoAspecto).limit(50).all()
    return render_template('verificar_sinais.html', registros=registros)


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

@app.route('/static/<path:filename>')
def static_files(images):
    return send_from_directory('static', images)

@app.route('/sitcon')
def sitcon():
    if not session.get('logado'):
        return redirect(url_for('login'))
    return render_template('sitcon.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        matricula = request.form.get('matricula')
        login = request.form.get('login')
        nome = request.form.get('nome')
        senha = request.form.get('senha')
        
        # Verifica se a matrícula NÃO existe na tabela de matrículas válidas
        if not MatriculasValidas.query.filter_by(matricula=matricula).first():
            flash('Matrícula não encontrada no sistema. Cadastro não permitido.', 'error')
            return redirect(url_for('cadastro'))
        
        # Verifica se a matrícula JÁ está cadastrada como usuário
        if Usuario.query.filter_by(matricula=matricula).first():
            flash('Esta matrícula já possui cadastro ativo.', 'error')
            return redirect(url_for('cadastro'))
        
        # Verifica se o login já existe
        if Usuario.query.filter_by(login=login).first():
            flash('Nome de usuário já em uso. Escolha outro.', 'error')
            return redirect(url_for('cadastro'))
        
        # Cria o usuário se passou nas validações
        novo_usuario = Usuario(
            matricula=matricula,
            login=login,
            nome=nome,
            senha=generate_password_hash(senha)
        )
        
        db.session.add(novo_usuario)
        db.session.commit()
        
        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('login'))
    
    return render_template('cadastro.html', titulo="Cadastro de Usuário")

@app.route('/amv')
def amv():
    if not session.get('logado'):
        return redirect(url_for('login'))
    amv_numbers = [3, 7, 9, 11, 25, 27, 29, 31, 39, 43, 47]
    return render_template('amv.html', 
                        amvs=amv_numbers,
                        titulo='Aparelhos de Mudança de Via')

@app.route('/amv_comando/<amv_id>')
def amv_comando(amv_id):
    return mostrar_amv(amv_id, tipo='Comando')

@app.route('/amv_indicacao/<amv_id>')
def amv_indicacao(amv_id):
    return mostrar_amv(amv_id, tipo='Indicação')


def mostrar_amv(amv_id, tipo):
    if not session.get('logado'):
        flash('Acesso não autorizado', 'error')
        return redirect(url_for('login'))
    
    TRADUCAO_CAMPOS = {
      'idamv': 'AMV',
      'tipofuncao': 'Tipo da Função',
      'L1': 'Locação 1',
        'L2': 'Locação 2',
        'L3': 'Locação 3',
        'L4': 'Locação 4',
        'L5': 'Locação 5',
        'L6': 'Locação 6',
        'L7': 'Locação 7',
        'L9': 'Locação 9',
        'L10': 'Locação 10',
        'tower': 'NX',
        'interface': 'Bastidor de Interface',
        'L14': 'Locação 14',
        'L15': 'Locação 15',
        'L16': 'Locação 16',
        'L17': 'Locação 17',
        'L18': 'Locação 18',
        'L20': 'Locação 20',
        'L21': 'Locação 21',
        'L22': 'Locação 22',
        'L23': 'Locação 23'
    }

    try:
        amv_number = int(amv_id)
    except ValueError:
        flash('ID do AMV deve ser um número', 'error')
        return redirect(url_for('amv'))
    
    # Definindo dados como lista vazia por padrão
    dados = []
    
    try:
        # Filtra por tipo (ajuste conforme sua lógica de negócios)
        if tipo == 'Comando':
            registros = AMV.query.filter_by(idamv=amv_number)\
                               .filter(AMV.tipofuncao.in_(['NWR', 'WR']))\
                               .order_by(AMV.tipofuncao)\
                               .all()
        else:  # Indicação
            registros = AMV.query.filter_by(idamv=amv_number)\
                               .filter(AMV.tipofuncao.in_(['NWP', 'WP']))\
                               .order_by(AMV.tipofuncao)\
                               .all()
        
        # Processa os registros encontrados
        for registro in registros:
            campos = {}
            for coluna in AMV.__table__.columns:
                nome_original = coluna.name
                nome_amigavel = nome_original if nome_original == 'tipofuncao' else TRADUCAO_CAMPOS.get(nome_original, nome_original)
                valor = getattr(registro, nome_original)
                if valor not in [None, '']:
                    campos[nome_amigavel] = valor
            dados.append(campos)
            
    except Exception as e:
        flash(f'Erro ao acessar banco de dados: {str(e)}', 'error')
        return redirect(url_for('amv'))
    
    if not dados:
        flash(f'Nenhum registro de {tipo} encontrado para AMV {amv_number}', 'warning')
        return redirect(url_for('amv'))
    
    return render_template('amv_detail.html',
                         amv_id=amv_number,
                         registros=dados,
                         tipo=tipo)

@app.route('/amv/<amv_id>')
def amv_detail(amv_id):
    if not session.get('logado'):
        return redirect(url_for('login'))
    
    try:
        amv_number = int(amv_id)
    except ValueError:
        flash('ID do AMV inválido', 'error')
        return redirect(url_for('amv'))
    
    # Busca TODOS os registros do AMV (não apenas o primeiro)
    registros = AMV.query.filter_by(idamv=amv_number).order_by(AMV.tipofuncao).all()
    
    if not registros:
        flash(f'AMV {amv_number} não encontrado', 'warning')
        return redirect(url_for('amv'))
    
    # Prepara os dados para o template
    dados = []
    for registro in registros:
        campos_registro = {}
        for coluna in AMV.__table__.columns:
            nome = coluna.name
            valor = getattr(registro, nome)
            if valor not in [None, '']:
                campos_registro[nome] = valor
        dados.append(campos_registro)
    
    return render_template('amv_detail.html',
                        amv_id=amv_number,
                        registros=dados)

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
    sinais = [4, 6, 12, 16, 20, 22, 28, 30, 52, 54, 56, 62, 64, 66, 68, 70, 72, 78, 80]
    return render_template('sinais.html', sinais=sinais, titulo='Sinais')

@app.route('/sinais/<sinal_id>')
def sinal_detail(sinal_id):
    if not session.get('logado'):
        return redirect(url_for('login'))
    
    try:
        amv_number = int(sinal_id)
    except ValueError:
        flash('ID do SINAL inválido', 'error')
        return redirect(url_for('sianais'))
    
    TRADUCAO_CAMPOS = {
      'idSinais': 'SINAL',
      'tipoAspecto': 'Tipo do Aspecto',
      'L1': 'Locação 1',
        'L2': 'Locação 2',
        'L3': 'Locação 3',
        'L4': 'Locação 4',
        'L5': 'Locação 5',
        'L6': 'Locação 6',
        'L7': 'Locação 7',
        'L9': 'Locação 9',
        'L10': 'Locação 10',
        'tower': 'NX',
        'interface': 'Bastidor de Interface',
        'L14': 'Locação 14',
        'L15': 'Locação 15',
        'L16': 'Locação 16',
        'L17': 'Locação 17',
        'L18': 'Locação 18',
        'L20': 'Locação 20',
        'L21': 'Locação 21',
        'L22': 'Locação 22',
        'L23': 'Locação 23'
    }
    
    registros = Sinais.query.filter_by(idSinais=sinal_id).all()
    
    if not registros:
        flash(f'SINAL {sinal_id} não encontrado', 'warning')
        return redirect(url_for('sinal'))
    
        # Prepara os dados para o template
    dados = []
    for registro in registros:
        campos_registro = {}
        for coluna in Sinais.__table__.columns:
            nome_original = coluna.name
            nome_amigavel = nome_original if nome_original == 'tipoAspecto' else TRADUCAO_CAMPOS.get(nome_original, nome_original)
            valor = getattr(registro, nome_original)
            if valor not in [None, '']:
                campos_registro[nome_amigavel] = valor
        dados.append(campos_registro)

    if not dados:
        flash(f'Sinal {sinal_id} não encontrado', 'warning')
        return redirect(url_for('sinais'))
    
    return render_template('sinal_detail.html',
                        sinal_id=sinal_id,
                        registros=dados)

@app.route('/logout')
def logout():
    session.pop('logado', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)