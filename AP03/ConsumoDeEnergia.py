'''
Uma residência deseja estimar o consumo mensal de energia de um equipamento.

Leia:

potência do aparelho (Watts)
horas de uso por dia
dias de uso no mês
preço da energia (R$/kWh)
'''
potencia = int(input('Quanto é a potencia: '))
horas_dia = int(input('Quantas horas voce usa o aparelho por dia: '))
consumo_diario = (potencia * horas_dia) / 1000
dia_mes = int(input('Quantos dias voce usa no mes: '))
preco = int(input('Qual o preço da energia em R$/kWh'))
consumo_mensal = consumo_diario * dia_mes
custo_mensal = preco * consumo_mensal
print(f'o consumo é de {consumo_diario} watts por dia')
print(f'o consumo mensal {consumo_mensal}')
print(f'o consumo mensal {custo_mensal}')