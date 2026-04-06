n = int(input('Digite uma temperatura: '))

if n <= 9:
    print('temperatura baixa')
elif n >= 10 and n <= 25:
    print('Temperatura agradavel')
elif n > 25:
    print('Temperatura alta')
    