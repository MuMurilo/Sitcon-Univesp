from flask import Flask, render_template, request, redirect, url_for, session
from sqlalchemy import inspect
from models import db, AMV, Sinais
import csv
from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory, flash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sitcon.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'univesp'  # Altere para produção

db.init_app(app)

# Rota para verificar a tabela
@app.route('/check_db')
def check_db():
    with app.app_context():
        try:
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            
            if 'amv' in tables:
                count = db.session.query(AMV).count()
                return f"✅ Tabela AMV existe! Registros: {count}"
            else:
                return "❌ Tabela AMV não encontrada"
        except Exception as e:
            return f"⚠️ Erro: {str(e)}"

@app.route('/add_example')
def add_example():
    with app.app_context():
        try:
            # Cria um registro de exemplo
            novo_amv = AMV(
                idamv=1,
                tipofuncao="TEST1",
                L1="Exemplo1",
                L2="Exemplo2",
                tower="TorreA"
                # Preencha outros campos conforme necessário
            )
            db.session.add(novo_amv)
            db.session.commit()
            return "✅ Registro inserido com sucesso!"
        except Exception as e:
            return f"❌ Falha ao inserir: {str(e)}"

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
                    # ... (atualize todos os outros campos como no exemplo AMV) ...
                    atualizados += 1
                else:
                    # Cria novo registro
                    novo_registro = Sinais(
                        idSinais=int(linha['idSinais']),
                        tipoAspecto=linha['tipoAspecto'],
                        L1=linha.get('L1'),
                        L2=linha.get('L2'),
                        # ... (adicione todos os outros campos) ...
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
                valor = getattr(registro, coluna.name)
                if valor not in [None, '']:
                    campos[coluna.name] = valor
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
    sinais = ['Sinal-4 LUZ', 'Sinal-6 LUZ', 'Sinal-12 LUZ', 'Sinal-16 LUZ', 'Sinal-20 LUZ', 'Sinal-22LUZ', 'Sinal-28LUZ', 'Sinal-30LUZ', 'Sinal-52LUZ', 'Sinal-54LUZ', 'Sinal-56LUZ', 'Sinal-62 LUZ', 'Sinal-64 LUZ', 'Sinal-66 LUZ', 'Sinal-68 LUZ', 'Sinal-70 LUZ', 'Sinal-72 LUZ', 'Sinal-78 LUZ', 'Sinal-80 LUZ']
    return render_template('sinais.html', sinais=sinais, titulo='Sinais')

@app.route('/logout')
def logout():
    session.pop('logado', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)