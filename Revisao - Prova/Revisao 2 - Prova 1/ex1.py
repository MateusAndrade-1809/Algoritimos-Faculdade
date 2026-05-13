## Peça um número inteiro positivo e verifique se ele é perfeito (soma dos divisores próprios é igual ao número).

numero = int(input('Digite um numero positivo e inteiro para verificar se ele é perfeito: '))


divisivel = 0
divisor = 1

for divisor in range(1, numero):
    if numero % divisor == 0:
        divisivel += divisor
        divisor += 1
        if divisivel == numero :
            print(f'O numero é perfeito')
                
if divisivel != numero:
    print(f'O numero {numero} não é perfeito')
