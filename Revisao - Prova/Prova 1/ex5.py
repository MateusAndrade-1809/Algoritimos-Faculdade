'''Faça um programa de um jogo de adivinhação. O programa deve gerar um número
aleatório entre 1 e 10. O usuário deve informar palpites, e o programa deve indicar
se o número correto é maior ou menor. O jogo continua até que o usuário acerte.'''

from random import randint

computador = randint(1, 10)

acerte = int(input('Informe um numero de 1 a 10: '))

while acerte != computador:
    
    if acerte < computador:
        print('Quase, tente outro numero!!')
        print('O numero é maior que essse.')
        
    else:
        print('Quase, tente outro numero!!')
        print('O numero é menor que esse!!')
    

    acerte = int(input('tente outro: '))

print(f'parabens voce acertou o numero, o numero era o {computador}.')