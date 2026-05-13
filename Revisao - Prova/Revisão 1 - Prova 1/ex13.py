a = int(input("Digite a primeira idade: "))
b = int(input("Digite a segunda idade: "))
c = int(input("Digite a terceira idade: "))

# encontrar o valor do meio
if (a > b and a < c) or (a < b and a > c):
    print((f'A idade de Francisca é {a}'))
elif (b > a and b < c) or (b < a and b > c):
    print(f'A idade de Francisca é {b}')
else:
    print((f'A idade de Francisca é {c}'))