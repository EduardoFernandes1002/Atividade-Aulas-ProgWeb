'''

    Crie um programa que armazene o nome e a idade de varias pessoas em um dicionario.
    Em seguida, peça ao usuário para digitar um nome que exiba a idade correspondente. 
    Se não existir o usuario, informe que não foi encontrado.

'''
nome = str(input("Digite um nome: "))

pessoa = {
    'Pedro': 20,
    'Eduardo': 19
}


if nome in pessoa:
    print(f'idade de {nome} é {pessoa[nome]}')
else:
    print('Essa pessoa não existe')