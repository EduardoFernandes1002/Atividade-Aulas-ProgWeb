'''

    1 - Crie um programa que recebe o produto e o valor dele,
    armazenando esses dados em um dicionario.
    Depois exiba as informações na tela.
    
'''
def exercicio1():
    produto: str = input("Qual o produto: ")
    valor: float = input("Valor do produto: ")
    custo = {produto: valor}
    print(f'o produto é: {produto}, com o valor de {custo[produto]}')
    
# exercicio1()

'''

    2 - Crie um programa que cadastre carros e seus valores em um dicionario, 
    quantos carros os usuario quizer.E quando for digitado "SAIR", será 
    encerrado a inserção.

'''

def exercicio2():
    Nomecarro: str = ''
    carros = {}
    

    while perg != 'SAIR':
        Nomecarro = input("qual seu(s) carro: ")
        carros[Nomecarro] = float(input("qual o valor desse carro: "))
        perg = input("Deseja sair?\nDigite 'SAIR' caso queira: ")
    else:
        print("Saindo")
    print(carros)

exercicio2()