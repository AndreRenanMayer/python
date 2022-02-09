##arquivo_texto.py

#modo para leitura e gravação de arquivos: 'r', 'w', 'a'
# r = read = somente leitura
# w = write = escrita (perde o que já existe no programa)
# a = append = anexa dados (não perde)

# tipos de arduivos: texto ou binário]

lista = []
def entrada():
    quant = int(input('Quantas frutas você quer digitar?'))
    for x in range (0,quant):
        fruta = input(f'Digite a fruta {x}: ')
        lista.append(fruta)
    print(lista)

def gravar():
    arquivo = open('frutas.txt', 'w')
    for fruta in lista:
        arquivo.write(fruta + '\n')
        
    arquivo.close()

def ler():
    arquivo=open('frutas.txt', 'r')
    for linha in arquivo:
        print(linha)

    arquivo.close()

def anexar():
    arquivo=open('frutas.txt','a')
    for fruta in lista:
        arquivo.write(fruta + '\n')
    arquivo.close()

if(__name__=='__main__'):
    entrada()
    #gravar()
    
    anexar()
    ler()
        
