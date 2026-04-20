palavra = input('Digite uma palavra para verificar se ela é um palindromo: ')
palindromo = True

for i in range(len(palavra)):
    if palavra[i] != palavra[len(palavra)-1 -i]:
        palindromo = False

if palindromo:
    print(f'A palavra {palavra} é um palindromo')

else:
    print('Não é um palindromo')