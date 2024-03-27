'''
Ex07 - Jogo da Forca: Implemente uma versão simples do jogo da forca. 
O programa começa com uma palavra oculta (o usuário não vê) e o usuário tenta adivinhar a palavra, letra por letra. 
O usuário tem um número limitado de tentativas para adivinhar toda a palavra.
'''

import random

def escolher_palavra():
    palavras = ['latorre', 'luk cho man', 'quirino', 'motta', 'ugo', 'claudete']
    return random.choice(palavras)

def mostrar_palavra_oculta(palavra, letras_descobertas):
    palavra_mostrada = ''
    for letra in palavra:
        if letra in letras_descobertas:
            palavra_mostrada += letra
        else:
            palavra_mostrada += '_'
    return palavra_mostrada

def jogo_da_forca():
    palavra = escolher_palavra()
    letras_descobertas = []
    tentativas_restantes = 6

    print("Bem-vindo ao jogo da forca de professores do IFSP!")
    print("Adivinhe o professor secreto. Você tem 6 tentativas.")

    while tentativas_restantes > 0:
        palavra_mostrada = mostrar_palavra_oculta(palavra, letras_descobertas)
        print(f"Palavra: {palavra_mostrada}")
        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite apenas uma letra válida.")
            continue

        if letra in letras_descobertas:
            print("Essa letra já tinha sido escolhida....")
            continue

        letras_descobertas.append(letra)

        if letra not in palavra:
            tentativas_restantes -= 1
            print(f"Letra '{letra}' não encontrada no nome. Tentativas restantes: {tentativas_restantes}")

        if '_' not in mostrar_palavra_oculta(palavra, letras_descobertas):
            print(f"Parabéns! Você adivinhou o professor '{palavra}' corretamente.")
            break

    if tentativas_restantes == 0:
        print(f"Você esgotou suas tentativas. O professor era '{palavra}'.")

jogo_da_forca()
