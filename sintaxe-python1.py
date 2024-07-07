#Manipubando Strings

frase = ('123456789')
print(frase[0:9:2]) #Do primeiro ao último a cada duas posições de caracteres.
print(frase[-1]) #Mostra último digito 'variavel[-1]'
print (len(frase)) #'len()' função para mostrar quantos caracteres há na variável.
print(frase.count('3')) #'frase.count()' conta e verifica caracteres específicos de uma variável na lista.
print(frase.find('4')) #Mostra em que posição está o valor solicitado.


frase2 = ('Eu estive lá.')
print (frase2.replace('estive','estarei'))
print (frase2.upper()) #Oposto 'frase.lower()'


frase3 = ('   Fui e não voltei mais!   ')
print (frase3.strip())
#corte dos espaços desnecessários do início e fim dos textos.
#var.rstrip() - da direita
#var.lstrip() - da esquerda
print (frase3.split())
#Função de separarar str pelos seus espaços.


nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome é diego? {}'.format('diego' in nome.lower()))
#Operador do 'IN' verifica o que está dentro da variável.
#'.lower()' para aceitar diferentes camels.

nome2 = str (input('Digite seu nome completo: ')) .split()
print ('Seu primeiro nome é {} \nE o último {}.'.format(nome2[0], nome2[-1])) #Os caracteres separados pelos espaços entre si se tornam valores.
