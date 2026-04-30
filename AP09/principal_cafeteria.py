from funcoes_cafeteria import calcular_preco_cafe, calcular_acompanhamento, resumo_item, calcular_totais


nome_cafe = input('Nome do café: ')
preco_cafe = float(input('Valor do café: '))
acrescimo_tamanho = float(input('Valor do acréscimo: '))

nome_acompanhamento = input('Nome do acompanhamento: ')
preco_acompanhamento = float(input('Preço do acompanhamento: '))
desconto_acompanhamento = float(input('Desconto do acompanhamento (%): '))

taxa_servico = float(input('Taxa do serviço (%): '))


valor_final_cafe = calcular_preco_cafe(preco_cafe, acrescimo_tamanho)
valor_final_acompanhamento = calcular_acompanhamento(preco_acompanhamento, desconto_acompanhamento)

descricao_cafe, valor_cafe_formatado = resumo_item(nome_cafe, valor_final_cafe)
descricao_acompanhamento, valor_acompanhamento_formatado = resumo_item(nome_acompanhamento, valor_final_acompanhamento)

subtotal, valor_taxa, total_final = calcular_totais(valor_final_cafe, valor_final_acompanhamento, taxa_servico)

print('--------- FECHAMENTO DO PEDIDO ---------')
print(f'Café: {descricao_cafe} - {valor_cafe_formatado}')
print(f'Acompanhamento: {descricao_acompanhamento} - {valor_acompanhamento_formatado}')
print(f'Subtotal: R$ {subtotal:.2f}')
print(f'Taxa de serviço: R$ {valor_taxa:.2f}')
print(f'Total final: R$ {total_final:.2f}')

