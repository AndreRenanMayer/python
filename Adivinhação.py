#adivinhação.py
import random

def jogar():
    print('********************************')
    print('Bem Vindo ao Jogo de Adivinhação')
    print('********************************')

    numero_secreto=random.randrange(1,101)
    total_tentativas = 0
    pontos = 1000
    print('Qual o nivel de dificuldade?')
    print('(1) Facil (2) Médio (3) Difícil (4) Morte Subita')

    nivel = int(input('Defina o nível: '))

    if nivel == 1:
        total_tentativas=20
    elif nivel ==2:
        total_tentativas=10
    elif nivel ==3:
        total_tentativas=5
    else:
        total_tentativas=3
                
    #print(numero_secreto)

    for tentativa in range (1, total_tentativas +1):
        print(f'Tentativa {tentativa} de {total_tentativas}')
        chute= int(input('Digite um Número entre 1 e 100: '))

        if chute == numero_secreto:
            print('#####Acertou#####')
            break

        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if chute > numero_secreto:
                print('Seu chute foi maior que o número secreto')
            else:
                print('Seu chute foi menor que o número secreto')
                
    print('Fim de Jogo')
    print(f'O número secreto era {numero_secreto}. Você fez {pontos} pontos')

if(__name__=='__main__'):
    jogar()
