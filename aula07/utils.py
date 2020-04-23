from models import Pessoas

def insere():
    pessoa = Pessoas(nome='Rafael', idade=29)
    pessoa.save()

def consulta():
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome='Sebastian').first()

def alterar():
    pessoa = Pessoas.query.filter_by(nome='Sebastian').first()
    pessoa.nome = 'Sebastian'
    pessoa.save()

def excluir():
    pessoa = Pessoas.query.filter_by(nome='Sebastian').first()
    pessoa.delete()

if __name__ == '__main__':
    insere()
    # alterar()
    # excluir()
    # consulta()
