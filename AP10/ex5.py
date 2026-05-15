lista = []
maior = 0
menor = 0
posicao_maior = 0
posicao_menor = 0

for i in range(8):
    numero = int(input('Digite numeros inteiros: '))
    lista.append(numero)
    if i == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
            posicao_maior = i
        if menor < menor:
            menor = numero
            posicao_menor = i

print(f'Maior valor: {maior}')
print(f'Posição do maior valor: {posicao_maior}')
print(f'Menor valor: {menor}')
print(f'Posição do menor valor: {posicao_menor}')
        
    
