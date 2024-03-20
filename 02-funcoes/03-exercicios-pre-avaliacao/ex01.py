'''
Ex01 - Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente. 
Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número.
'''
import random

numero = random.randint(1,100)
acertou = False

while acertou == False:
    guess = int(input('Escreva um numero inteiro:'))
    if guess==numero:
        print('Acertou')
        acertou = True
    elif guess<numero:
        print('Maior')  
    else:
        print('Menor')  