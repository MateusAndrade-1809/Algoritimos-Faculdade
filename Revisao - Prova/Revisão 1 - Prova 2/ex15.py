sequencia = int(input('Digite uma sequencia: '))
lista = []
maior = 0

while sequencia != 0:
    anterior = sequencia
    lista.append(sequencia)
    sequencia = int(input('Digite uma sequencia: '))
    if anterior < sequencia:
        maior += 1

print(lista)
print(f'Trecho consecutivo presente: {maior}')

