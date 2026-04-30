from funcoes_viagem import calcular_passagem, calcular_hospedagem, converter_duracao, calcular_orcamento

base_passagem = int(input('Valor base da passagem: '))
taxa_bagagem = int(input('Taxa bagagem: '))
diaria = int(input('Valor da diária: '))
qntd_dias = int(input('Quantidade de dias: '))
taxa_hospedagem = int(input('Taxa hospedagem: '))
duracao_viagem = int(input('Duração da viagem em hrs: '))
alimentacao = int(input('Gasto com alimentação: '))

total_passagem = calcular_passagem(base_passagem, taxa_bagagem)
total_hospedagem = calcular_hospedagem(diaria, qntd_dias, taxa_hospedagem)
duracao = converter_duracao(duracao_viagem)
total_orcamento = calcular_orcamento(total_passagem, total_hospedagem, alimentacao)

print('------RESUMO VIAGEM--------')
print(f'Valor passagem: {total_passagem}')
print(f'Valor hospedagem: {total_hospedagem}')
print(f'Duração viagem: Dias - {duracao} - Horas')
print(f'Custo fixo, custo extra e custo total: {total_orcamento}')