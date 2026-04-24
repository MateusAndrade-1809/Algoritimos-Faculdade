def calcular_comissao(valor_venda):
    return valor_venda * 0.05

valor_venda = float(input('Qual o valor da venda: '))
comissao = calcular_comissao(valor_venda)

print(f'Valor da comissão é de {comissao}')