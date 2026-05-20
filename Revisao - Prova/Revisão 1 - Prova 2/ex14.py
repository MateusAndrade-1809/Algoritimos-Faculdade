def calcular_bonus(pontos):
    if pontos > 50:
        return 100
    else:
        return 10
    
funcionarios = int(input('Digite o numero de funcionarios: '))
lista = []

for i in range(funcionarios):
    pontos = int(input(f'Digite a pontuação do funcionario {i + 1}: '))
    lista.append(pontos)

total_pago = 0

for i in range(funcionarios):
    bonus = calcular_bonus(lista[i])
    lista[i] = bonus
    total_pago += bonus

print(f'Lista final de bonus: {lista}')
print(f'Total pago: R$ {total_pago}')
    