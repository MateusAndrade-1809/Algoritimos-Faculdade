## Igual ao jogo de adivinhação, mas agora o usuário tem no máximo 5 tentativas.

from random import randint

escolha = randint(1, 50)

tentativas = 1

while tentativas <= 5:
    
    numero = int(input(f'Escolha um numero de 1 a 50 para advinhar (tentativa {tentativas}): '))
    if numero == escolha:
        print('Parabens, Voce acertou!!')
        tentativas += 50
    elif numero > escolha:
        print(f'Voce errou, o numero escolhido é menor que {numero}')
        tentativas += 1
    elif numero < escolha:
        print(f'Voce errou, o numero escolhido é maior que {numero}.')
        tentativas += 1
    
if tentativas > 3 and tentativas < 50:
    print(f'Voce nao conseguiu advinhar!! O numero era o {escolha}')  
    

print('FIM DO PROGRAMA')