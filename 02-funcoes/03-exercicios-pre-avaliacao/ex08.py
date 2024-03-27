'''
Ex08 - Função de Contagem de Palavras: 
Escreva uma função que receba uma string (frase) como argumento e retorne um dicionário 
onde as chaves são as palavras únicas no texto e os valores são o número de vezes que cada palavra aparece no texto. 
Depois, teste a função com diferentes textos fornecidos pelo usuário. 
'''
import re

frase = input("Digite a frase: ")
frase = re.sub(r'[^\w\s]', '', frase).split()


dicionario = {}

for palavra in frase:
    if palavra in dicionario:
        dicionario[palavra] += 1
    else:
        dicionario[palavra] = 1

print("Dicionário de contagem de palavras:")
print(dicionario)