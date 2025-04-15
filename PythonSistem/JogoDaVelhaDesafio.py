import random

lista = ["Abecedario", "Joalheria", "Cavalo", "Professor"]

palavra_escolida = random.choice(lista)
palavra_digitada = ''
palavra_escondida = ''


for i in palavra_escolida:
    i = "_ "
    palavra_escondida += i

def achou_letra():
    for i in palavra_escolida:
        if palavra_digitada in i:
            pass
    return palavra_escondida

print(palavra_escondida)


while True:
    palavra_digitada =  str(input("Digite uma letra ou a palavra:"))

    if palavra_digitada in palavra_escolida:
        count = 0
        print("letra existe")
        achou_letra()
    