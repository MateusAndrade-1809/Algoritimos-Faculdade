def calcular_medias(notas):
    maior_nota = notas[0]
    menor_nota = notas[0]
    soma = 0
    
    for nota in notas:
        soma += nota
        
        if nota > maior_nota:
            maior_nota = nota
            
        if nota < menor_nota:
            menor_nota = nota
        
    media = (soma - maior_nota - menor_nota) / (len(notas) - 2)

    return media

jurados = int(input('Digite a quantidade de jurados: '))

notas_lista = []

for i in range(jurados):
    nota = int(input(f'Digite a nota '))
    notas_lista.append(nota)
    
notas = tuple(notas_lista)

media_final = calcular_medias(notas)

print(f'Notas digitadas: {notas}')
print(f'Media final: {media_final}')