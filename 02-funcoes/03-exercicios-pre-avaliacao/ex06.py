'''
Ex06 - Conversor de Notas Escolares: 
Baseado em uma pontuação fornecida pelo usuário (0 a 100), 
converta para o sistema de notas A, B, C, D, ou F, seguindo os padrões de conversão comuns.
'''

def converter_nota(pontuacao):
    if pontuacao > 100 or pontuacao < 0:
        return 'Pontuação inválida. Tente novamente.'
    if pontuacao >= 90:
        return 'A'
    elif pontuacao >= 80:
        return 'B'
    elif pontuacao >= 70:
        return 'C'
    elif pontuacao >= 60:
        return 'D'
    else:
        return 'F'
    
nota = int(input('Escreva sua nota:'))
print(f'Você tirou: {converter_nota(nota)}')