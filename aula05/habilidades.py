from flask_restful import Resource

habilidades = ['Python', 'Flask', 'Node', 'JavaScript']

class Habilidades(Resource):
    def get(self):
        return habilidades
