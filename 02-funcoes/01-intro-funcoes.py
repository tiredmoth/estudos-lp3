# função
# modularizar o programa
# reuso/manutenabilidade

#olha que coisa ruim
hora_atual= 12
if hora_atual >= 8 and hora_atual <= 18:
    print ('PERMITIDO O ACESSO')

# função que facilita as coisas
def dentro_horario_comercial(hora):
    return hora_atual >= 8 and hora_atual <= 18

# declaração
# def nome_funcao():
#      corpo da funcao

# função sem retorno
#side effect: função não retorna nada

def diga_lepo(nome):
    print(f"lepo {nome}!")
    
diga_lepo('Bell')

#melhor
#função pura

def diga_lepo2(nome):
    return f"lepo {nome}!"

nome = 'Yniphora'
print(diga_lepo2(nome))
    

# parâmetro e argumentos

def somar(numero1, numero2):
    return numero1 + numero2

somar (10.0, 5.0)

#escopo de variaveis

#variavel local
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    return media

#variavel global
media = 0.0
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    return media

# parãmetros com o valor padrão (default)
def boas_vindas(nome , mensagem="Bom dia"):
    return f"{mensagem}, {nome}"

print(boas_vindas('Bell'))

# argumentos nomeados
print(boas_vindas(nome='Mori'))

