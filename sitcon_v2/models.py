from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AMV(db.Model):
    __tablename__ = 'amv'
    
    idamv = db.Column(db.Integer, primary_key=True)
    tipofuncao = db.Column(db.String(5), primary_key=True)
    L1 = db.Column(db.String(8), nullable=True)
    L2 = db.Column(db.String(8), nullable=True)
    L3 = db.Column(db.String(8), nullable=True)
    L4 = db.Column(db.String(8), nullable=True)
    L5 = db.Column(db.String(8), nullable=True)
    L6 = db.Column(db.String(8), nullable=True)
    L7 = db.Column(db.String(8), nullable=True)
    L9 = db.Column(db.String(8), nullable=True)
    L10 = db.Column(db.String(8), nullable=True)
    tower = db.Column(db.String(8), nullable=True)
    interface = db.Column(db.String(8), nullable=True)
    L14 = db.Column(db.String(8), nullable=True)
    L15 = db.Column(db.String(8), nullable=True)
    L16 = db.Column(db.String(8), nullable=True)
    L17 = db.Column(db.String(8), nullable=True)
    L18 = db.Column(db.String(8), nullable=True)
    L20 = db.Column(db.String(8), nullable=True)
    L21 = db.Column(db.String(8), nullable=True)
    L22 = db.Column(db.String(8), nullable=True)
    L23 = db.Column(db.String(8), nullable=True)

    def __repr__(self):
        return f'<AMV idamv={self.idamv}, tipofuncao={self.tipofuncao}>'
    
class Sinais(db.Model):
    __tablename__ = 'sinais'
    
    idSinais = db.Column(db.Integer, primary_key=True)
    tipoAspecto = db.Column(db.String(5), primary_key=True)
    L1 = db.Column(db.String(8), nullable=True)
    L2 = db.Column(db.String(8), nullable=True)
    L3 = db.Column(db.String(8), nullable=True)
    L4 = db.Column(db.String(8), nullable=True)
    L5 = db.Column(db.String(8), nullable=True)
    L6 = db.Column(db.String(8), nullable=True)
    L7 = db.Column(db.String(8), nullable=True)
    L8 = db.Column(db.String(8), nullable=True)
    L10 = db.Column(db.String(8), nullable=True)
    tower = db.Column(db.String(8), nullable=True)
    interface = db.Column(db.String(8), nullable=True)
    L14 = db.Column(db.String(8), nullable=True)
    L15 = db.Column(db.String(8), nullable=True)
    L16 = db.Column(db.String(8), nullable=True)
    L18 = db.Column(db.String(8), nullable=True)
    L19 = db.Column(db.String(8), nullable=True)
    L20 = db.Column(db.String(8), nullable=True)
    L21 = db.Column(db.String(8), nullable=True)
    L22 = db.Column(db.String(8), nullable=True)
    L23 = db.Column(db.String(8), nullable=True)

    def __repr__(self):
        return f"<Sinais idSinais={self.idSinais}, tipoAspecto={self.tipoAspecto}>"
    
class MatriculasValidas(db.Model):
    """Tabela com as matrículas que podem se cadastrar"""
    __tablename__ = 'matriculas_validas'
    matricula = db.Column(db.String(20), primary_key=True)

class Usuario(db.Model):
    """Tabela de usuários cadastrados"""
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.String(20), unique=True, nullable=False)
    login = db.Column(db.String(50), unique=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(128), nullable=False)


class CDV(db.Model):
    __tablename__ = 'cdv'
    

    idcdv = db.Column(db.String(5), primary_key=True)
    tipo = db.Column(db.String(6), primary_key=True)
    L1 = db.Column(db.String(8), nullable=True)
    L2 = db.Column(db.String(8), nullable=True)
    L3 = db.Column(db.String(8), nullable=True)
    L4 = db.Column(db.String(8), nullable=True)
    L5 = db.Column(db.String(8), nullable=True)
    L6 = db.Column(db.String(8), nullable=True)
    L7 = db.Column(db.String(8), nullable=True)
    L8 = db.Column(db.String(8), nullable=True)
    L9 = db.Column(db.String(8), nullable=True)
    L10 = db.Column(db.String(8), nullable=True)
    tower = db.Column(db.String(8), nullable=True)
    interface = db.Column(db.String(8), nullable=True)
    L14 = db.Column(db.String(8), nullable=True)
    L15 = db.Column(db.String(8), nullable=True)
    L16 = db.Column(db.String(8), nullable=True)
    L18 = db.Column(db.String(8), nullable=True)
    L17 = db.Column(db.String(8), nullable=True)
    L20 = db.Column(db.String(8), nullable=True)
    L21 = db.Column(db.String(8), nullable=True)
    L22 = db.Column(db.String(8), nullable=True)
    L23 = db.Column(db.String(8), nullable=True)

    def __repr__(self):
        return f'<CDV idcdv={self.idcdv}, tipo={self.tipo}>'