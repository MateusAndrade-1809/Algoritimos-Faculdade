from funcoes_treino import calcular_calorias, calcular_tempo_treino, analisar_desempenho, consolidar_treino

base_calorias = int(input('Quantidade de calorias do treino: '))
bonus_calorias = int(input('Digite o bonus opcional de calorias: '))
tempo_treino = int(input('Tempo principal do treino: '))
tempo_aquecimento = int(input('Tempo de aquecimento: '))
tempo_semana = int(input('Digite o tempo total em minutos treinado por semana: '))
meta_semanal = int(input('Digite a meta semanal: '))
total_calorias = base_calorias + bonus_calorias

print()
print('-----RELATORIO FINAL-----')
print(f'Calorias totais: {calcular_calorias(base_calorias, bonus_calorias)}')
print(f'Tempo total do treino: {calcular_tempo_treino(tempo_treino, tempo_aquecimento)}')
print(f'Tempo em horas e minutos: {analisar_desempenho(tempo_semana)}')
print(f'{consolidar_treino(total_calorias, meta_semanal)}')