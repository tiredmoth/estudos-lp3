'''
Ex04 - Simulador de Eleições: Crie um programa que simule uma votação com três candidatos. 
O programa deve pedir ao usuário para votar várias vezes e, no final, mostrar o número de votos de cada candidato e quem foi o vencedor. 
'''
import random

print('Bem vindo a votação para o novo prefeito! Você tem cinco votos.')
print('Nossos candidatos são:')
print('1- Bell, a ovelha')
print('2- Kitzi, a raposa')
print('3- Mori, a mariposa')

candidato1 = ['Bell', 0]
candidato2 = ['Kitzi', 0]
candidato3 = ['Mori', 0]


num_votos = random.randint(1,10)

while num_votos> 0:
    print('Votos restando:', num_votos)
    voto = int(input('Escreva seu voto:'))
    if voto==1:
         candidato1[1]+=1
         num_votos-=1
    elif voto==2:
        candidato2[1]+=1
        num_votos-=1
    elif voto==3:
        candidato3[1]+=1
        num_votos-=1
    else:
        print('Voto inválido')

def resultado(x, y, z):
    if (x >= y) and (x >= z):
        vencedor= x
    elif (y >= x) and (y >= z):
        vencedor = y
    else:
        vencedor = z
    if vencedor in candidato1:
        return candidato1[0]
    if vencedor in candidato2:
        return candidato2[0]
    if vencedor in candidato3:
        return candidato3[0]

print('Resultados da eleição:')
print('Votos para o Bell:', candidato1[1])
print('Votos para a Kitzi:', candidato2[1])
print('Votos para a Mori:', candidato3[1])
print('Vencedor:', resultado(candidato1[1], candidato2[1], candidato3[1]))