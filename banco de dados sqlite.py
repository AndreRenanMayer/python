#banco de dados sqlite.py

import sqlite3
conexao = sqlite3.connect('escola.db')

#cria um cursor
cursor = conexao.cursor()

def criarTabela():
    sql = 'CREATE TABLE if not exists aluno('\
          'id integer primary key,'\
          'nome varchar(100),'\
          'email varchar(100),'\
          'telefone varchar(14))'

    #cria a tabela
    cursor.execute(sql)

def inserirdados():
    #comando sql
    sql = 'INSERT INTO aluno VALUES (?,?,?,?)'


    #dados
    recset = [
                (1, 'joão da silva','joao@gmail.com','(42)99964-4785'),
                (2, 'Maria Silva','maria@gmail.com','(42)99977-4755'),
                (3, 'Luiz Carlos','luiz@ig.com','(42)99975-3781')
                
                ]
    #insere os dados na tabela
    for rec in recset:
        cursor.execute(sql,rec)

    #confirma a transação
        conexao.commit()
def listarDados():
    #seleciona todos os registros da tabela aluno
    cursor.execute('select * from aluno')

    #recupera os resultados
    recset = cursor.fetchall()

    #mostra na tela
    for rec in recset:
        print('ID: %d \t Nome: %-20s \t Email:%-18s \t Telefone:%-20s' % rec)
    #fecha conexão co banco
        conexao.close()
#programa principal
if(__name__=='__main__'):
    #criarTabela()
    #inserirdados()
    listarDados()
