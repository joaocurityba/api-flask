from flask import Blueprint, request, jsonify, Response
from models import db, Tarefa
import json


tarefas_bp = Blueprint('tarefas', __name__, template_folder='templates')


@tarefas_bp.route('/api/tarefas/', methods=['GET', 'POST'])
def get_tarefas():
    if request.method == 'POST':
        nome = request.json['nome']
        descricao = request.json['descricao']
        new_task = Tarefa(nome=nome, descricao=descricao)
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'message': 'Tarefa criada com sucesso!'}), 201
    all_tasks = Tarefa.query.all()
    tasks_list = [{'id': task.id, 'nome': task.nome} for task in all_tasks]
    response = Response(json.dumps(tasks_list, ensure_ascii=False), content_type='application/json; charset=utf-8')
    return response, 200


@tarefas_bp.route('/api/tarefas/<int:id>/', methods=['GET'])
def get_tarefas_id(id):
    tarefa = Tarefa.query.get(id)
    if tarefa:
        tarefa_dict =  [{'id': tarefa.id, 'nome': tarefa.nome, 'descricao': tarefa.descricao}]
        response = Response(json.dumps(tarefa_dict, ensure_ascii=False), content_type='application/json; charset=utf-8')
        return response, 200
    return jsonify({'message': 'Tarefa não encontrada'}), 404


@tarefas_bp.route('/api/tarefas/<int:id>/', methods=['DELETE'])
def delete_tarefas(id):
    tarefa = Tarefa.query.get(id)
    if tarefa:
        db.session.delete(tarefa)
        db.session.commit()
        return jsonify({'message': 'Tarefa deletada com sucesso!'}), 201
    return jsonify({'message': 'Tarefa não encontrada'}), 404


@tarefas_bp.route('/api/tarefas/<int:id>/', methods=['PUT'])
def update_tarefas(id):
    tarefa = Tarefa.query.get(id)
    if tarefa:
        tarefa.nome = request.json['nome']
        tarefa.descricao = request.json['descricao']
        db.session.commit()
        return jsonify({'message': 'Tarefa alterada com sucesso!'}), 200
    return jsonify({'message': 'Tarefa não encontrada'}), 404
