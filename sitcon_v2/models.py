from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AMV(db.Model):
    __tablename__ = 'amv'
    
    # Chave primária composta (como no MySQL)
    idamv = db.Column(db.Integer, primary_key=True)
    tipofuncao = db.Column(db.String(5), primary_key=True)
    
    # Todas as colunas exatamente como na tabela MySQL
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