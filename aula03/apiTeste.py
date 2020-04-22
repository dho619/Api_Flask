from flask import Flask, jsonify, request
import  json

app = Flask(__name__) #mostra a quem pertence

@app.route('/pessoas/<int:id>') # criando a rota, <int:id> um parametro inteiro, pode clk apenas id, mas ai ele vai ser string
def pessoas(id):#a funcao executada ao chamar a rota
    return jsonify({#jsonify e para retornar json
                    'id': id,
                    'nome': 'João das Neves',
                    'idade': 20
                    })

#RECEBENDO VARIOS PARAMETRO PELO URI
# @app.route('/soma/<int:v1>/<int:v2>')
# def soma(v1, v2):
#     return jsonify({
#         'result': v1+v2
#     })

@app.route('/soma', methods=['POST', 'GET'])
def soma():
    if request.method == 'GET': #verificar o tipo do metodo
        return('hmmmm, isso é GET')
    dados = json.loads(request.data)#transforma string em formato json em json e request.data e o body da requisicao
    return jsonify({
        'result': sum(dados['valores'])
    })

if __name__ == '__main__':#verificar que e o proprio main que esta chamando a funcao, e uma boa pratica
    app.run(debug=True)#debug=True funcionara tipo o nodemon
