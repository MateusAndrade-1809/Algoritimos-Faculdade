sequencia = int(input('Digite numeros inteiros: '))
lista = []
maior_trecho = []

while sequencia != 0:
    lista.append(sequencia)
    sequencia = int(input('Digite numeros inteiros: '))
    
maior_trecho = [lista[0]]
trecho_atual = [lista[0]]

for i in range(1, len(lista)):
    if lista[i] > lista[i - 1]:
        trecho_atual.append(lista[i])
    else:
        trecho_atual = [lista[i]]
        
    if len(trecho_atual) > len(maior_trecho):
        maior_trecho = trecho_atual

print(f'Maior trecho crescente: {maior_trecho}')
print(f'Tamanho: {len(maior_trecho)}')