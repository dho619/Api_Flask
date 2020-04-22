from flask import Flask, jsonify, request
import json

app = Flask(__name__)

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

@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'error',
                        'mensage': 'Não Existe o ID'}
        except Exception:
            response = {'status': 'error',
                        'mensage': 'Erro desconhecido'}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucess', 'mensage': 'Excluido'})

@app.route('/dev', methods=['POST', 'GET'])
def lista_devs():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return(jsonify({'status': 'sucess', 'mensage': 'Inserido', 'id': posicao}))
    if request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)
