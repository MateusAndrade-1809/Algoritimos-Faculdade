from random import randint

print('BEM VINDO AO PAR OU IMPAR')


vitorias = 0
derrotas = 0

while derrotas <= 3:
    n_computador = randint(1,10)
    escolha = input('Escolha (p) para par e (i) para impar: ').lower()
    if escolha != 'p' or 'i':
        print('Voce deve escolher i ou p para selecionar par ou impar')
        derrotas += 4
    else:
        n_usuario = int(input('Escola um numero positivo e inteiro para jogar: '))
        print('Muito bem, agora vamos começar')
        print()
        print(f'O numero escolhido pelo computador foi o {n_computador}')
        print()
        print(f'A soma dos numeros é de {n_computador + n_usuario}')
        print()
        if escolha == 'p':
            if (n_usuario + n_computador) % 2 == 0:
                print('PARABENS!! VOCE VENCEU!!')
                print(f'Agora voce esta com {vitorias + 1} vitoria(s)')
            else:
                print(f'Não foi dessa vez. :(')
                print(f'Agora voce esta com {derrotas + 1} derrota(s)')

        if escolha == 'p':
            if (n_usuario + n_computador) % 2 == 0:
                print(f'Não foi dessa vez. :(')
                print(f'Agora voce esta com {derrotas + 1} derrota(s)')
            else:
                print('PARABENS!! VOCE VENCEU!!')
                print(f'Agora voce esta com {vitorias + 1} vitoria(s)')
            
print()
print(f'Voce alcançou as 3 derrtoas, seu total de vitorias foi de {vitorias}')
print()
print('FINALIZANDO PROGRAMA')