from random import randint
computador = randint(1, 10)
print('Vou pensar em um número de 1 a 10. Tente adivinhar...')
jogador = int(input('Em que número eu pensei? '))
if jogador == computador:
    print('PARABÉNS, você adivinhou na mosca!')
elif jogador < computador:
    print('Tente um número maior!')
else:
    print('Tente um número menor!')