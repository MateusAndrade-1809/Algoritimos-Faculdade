def calcular_valor_final(valor_produto, desconto):
    return valor_produto - (valor_produto * desconto / 100)

valor = int(input('Qual o valor do produto: '))
desconto = int(input('Qual o desconto do produto: '))
final = calcular_valor_final(valor, desconto)

print(f'Valor com desconto: {final}')