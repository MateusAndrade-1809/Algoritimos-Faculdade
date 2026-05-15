lista = []
aumentou = 0
diminuiu = 0
igual = 0
anterior = 0

for i in range(10):
    temperatura = int(input('Digite a temperatura da maquina: '))
    lista.append(temperatura)
    
for i in lista:
    if anterior != 0:
        if i == anterior:
            igual += 1
        elif i < anterior:
            diminuiu += 1
        elif i > anterior:
            aumentou += 1
    anterior = i

print(f'Aumentou: {aumentou} vezes')
print(f'Diminuiu: {diminuiu} vezes')
print(f'Permaneceu igual: {igual} vezes')