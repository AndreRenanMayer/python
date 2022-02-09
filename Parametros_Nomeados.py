#parametros_nomeados.py

def mensagem(tipo = 'Mensagem',msg = 'Bom dia'):
    print(f'{tipo}: {msg}')

mensagem(tipo = 'Alerta')
mensagem(msg='Bom tarde')
mensagem(msg='Bom noite', tipo='Alerta')

##Parametro nomeado dentro do print end=\n

print(1)
print(2)
print(3)
print(1,end='')
print(2,end='')
print(3,end='\n')
print(1,end='\n\n')
print(2,end='\n\n')
print(3,end='\n\n')

