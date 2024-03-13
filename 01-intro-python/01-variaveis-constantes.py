#identificadores
#letras, numeros e _ (não pode ser if,None,True,False)

#case sensitive
nome = "Bell"
Nome = "Bell"

#variáveis
#convenção snake_case: tudo em minúsculo, separador _
#Inferência de tipo: tipo da variável é definido baseado no valor

ovelha_nome = "Bell" #ele assume String
imposto_renda = 22 #ele assume Int

#constantes
#não existe constante em Python
#convenção: nome em maiúsculo

PI = 3.14 #isso é uma constante, não variável

# comentários de uma única linha

#docstring (comentário de documentação)
#serve para documentar classes, objetos, funções, etc...

def somar(num1,num2):
    '''
    função que soma dois números
    :param num1: primeiro número
    :param num2: segundo número
    :return: soma dos números
    '''
    return num1+num2

somar(1,2)