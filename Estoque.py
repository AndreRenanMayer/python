#Estoque.py


#crida listas vazias
produtos = []
quantidades = []



def menu():
    opcao = ' '
    while opcao != '0':
        print('###CONTROLE DE ESTOQUE###')
        print('SISTEMA DE CONTROLE VERSÃO 1.0')
        print('DESENVOLVIDO POR: Andre Mayer')
        print('1 = CADASTRAR')
        print('2 = LISTAR')
        print('3 = APAGAR')
        print('0 = SAIR\n')

        opcao = input('Qual opção? ')


        
        if opcao == '0':
            print('Saindo...')
            
        elif opcao == '1':
            cadastrar()
            
        elif opcao == '2':
            listar()

        elif apagar == '3':
            apagar()
        
        else:
            print('Opção Inválida')
            

def cadastrar():
    resp = 'S'
    r = ['S','N']
    while resp == 'S':

        #Pede as variáveis
        nome = input('Digite o item: ').title()

        if nome in produtos:
            print('Produtos já cadastrado')
            continue
        
        quant = int(input('Digite a quantidade: '))

        #Adiciona às listas
        produtos.append(nome)
        quantidades.append(quant)
        produtos

        #Mostra as listas


        resp = input('Quer continuar? (S)im ou (N)ão: ').upper()
        while resp not in r:
            resp = input('Favor digitar uma resposta válida (S)im ou (N)ão: ').upper()

def listar():

    print(produtos)
    print(quantidades)

def apagar():
    nome = input('Nome do produto para apagar do estoque')
    produtos.apagar()
	#continua na próxima aula

menu()
        
