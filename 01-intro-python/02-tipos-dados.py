#1. Números

#int
idade = 17

#float
altura = 1.65

#complex
#cálculos com números complexos
numero_complexo = 1 + 2j

#2. Boolean
#primeira letra maiuscula
verdade = True
menira = False

#3. Sequências
#str, list, tuple

#str e "char"
nome = "Bell"
nome = "B"

#str de multiplas linhas
frase="""
Parabéns! Parabéns!
saúde...felicidade!!!
"""
#interpolação de str
nome="Bell"
idade=22
mensagem=f'{nome} é uma ovelha! ele tem {idade} anos'

#Como acessar os caracteres de uma str?
nome = "Bell"
print(nome[1])

#Métodos de str
print(nome.upper())
print(nome.capitalize())
print(nome)

#list
#lista de valores
#permite diferentes tipos de dados na mesma lista

perfil = ['Bell', 'ovelha', 'jardineiro', 22]
print(perfil[2]) 

#printar tudo da lista
for perfils in perfil:
    print(perfils)

#adiciona no final da lista
perfil.append('deprimido')

#adiciona em uma posição
perfil.insert(1,"bobo")

#remover
perfil.remove('bobo')

#tuple
#"lista" de valores que não pode ser alterada

cozinhar=('bolo', 'torta', 'macaron')

def estatistica_notas(notas):
    maior=max(notas)
    menor=min(notas)
    media=sum(notas)/len(notas)
    return maior,menor,media

notas=[10, 3.5, 7.8, 6.7]

estatistica=estatistica_notas(notas)
print(estatistica)

# desempacotar uma tupla
maior,menor,media=estatistica_notas(notas)
print(maior,menor,media)

#set
#conjunto de valores não indexado que não permite duplicados

habilidades={'java', 'python'}
habilidades.add('bababoey')

#dict
#palavra->definição
#key->value

formiga = {
    'nome':'Myrmica',
    'profissao':"contadora",
    'idade':25,
    'altura':1.45
}

print(formiga['nome'])
print(formiga['profissao'])
print(formiga['idade'])
print(formiga['altura'])

#None
#vairaveis que serão inicializadas em tempo de execução
#retorno de função

nulo=None