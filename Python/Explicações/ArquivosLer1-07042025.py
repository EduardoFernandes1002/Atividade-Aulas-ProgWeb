### Metodo Padrão
def met1():
    arquivo = open('Python\\ArquivosAcesso(explicacao)\\email.txt', 'r')
    conteudo = arquivo.read()
    print(conteudo)
    arquivo.close()
# met1()

def met2():
    arquivo = open('Python\\ArquivosAcesso(explicacao)\\email.txt', 'r', encoding="utf-8")
    conteudo = arquivo.read()
    print(conteudo)
    arquivo.close()

# met2()

def met3():
    with open('Python\\ArquivosAcesso(explicacao)\\email.txt', 'r', encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
    print(conteudo)
met3()