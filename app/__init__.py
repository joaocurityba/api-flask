from flask import Flask, render_template
from .tarefas.tarefas import tarefas_bp
from models import db


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'


db.init_app(app)


app.register_blueprint(tarefas_bp)


@app.route('/')
def index():
    return render_template('index.html')
