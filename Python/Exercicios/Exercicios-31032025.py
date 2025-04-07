''' 

    Exercicio 1 - Faça um algoritimo para ler 3 notas obtidas e a media dos exercicios que fazem parte da eavaliação. Calcular a média
    de apriveutamento, uusando a formula abaixo e escrever o coneito doo aluno de acordo com a tabela de conceitos mais abaixo:           

    Média_de_Aproveitamento = N1 + N2 * 2 + N3 * 3 + media_dos_exercicios

    A atrubyulça de conceitos obedece a tabela abaixo: 

    (tabela aq)

'''



def Exercicio1():
    n = 0
    media = 0
    mediaAPV = 0

    for i in range (3):
        n = float(input(f"Digite a {i + 1}° nota: "))
        media += n
        mediaAPV += (n * (i+1))

    mediaAPV = (mediaAPV + (media/3)) / 7

    if mediaAPV >= 9:
        print(f"Aluno teve Media de Aproveitamento: {mediaAPV}\nAluno tirou 'A'")
    elif mediaAPV >= 7.5:
        print(f"Aluno teve Media de Aproveitamento: {mediaAPV}\nAluno tirou 'B'")
    elif mediaAPV >= 6:
        f"Aluno teve Media de Aproveitamento: {mediaAPV}\nAluno tirou 'C'"
    else:
        f"Aluno teve Media de Aproveitamento: {mediaAPV}\nAluno tirou 'D'"
        
# Exercicio1()    
        

'''
    Desenvolva um algoritmo que:
        1) Solicite a seguinte senha inicial “Senha123”
        Onde o usuário só terá acesso se a senha correta for digitada.
        
        2) Em seguida ler: 
        Nome do cliente
        Número da conta
        Saldo da conta
        Valor do Débito
        Valor do Crédito

        3 - Na sequência, calcular e escrever o saldo atual da seguinte forma:
        (saldo atual = saldo - débito + crédito)
        
        4 - Após, testar se saldo atual for maior ou igual a zero escrever a mensagem
        'Saldo é Positivo', senão escrever a mensagem 'Saldo é Negativo'.
    
    Onde a mensagem deverá aparecer da seguinte forma:
    
    Cliente “NOME DO CLIENTE”, o seu Saldo é ______ no valor de: “VALOR DO
    SALDO ATUAL”
'''
        
def Exercicio2(senha):   
    while senha != "Senha123":
        senha = input("Digite sua senha: ")
    else:
        print("Acesso Permitido")

    
    NomeCliente = str(input("Seu nome: "))
    NúmeroConta = int(input("numero da conta: "))
    SaldoConta = float(input("Seu Saldo: "))
    ValorDebito = float(input("Valor do Débito: "))
    ValorCredito = float(input("Valor do Crédito: "))
    
    SaldoAtual = SaldoConta - (ValorDebito + ValorCredito)

    if saldoAtual >= 0:
        print(f"Saldo positivo.\nCliente “{NomeCliente}”, o seu Saldo é {SaldoConta} no valor de: “{SaldoAtual}”")
    else:
        print(f"Saldo é Negativo.\nCliente “{NomeCliente}”, o seu Saldo é {SaldoConta} no valor de: “{SaldoAtual}”")
        
# Exercicio2(senha = "")


'''
    Exercicio 3 - Escreva um algoritmo que leia uma temperatura em graus Fahrenheit, e em
    seguida converta o mesmo em graus Celsius. Mostrando o resultado no
    final.
    Fórmula para converter graus Fahrenheit em graus Celsius. Onde F é graus
    Fahrenheit e C corresponde a graus Celsius.
    C = (F – 32) * 1,8
'''

def Exercicio3():
    F = float(input("Digite a temperatura Fahrenheit? "))
    C = (F - 32) * 0.55
    print(f"O valor convertido de {F} Fahrenheit para Celsius é de: ", C)
    
# Exercicio3()
    
'''
    Exercicio 4 - Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em
    estoque e quantidade mínima em estoque de um produto. Calcular e escrever a
    quantidade média ((quantidade média = quantidade máxima + quantidade
    mínima)/2). Se a quantidade em estoque for maior ou igual a quantidade média
    escrever a mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar
    compra'.
'''

def Exercicio4():
    quantidade = int(input("Quantidade no Extoque: "))
    quantidadeMaxima = int(input("Quantidade Maxima do Extoque: "))
    quantidadeMinima = int(input("Quantidade Minima do Extoque: "))
    quantidadeMedia = (quantidadeMaxima + quantidadeMinima)/2
    
    if quantidade >= quantidadeMedia:
        print("Não efetuar compra")
    else:
        print("Efetuar compra")
        
# Exercicio4()
        
'''

    Exercicio 5 - Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres (considere
    que as idades dos homens serão sempre diferentes entre si, bem como as das
    mulheres). Calcule e escreva a soma das idades do homem mais velho com a
    mulher mais nova, e o produto das idades do homem mais novo com a mulher
    mais velha.

'''
    
def Exercicio5():
    homem = []
    mulher = []
    
    veioNova = []
    veiaNovo = []
    
    for i in range(2):
        homem.append(int(input(f"Idade do {i + 1}° homem: ")))
        mulher.append(int(input(f"Idade da {i + 1}° mulher: ")))
        
    if homem[0] < homem[1]:
        veioNova.append(homem[1]) # Homem mais velho
        veiaNovo.append(homem[0]) # Homem mais novo
    else:
        veioNova.append(homem[0]) # Homem mais velho
        veiaNovo.append(homem[1]) # Homem mais novo

    if mulher[0] < mulher[1]:
        veioNova.append(mulher[0]) # mulher mais velha
        veiaNovo.append(mulher[1]) # mulher mais nova
    else:
        veioNova.append(mulher[0]) # mulher mais velha
        veiaNovo.append(mulher[1]) # mulher mais nova
        
    soma = veioNova[0] + veioNova[1]
    prod = veiaNovo[1] * veiaNovo[0]

        
    print("soma: ", soma, "\nproduto: ", prod)
        
# Exercicio5()



''' 
Exercicio Bonus 1 - Inverter String 
'''

def ExercicioBonus1():
    string = "Cavalo"
    print(string[::-1])
    
# ExercicioBonus1()



''' 
Exercicio Bonus 2 - Criar e verificar Palindromo
'''

def ExercicioBonus2():
    palindromo = str(input("Hello, whire something to check the palindromo"))
    certeza = palindromo[::-1]
    
    if certeza.casefold() != palindromo.casefold():
        print(certeza, "\nnão Palindromo")
    else:
        print(certeza, "\né Palindromo")
# ExercicioBonus2()