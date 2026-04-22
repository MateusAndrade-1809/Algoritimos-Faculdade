linha = int(input('Digite um numero inteiro positivo: '))
coluna = int(input('Digite um numero inteiro positivo: '))

for i in range(1, linha + 1):
    for j in range(1, coluna + 1):
        print(f'linha {i} e coluna {j}')
        print(f'produto = {i * j}')
        if i * j < 11 and i * j % 2 == 0:
            print(f'par, pequeno')
        elif i * j > 10 and i * j < 21 and i * j % 2 == 0:
            print('par, medio')
        elif i * j > 20 and i * j % 2 == 0:
            print('par, grande')
        elif i * j < 11 and i * j % 2 != 0:
            print('impar, pequeno')
        elif i * j > 10 and i * j < 21 and i * j % 2 != 0:
            print('impar, medio')
        elif i * j > 20 and i * j % 2 != 0:
            print('impar, grande')