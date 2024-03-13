# Ex01 - Escreva um programa em Python que solicita ao usuário um número inteiro e apresenta seu antecessor e sucessor.
num = int(input('Escreva um numero inteiro:'))
print(f'Antecessor: {num-1} Sucessor: {num+1}')

# Ex02 - Escreva um programa em Python que solicita ao usuário três números e apresenta a média aritmética dos números informados.
num1 = float(input('Escreva o numero 1:')) 
num2 = float(input('Escreva o numero 2:')) 
num3 = float(input('Escreva o numero 3:')) 
media= (num1+num2+num3)/3
print(media)


# Ex03 - Crie um programa em Python que recebe como entrada o valor de uma compra e apresenta como saída o valor final com desconto e o desconto aplicado com base nas seguintes regras:

#    Compras entre R$ 0,01 e R$ 9,99 - 0% de desconto
#    Compras entre R$ 10,00 e R$ 99,99 - 5% de desconto
#   Compras entre R$ 100,00 e R$ 499,99 - 10% de desconto
#   Compras iguais ou superiores a R$ 500,00 - 15% de desconto

preco = float(input('valor da compra:'))
if preco>=0.01 and preco<=9.99:
    desconto = 0
elif preco>=10.00 and preco<=99.99:
    desconto = 5
    preco = preco-preco*0.05
elif preco>=100.00 and preco<=499.99:
    desconto = 10
    preco = preco-preco*0.1
elif preco>=500.00:
    desconto= 15
    preco = preco-preco*0.15
    
print (f'Preco: {preco} Desconto {desconto}%')

#Ex04 - O código identificador de funcionários de uma empresa contém 7 caracteres, inicia com a sequência de caracteres BR, em seguida apresenta um número inteiro entre 0001 e 9999 e finaliza com o caractere X.

#Exemplos válidos:

#    BR0001X
#    BR1236X
#    BR9999X

#Exemplos inválidos:

#    br0001X
#   BR126X
#   BR99999X
#    BR9999Y
    
#Crie uma função em Python que implementa essa verificação

cod = input('Insira o código:')
def verificacao(cod):
    if cod[0] == 'B' and cod[1] == 'R' and isinstance(cod[2]) and isinstance(cod[3], int) and isinstance(cod[3], int) and isinstance(cod[4], int) and isinstance(cod[5], int) and cod[0] == 'X':
        return True
    else:
        return False
        
print(verificacao(cod))

#Ex05 - Crie um programa em Python que solicita ao usuário um identificador e apresenta se o que foi informado é um valor válido ou inválido. 

#Ex06. Crie um programa em Python que recebe como entrada o comprimento, altura e a largura de um aquário e calcule as seguintes informações.

#    O volume do aquário em litros;
#    A potência do termostato necessária para manter a temperatura adequada dentro do aquário;
#    A quantidade em litros de filtragem por hora necessária para manter a qualidade da água.
#    Volume é dado por (comprimento * altura * largura) / 1000
#    A potência do termostato depende do tamanho do aquário e da temperatura ambiente. Para o cálculo utilizar a fórmula: potencia = volume * 0,05 * (temperatura desejada - temperatura ambiente)
#    A quantidade de filtragem por hora deve ser no mínimo 2 a 3 vezes o volume do aquário.

#Utilize funções.

#Ex07. Utilizando as diretrizes de Índice de Massa Corporal (IMC) da Organização Mundial de Saúde (OMS), crie uma calculadora em Python que solicita ao usuário seu peso (Kg) e sua altura (m) e apresenta em qual classificação o indivíduo se encaixa. Além disso, o programa deve apresentar quanto o indivíduo precisa perder ou ganhar de peso para chegar no peso normal (imc = 24,9).

#IMC = peso / altura * altura

#Classificação
#----------------------------------
#IMC           Classificação
#-----------------------------------
#< 18,5         Baixo peso
#18,5 a 24,9     Peso normal
#25,0 a 29,9     Excesso de peso
#30,0 a 34,9     Obesidade de Classe 1
#35,0 a 39,9     Obesidade de Classe 2
#>= 40,00      Obesidade de Classe 3

#Utilize funções.