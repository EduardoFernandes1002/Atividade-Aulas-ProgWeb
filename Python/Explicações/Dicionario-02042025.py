planetas = {
    'nome' : 'Terra',
    'luas': 1
}

print(planetas.get('nome'))

chuvas = {
    'janeiro': 3.5,
    'fevereiro': 4.2,
    'março': 2.1
    }
    
if 'março' in chuvas:
    chuvas['março'] = chuvas['março'] + 1
else:
    chuvas['março'] = 1
print(chuvas)