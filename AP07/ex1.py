A = int(input())
B = int(input())

for i in range(A, B + 1):
    print(f'Número {i}:')
    
    for j in range(1, i + 1):
        if j % 3 == 0 and j % 5 == 0:
            print(f'{j} - múltiplo de 3 e 5')
        elif j % 3 == 0:
            print(f'{j} - múltiplo de 3')
        elif j % 5 == 0:
            print(f'{j} - múltiplo de 5')
        else:
            print(f'{j} - nenhum')