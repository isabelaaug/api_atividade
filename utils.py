from models import Pessoas


# GET na tabela pessoa
def consulta_pessoa():
    pessoa = Pessoas.query.all()
    print(pessoa)
    # pessoa = Pessoas.query.filter_by(nome='Isabela')
    # for p in pessoa:
    # print(p)
    # pessoa = Pessoas.query.filter_by(nome='Isabela').first()
    # print(pessoa.idade)


# POST na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Luiz', idade=22)
    print(pessoa)
    pessoa.save()


# PUT na tabela pessoa
def altera_pessoa():
    # pessoa = Pessoas.query.filter_by(nome='Isabela').first()
    # pessoa.idade = 31
    pessoa = Pessoas.query.filter_by(nome='Oliveira').first()
    pessoa.nome = 'Marco Antonio'
    pessoa.save()


# DELETE na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Marco Antonio').first()
    pessoa.delete()


if __name__ == '__main__':
    # insere_pessoas()
    # altera_pessoa()
    exclui_pessoa()
    consulta_pessoa()
