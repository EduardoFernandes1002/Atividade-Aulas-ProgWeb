lar = int(input("Digite um largura"))
alt = int(input("Digite o numero de altura"))


print(lar*'*')
for x in range(alt):
    print('*' + ' ' * (lar - 2) + '*')
print(lar*'*')

### Exercicio1
frase = "Todo  e qualquer  espaço  duplo  em  branco  deve  ser removido  !!"

print(frase.replace('  ', ' '))

frase2 = "Hello World"
print(frase2.replace('World', "Universe"))