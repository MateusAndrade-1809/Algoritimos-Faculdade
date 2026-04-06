n = int(input('digite a nota do aluno de 0 a 100: '))
if n >= 90 and n <= 100:
    print('Excelente')
elif n >= 70 and n <=89:
    print('Bom')
elif n >= 50 and n <= 69:
    print('Regular')
elif n < 50:
    print ('Insuficiente')
    