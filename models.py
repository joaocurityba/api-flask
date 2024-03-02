from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    descricao = db.Column(db.String(120), nullable=True)
