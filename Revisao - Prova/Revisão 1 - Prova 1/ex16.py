capacidade = int(input('Qual a capacidade maxima do silo (em kg): '))

total_agricultores = 0

quilos_totais = capacidade

total = 0

while capacidade > 0:
    agricultor = int(input('Qual o peso desejado pelo agricultor: '))
    if agricultor > capacidade:
        print('O silo nao tem esse estoque')
        break
    
    capacidade = capacidade - agricultor
    total_agricultores += 1
    total = quilos_totais - capacidade
    
print(f'O total de agricultores foi de {total_agricultores}')
print(f'O total distribuido em kg foi de {total}')

print('---------Encerrando programa--------')