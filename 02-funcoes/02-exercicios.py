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

def verificacao(cod: str):

    if len(cod) != 7:
        return False
    elif not f"{cod[0]}{cod[1]}" == "BR":
        return False
    elif not int(cod[2:6]):
        return False 
    if not cod[6] == "X":
        return False
    return True


#Ex05 - Crie um programa em Python que solicita ao usuário um identificador e apresenta se o que foi informado é um valor válido ou inválido. 
cod = input('Insira o código: ')

if verificacao(cod):
    print("O código informado é válido.")
else:
    print("O código informado é inválido.")

#Ex06. Crie um programa em Python que recebe como entrada o comprimento, altura e a largura de um aquário e calcule as seguintes informações.

#    O volume do aquário em litros;
#    A potência do termostato necessária para manter a temperatura adequada dentro do aquário;
#    A quantidade em litros de filtragem por hora necessária para manter a qualidade da água.
#    Volume é dado por (comprimento * altura * largura) / 1000
#    A potência do termostato depende do tamanho do aquário e da temperatura ambiente. Para o cálculo utilizar a fórmula: potencia = volume * 0,05 * (temperatura desejada - temperatura ambiente)
#    A quantidade de filtragem por hora deve ser no mínimo 2 a 3 vezes o volume do aquário.

#Utilize funções.

def calcular_volume(comprimento, altura, largura):
    return (comprimento * altura * largura) / 1000

def calcular_potencia_termostato(volume, temperatura_desejada, temperatura_ambiente):
    return volume * 0.05 * (temperatura_desejada - temperatura_ambiente)

def calcular_filtragem_por_hora(volume):
    return volume * 2  


comprimento = float(input("Digite o comprimento do aquário em centímetros: "))
altura = float(input("Digite a altura do aquário em centímetros: "))
largura = float(input("Digite a largura do aquário em centímetros: "))
temperatura_desejada = float(input("Digite a temperatura desejada em graus Celsius: "))
temperatura_ambiente = float(input("Digite a temperatura ambiente em graus Celsius: "))

volume = calcular_volume(comprimento, altura, largura)
potencia_termostato = calcular_potencia_termostato(volume, temperatura_desejada, temperatura_ambiente)
filtragem_por_hora = calcular_filtragem_por_hora(volume)

print(f"Volume do aquário: {volume} litros")
print(f"Potência do termostato necessária: {potencia_termostato} watts")
print(f"Quantidade de filtragem por hora necessária: {filtragem_por_hora} litros/hora")


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

peso_normal =0
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif imc >= 18.5 and imc <= 24.9:
        return "Peso normal"
    elif imc >= 25.0 and imc <= 29.9:
        return "Excesso de peso"
    elif imc >= 30.0 and imc <= 34.9:
        return "Obesidade de Classe 1"
    elif imc >= 35.0 and imc <= 39.9:
        return "Obesidade de Classe 2"
    else:
        return "Obesidade de Classe 3"

def diferenca_peso_normal(peso, altura):
    imc_normal = 24.9
    peso_normal = imc_normal * (altura ** 2)
    diferenca = abs(peso - peso_normal)
    return diferenca

peso = float(input("Digite o seu peso em Kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)
diferenca_peso = diferenca_peso_normal(peso, altura)

print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
print(f"Você precisa {'ganhar' if peso < peso_normal else 'perder'} {diferenca_peso:.2f} Kg para atingir o peso normal.")

