quantidade_termos = int(input('Digite o valor inteiro de n: '))

soma_final = 0
soma_denominador = 0

for numero in range(1, quantidade_termos + 1):
    soma_denominador += numero
    
    termo_atual = soma_denominador
    
    soma_final += termo_atual
    
    print(f'Termo {numero}: {termo_atual}')
    

print(f'O resultado da soma é: {soma_final}')