quantidade_termos = int(input('Digite o valor inteiro de n: '))

soma_final = 0
numerador = 1
numero_impar = 1

for posicao in range(1, quantidade_termos + 1):
    numerador *= numero_impar
    denominador = (2 ** posicao) * posicao

    termo_atual = numerador / denominador

    soma_final += termo_atual
    
    print(f'Termo {posicao}: {termo_atual}')
    
    numero_impar += 2

print(f'O resultado da soma é: {soma_final}')