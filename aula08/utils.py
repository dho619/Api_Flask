from models import Pessoas, Usuarios

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

def insereUsuario(login, senha):
    usuario = Usuarios(login=login, senha = senha)
    usuario.save()

def consultaUsuarios():
    usuarios = Usuarios.query.all()
    response = [{'login': u.login, 'senha':u.senha} for u in usuarios]
    return response

if __name__ == '__main__':
    # insere()
    # alterar()
    # excluir()
    # consulta()
    # insereUsuario('rafael', '123')
    print(consultaUsuarios())
