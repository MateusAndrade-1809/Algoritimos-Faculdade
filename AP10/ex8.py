lista = []
encontrado = 0
nome_encontrado = False

for i in range(8):
    nome = input('Diga o nome das pessoas: ')
    lista.append(nome)
    
procurado = input('Digite o nome a ser procurado: ')

for i in lista:
    if i == procurado:
        encontrado += 1
        nome_encontrado = True
        
if nome_encontrado:
    print(f'Nome encontrado.')
    print(f'Quantidade de ocorrências: {encontrado}')
else:
    print(f'Nome não encontrado.')
