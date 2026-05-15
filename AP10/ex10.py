lista = []
anterior = 0
ordem_cresente = True

for i in range(8):
    numero = int(input('Digite numeros inteiros: '))
    lista.append(numero)
    
for i in lista:
    if anterior != 0:
        if anterior > i:
            ordem_cresente = False
    anterior = i

if ordem_cresente:
    print('A lista esta em ordem crescente.')
else:
    print('A lista não está em ordem crescente.')