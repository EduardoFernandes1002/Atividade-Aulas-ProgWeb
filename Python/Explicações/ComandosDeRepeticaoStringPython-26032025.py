Lista = [1,2,3]
lista2 = []

print(lista2)

lista2 = list(range(5, 21))
print(lista2)

lista2 = list(range(0, 50, 5))

print(lista2)




''' ---- MANIPULAÇÃO DE STRINGS ---- '''

texto = '1000.00'
print(texto.replace('.', ','))

### len | Retorna quantidade de caracteres

cpf = "12345678913"
print(len(cpf))

###  - Coloca primeira letra em maiusculo

txt = "eduardo Fernandes"

print(txt.capitalize())

### title - Coloca primeira letra de cada palavra em maiusculo

txt2 = "Eduardo Fernandes"

print(txt2.title())

### upper() - Coloca toda string em maiusculo

thiago = "Thiago do Santos"
print(thiago.upper())

### Casefold - Coloca as letras da string em minusculo, (também existe LOWER)

Dias = "DIas"
print(Dias.swapcase())

### swapcase - Inverte letras maiusculas para minusculas e vice-versa

Dias2 = "DIas"
print(Dias2.swapcase())

### count - Conta quantidade de vezes que um caractere aparece em uma string

frase = "quantas veezes aparece a letra 'A' nessa string"

print(frase.count('a'))

### find - Procura uma palavra especifica (ou letra) em string

email = "meuemail@gmail.com"
print(email.find('@'))

### Split - Função utiliza para cortas string a partir de um caracter

que = "Eu gosto de café."
print(que.split(' '))

print(que[1:6])

que += '\nEu também'

print(que)