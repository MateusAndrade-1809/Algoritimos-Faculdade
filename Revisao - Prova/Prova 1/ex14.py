dia = int(input('Informe o dia do mês atual (1-30): '))
while dia < 1 or dia > 30:
    dia = int(input('Dia inválido. Por favor, informe um dia entre 1 e 30: '))

id_engenheiro = int(input('Informe o ID do engenheiro que deseja escalar (1-7): '))
while id_engenheiro < 1 or id_engenheiro > 7:
    id_engenheiro = int(input('ID do engenheiro inválido. Por favor, informe um ID entre 1 e 7: '))

if id_engenheiro % 2 == dia % 2:
    print('Escala confirmada.')
else:
    print('Funcionáriofora da escala.')
