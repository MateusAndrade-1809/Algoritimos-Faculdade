import random
sair  = 'n'
while sair == 'n':
    escolha = input('par ou impar(p ou i): ').lower()
    while escolha not in ['p', 'i']:
        escolha = input('Escolha invalida. Escolha p ou i:').lower()

    if escolha == 'p':
        print('Voce escolheu par. Logo, o computador sera impar.')
        numero_jogador = int(input('Agora escolha o numero qeu voce vai jogar:'))
        numero_computador = random.randint(1, 100)
        print(f'O numero jogado pelo computador foi de {numero_computador}')
        print(f'A soma dos dois numeros foi de {numero_jogador + numero_computador}')
        if (numero_computador + numero_jogador) % 2 == 0:
            print('Parabens, Voce ganho!!')
        else:
            print('O computador ganhou, não foi desssa vez!!')

    if escolha == 'i':
        print('Voce escolheu impar. Logo, o computador sera par.')
        numero_jogador = int(input('Agora escolha o numero qeu voce vai jogar:'))
        numero_computador = random.randint(1, 100)
        print(f'O numero jogado pelo computador foi de {numero_computador}')
        print(f'A soma dos dois numeros foi de {numero_jogador + numero_computador}')
        if (numero_computador + numero_jogador) % 2 == 1:
            print('Parabens, Voce ganho!!')
        else:
            print('O computador ganhou, não foi desssa vez!!')

    sair = input('voce deseja sair? s/n :')
print('Saindo do Programa...')