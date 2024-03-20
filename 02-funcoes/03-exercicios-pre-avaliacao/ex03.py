'''
Ex03 - Contador de Vogais e Consoantes: Peça ao usuário para digitar uma frase e retorne o número de vogais e consoantes na frase.
'''
import unicodedata

vogal=0
consoante=0
frase = unicodedata.normalize('NFKD', input('Escreva uma frase:').lower()).encode('ASCII', 'ignore').decode('ASCII')

for i in frase:
    if i in 'aeiou':
        vogal+=1
    else:
        consoante+=1   

print('Número de vogais:', vogal)
print('Número de consoantes', consoante)