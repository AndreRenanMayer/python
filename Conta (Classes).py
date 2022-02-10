#conta.py

class Conta():

    #numero
    #titular
    #saldo
    #limite
    #construtor de classe

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    def depositar(self,valor):
        self.__saldo += valor
    def sacar(self,valor):
        if (self.__saldo + self.__limite) >= valor:
            self.__saldo -= valor
            print(f'Você sacou {valor}, seu saldo atual é {self.__saldo}')
            return True
        else:
            print('Não há valor suficiente para sacar')
            return False

    def transferir (self, valor, destino):
        
        if self.sacar(valor):
            destino.depositar(valor)
        else:
            print('Saldo insuficiente')

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @property
    def numero(self):
        return self.__numero

    @limite.setter
    def limite(self, limite):
        self.__limite=limite

    #exemplo de método estático

    @staticmethod
    def codigo_banco():
        return '001'
        
ContaJoao = Conta(123, 'João da Silva', 100,1000)
ContaZe = Conta(456,'José da Silva',100,1000)


print (Conta.codigo_banco())
