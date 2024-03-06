# if, if/else, if,elif,else, ternario, match

#if
#if condicao:
#   corpo
#   corpo

idade = 20
if idade>=18:
    print('lepo')
    print('oohhhlepo lepoooo')
else:
    print('nada de lepo')

print('agora acabou')

#criança (0-12), adolescente (13-17), adulto(18-59), velho(60+)

if idade<=12:
    print('kid do caralho')
elif idade<=17:
    print('adoles')
elif idade<=59:
    print('adult')
else:
    print('idoso')


# if aninhado (EVITAR)

email = 'bellovelha@email.com'
senha = 'amograma'

if email == 'bellovelha@email.com':
    if senha == 'amograma':
        print('Acesso liberado')
    else:
        print('Email ou senha incorretos')
else:
    print('Email ou senha incorretos')

#uma solução para esse if aninhado feio

if email=='bellovelha@email.com' and senha=='amograma':
    print('Acesso liberado')
else:
    print('voce nao eh o bell vai embora!!!')


# condição complexa no if
#permitir a entrada se o usuario não estiver bloqueado e se for um funcionario e se a hora atual é entre 8h a 18h ou o usuario é adm

#exemplo ruim
usuario_bloqueado= False
usuario_funcionario = True
horario_atual = 19
usuario_admin = False

if (not usuario_bloqueado and usuario_funcionario and horario_atual>=8 and horario_atual<=18)or usuario_admin:
    print("liberado")
else:
    print("vai embora!")

# exemplo bom

horario_comercial = horario_atual>=8 and horario_atual<=18
usuario_ativo = usuario_funcionario and not usuario_bloqueado
liberado = (usuario_ativo and horario_comercial) or usuario_admin

if liberado:
    print("eba!!")
else:
    print("vai embora")

#entrada: hora_atual
# saida: hora_atual está dentro do horário comercial (bool)

def dentro_horario_comercial (hora_atual):
    return hora_atual >=8 and hora_atual <= 18

#operador ternario
if idade>=18:
    status = 'maior'
else:
    status = 'menor'
status = 'maior' if idade>=18 else 'menor'

#usuario passa o dia (int) devolve string nome
# 1-segunda, 2-terça, etc
#match
#python 3.10
# 'switch case' mais poderoso

dia =4

match dia:
    case 1| 7:
        print('Fim de semana')
    case 2|3|4|5|6:
        print('dia útil')
    case _:
        print('inválido')