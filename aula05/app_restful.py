from flask import Flask, request
from flask_restful import Resource, Api
import json

from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id': 0,
        'nome': 'João das Neves',
        'habilidades': ['Python', 'Flask']
    },
    {
        'id': 1,
        'nome': 'Arya Stark',
        'habilidades': ['JavaScript', 'Node']
    }
]

class Dev(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'error',
                        'mensage': 'Não Existe o ID'}
        except Exception:
            response = {'status': 'error',
                        'mensage': 'Erro desconhecido'}
        return response
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucess', 'mensage': 'Excluido'}

class ListaDevs(Resource):
    def get(self):
        return desenvolvedores
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return({'status': 'sucess', 'mensage': 'Inserido', 'id': posicao})


api.add_resource(Dev, '/dev/<int:id>')
api.add_resource(ListaDevs, '/dev')
api.add_resource(Habilidades, '/hab')

if __name__ == '__main__':
    app.run(debug=True)
