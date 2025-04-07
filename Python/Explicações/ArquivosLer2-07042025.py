
def Linha():
    arquivo = open('Python\\ArquivosAcesso(explicacao)\\email.txt', 'r', encoding="utf-8")
    linha = arquivo.readline()
    print(linha)
    arquivo.close()

# Linha()
    
def Linha2():
    arquivo = open('Python\\ArquivosAcesso(explicacao)\\email.txt', 'r', encoding="utf-8")
    linha = arquivo.readline()

    while linha != '':
        linha = arquivo.readline()
        print(linha)
    arquivo.close()
 
# Linha2()

def Linha3():
    arquivo = open('Python\\ArquivosAcesso(explicacao)\\email.txt', 'r', encoding="utf-8")
    linha = arquivo.readline()

    while linha != '':
        if "Diciplina" in linha:
            print(linha)
        linha = arquivo.readline()

    arquivo.close()
    
# Linha3()


