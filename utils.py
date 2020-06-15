from models import Pessoas, Usuarios


# Consulta dados na tabela pessoa
def consulta_pessoa():
    pessoa = Pessoas.query.all()
    print(pessoa)
    # pessoa = Pessoas.query.filter_by(nome='Isabela')
    # for p in pessoa:
    # print(p)
    # pessoa = Pessoas.query.filter_by(nome='Isabela').first()
    # print(pessoa.idade)


# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Luiz', idade=22)
    print(pessoa)
    pessoa.save()


# Atualiza dados na tabela pessoa
def altera_pessoa():
    # pessoa = Pessoas.query.filter_by(nome='Isabela').first()
    # pessoa.idade = 31
    pessoa = Pessoas.query.filter_by(nome='Oliveira').first()
    pessoa.nome = 'Marco Antonio'
    pessoa.save()


# Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Marco Antonio').first()
    pessoa.delete()


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consulta_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    # insere_pessoas()
    # altera_pessoa()
    # exclui_pessoa()
    # consulta_pessoa()
    # insere_usuario('jorge', '1234')
    # insere_usuario('ana', '1234')
    # insere_usuario('arthur', '1234')
    consulta_usuarios()
