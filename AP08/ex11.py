def calcular_inscricao(valor_base, taxa = 10):
    return valor_base + (valor_base * taxa / 100)
    

valor_base = float(input('Informe o valor: '))

valor_padrao = calcular_inscricao(valor_base)
valor_personalizado = calcular_inscricao(valor_base, taxa = 40)

print(f'Valor: {valor_base}')
print(f'Total a pagar com a taxa: {valor_padrao}')
print(f'Total a pagar com valor personalizado: {valor_personalizado}')