##banco de dados

## python -m pip install --upgrade pip
##cd scripts
## pip3 install PyMySQL

##criar banco escola.db usando sqlitestudio

import pymysql

def ListaDatabase():
    #executa um comando SQL
    cursor.execute('Show Database')

    #Recupera o resultado
    recordtest = cursor.fetchall()
    #mostra o resultado
    for registro in recordser:
        print(record)

if  (__name__=='__main__'):
    #cria conexão com banco de dados
    conexao = pymysql.connect(db='escola', user='root',passwd='')
    #cria um cursor
    cursor = conexao.cursor()
    listaDataBase
