'''Crie um jogo em que o usuário escolhe par ou ímpar, informa um número e joga
contra o computador (que gera um número aleatório). O programa deve mostrar o
resultado da soma, identificar se é par ou ímpar e informar o vencedor. O jogo deve
se repetir até o usuário desejar sair.'''

from random import randint

n_computador = randint(1,100)

print('Jogo impar ou par')

n_usuario = -1

while n_usuario:
    impar_par = input('Escolha (i) para imapr ou (p) para par: ')
    n_usuario = int(input('Escolha o seu numero para jogar(0 para sair): '))
    print(f'O numero do computador foi {n_computador}')
    print(f'A soma dos numeros foi de {n_usuario + n_computador}')
    if impar_par == 'i':
        print(f'Voce escolheu impar')
        if (n_computador + n_usuario) / 2 % 1:
            print('Parabens, voce venceu!!')
        else:
            print('Não foi dessa vez, tente novamente!!')
            
    if impar_par == 'p':
        print('Voce escolheu par')
        if (n_computador + n_usuario) / 2 % 1:
            print('Não foi dessa vez, tente novamente!!')
        else:
            print('Parabens, voce venceu!!')
    