'''
Ex05 - Verificador de Palíndromos: 
Solicite ao usuário que digite uma palavra ou frase e verifique se é um palíndromo (ou seja, pode ser lida de frente para trás e de trás para frente da mesma forma).
'''
def ehpalindromo(str):
    reverso = ''.join(reversed(str))
    if (str == reverso):
        return True
    return False

palavra = input('Escreva uma palavra ou frase:')
resultado = ehpalindromo(palavra)
if resultado:
    print('É um palíndromo')
else:
    print('Não é um palindromo')