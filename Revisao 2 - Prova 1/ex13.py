n1 = int(input('informe uma idade(1): '))
n2 = int(input('informe uma idade(2): '))
n3 = int(input('informe uma idade(3): '))

if n1 < n2 and n1 > n3 or n1 < n3 and n1 > n2:
    print(f'A idade do meio é a (1): {n1}')
    
elif n2 < n1 and n2 > n3 or n2 < n3 and n2 > n1:
    print(f'A idade maior é a (2): {n2}')
    
elif n3 < n1 and n3 > n2 or n3 < n2 and n3 > n1:
    print(f'A idade do meio é (3): {n3}')