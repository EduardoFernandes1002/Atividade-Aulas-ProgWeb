def exercicio1():
    arquiva = open('Python/ArquivosAcess(Exercicios)/frases.txt', 'a', encoding='utf-8')
    for i in range(3):
        f = str(input(f"Digite a {i+1}°"))
        arquiva.write(f"{f}\n")
        
    arquiva = open('Python\\ArquivosAcess(Exercicios)\\frases.txt', 'r', encoding='utf-8')
    print(arquiva.read())
    arquiva.close()
    
# exercicio1()

def exercicio2e3():
    arquiva2 = open('Python\\ArquivosAcess(Exercicios)\\email.txt', 'r', encoding='utf-8')
    palavra = arquiva2.read()
    print(f"Numero de palavras: {len(palavra.split())} \nNumero de Linhas: {len(palavra.split("\n"))}")
    arquiva2.close()
    
# exercicio2e3()

def exercicio4():
    with open('Python/ArquivosAcess(Exercicios)/frases.txt', 'r', encoding='utf-8') as arquivo1:
        conteudo = arquivo1.read()
    with open('Python/ArquivosAcess(Exercicios)/copia.txt', 'w', encoding='utf-8') as arquivo2:
        arquivo2.write(conteudo)
    with open('Python/ArquivosAcess(Exercicios)/copia.txt', 'r', encoding='utf-8') as arquivo2:
         print(arquivo2.read())
    
# exercicio4()

def exercicio5():
    with open('Python/ArquivosAcess(Exercicios)/frases.txt', 'r', encoding='utf-8') as arquivo1:
        linhas = arquivo1.readlines()
    linhas = [linha.strip() for linha in linhas]
    linhas.sort()

    with open('Python/ArquivosAcess(Exercicios)/frases_ordenadas.txt', 'a', encoding='utf-8') as arquivo2:
        for linha in linhas:
            arquivo2.write(linha+'\n')
    with open('Python/ArquivosAcess(Exercicios)/frases_ordenadas.txt', 'r', encoding='utf-8') as arquivo2:
        print(arquivo2.read())
        
    arquivo1.close()
    arquivo2.close()
       
exercicio5()