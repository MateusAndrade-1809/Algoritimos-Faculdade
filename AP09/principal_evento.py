from funcoes_evento import gerar_relatorio_participante


valor_padrao = 120.0
contador = 1

while contador <= 3:
    print(f'\n----- Participante {contador} -----')

    nome = input('Nome do participante: ')
    tipo_ingresso = input('Tipo de ingresso (regular, vip ou estudante): ')
    oficinas = int(input('Quantidade de oficinas extras: '))

    resposta_material = input('Deseja material extra? (s/n): ').lower()

    if resposta_material == 's':
        material_extra = True
    else:
        material_extra = False

    cupom = float(input('Cupom de desconto (%): '))

    valor_base, valor_oficinas, valor_material, valor_desconto, valor_taxa, valor_final, classificacao = gerar_relatorio_participante(
        nome,
        tipo_ingresso,
        valor_padrao,
        oficinas,
        material_extra,
        cupom
    )

    print('\n----- RELATÓRIO DA INSCRIÇÃO -----')
    print(f'Participante: {nome}')
    print(f'Tipo de ingresso: {tipo_ingresso}')
    print(f'Valor base do ingresso: R$ {valor_base:.2f}')
    print(f'Valor das oficinas extras: R$ {valor_oficinas:.2f}')
    print(f'Valor do material extra: R$ {valor_material:.2f}')
    print(f'Valor do desconto aplicado: R$ {valor_desconto:.2f}')
    print(f'Taxa administrativa: R$ {valor_taxa:.2f}')
    print(f'Valor final da inscrição: R$ {valor_final:.2f}')
    print(f'Classificação: {classificacao}')

    contador += 1