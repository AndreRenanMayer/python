##aquivo_CSV.py

#Permite gravar e ler arquivos .csv do Excel

#Gravando um arquivo .csv

import csv

def gravar():
    tabela=(('PRODUTO','UNIDADE','PREÇO UNITÁRIO','QUANTIDADE ESTOQUE','VALOR TOTAL'),
            ('Açúcar','2kg', 3.59, 10, 35.90),
            ('Biscoito','200gr',1.19,10,11.90)
            )
    # a objeto de escrita
    saida = csv.writer(open('tabela.csv','w',newline=''), delimiter = ';')

    #escreve as tuplas no arquivo de saida
    saida.writerows(tabela)

#Lendo .csv
def ler():
    tabela = csv.reader(open('tabela.csv','r'))

    for lista in tabela:
        print(lista[0].split(';'))
        
        
    

if(__name__=='__main__'):
    #gravar()
    ler()
