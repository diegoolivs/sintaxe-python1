#Embaralhando lista
from random import shuffle #importação direta de 'shuffle'(enbaralhar) de random.
n1 = str(input('Primeiro agente: '))
n2 = str(input('Segundo agente: '))
n3 = str(input('Terceiro agente: '))
n4 = str(input('Quarto agente: '))
lista = [n1,n2,n3,n4] #criação simples de um array de valores str.
shuffle(lista) #função de embaralhar a ordem dos valores.
print('A ordem agora é: ')
print(lista) #Nova ordem após a alteração.