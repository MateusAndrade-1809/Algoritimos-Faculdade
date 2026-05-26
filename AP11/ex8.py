notas = []
medias = []
aprovados = 0

for i in range(5):
    linha = []
    for j in range(4):
        nota = float(input(f'Digite a nota do aluno {i}, atividade {j}: '))
        linha.append(nota)
    notas.append(linha)

for i in range(5):
    soma = 0

    for j in range(4):
        soma += notas[i][j]

    media = soma / 4
    medias.append(media)

    if media >= 70:
        situacao = 'Aprovado'
        aprovados += 1
    elif media >= 40:
        situacao = 'Recuperacao'
    else:
        situacao = 'Reprovado'

    print(f'Aluno {i} - Media: {media:.2f} - {situacao}')

maior = medias[0]
menor = medias[0]

for media in medias:
    if media > maior:
        maior = media

    if media < menor:
        menor = media

print(f'Maior media: {maior:.2f}')
print(f'Menor media: {menor:.2f}')
print(f'Quantidade de aprovados: {aprovados}')