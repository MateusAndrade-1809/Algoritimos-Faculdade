def calcular_preco_cafe(preco_base, acrescimo=0.0):
    return preco_base + acrescimo


def calcular_acompanhamento(preco, desconto=0.0):
    return preco - (preco * desconto / 100)


def resumo_item(nome, valor):
    descricao = nome
    valor_formatado = f'R$ {valor:.2f}'
    return descricao, valor_formatado


def calcular_totais(valor1, valor2, taxa_servico=10.0):
    subtotal = valor1 + valor2
    valor_taxa = subtotal * taxa_servico / 100
    total_final = subtotal + valor_taxa

    return subtotal, valor_taxa, total_final