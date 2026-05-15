lista = []
media = 0
acima_media = 0
lista_media = []

for i in range(10):
    nota = int(input('Digite a nora do aluno: '))
    lista.append(nota)
    media += nota 

media_total = media / 10

for i in lista:
    if i > media_total:
        acima_media += 1
        lista_media.append(i)

print(f'Media da turma: {media_total}')
print(f'Quantidade acima da media: {acima_media}')
print(f'Notas acima da media: {lista_media}')
