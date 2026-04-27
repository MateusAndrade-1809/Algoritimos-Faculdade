def converter_tempo(total_segundos):
    horas = total_segundos // 3600
    resto = total_segundos % 3600
    
    minutos = resto // 60
    segundos = resto % 60
    
    return horas, minutos, segundos

def gerar_resumo_tempo(nome, total_segundos):
    horas, minutos, segundos = converter_tempo(total_segundos)
    return f'Participante {nome}: {horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s).'

nome = input('Nome do participante: ')
tempo = int(input('Digite o tempo em segundos desse participante: '))

resumo = gerar_resumo_tempo(nome, tempo)

print(resumo)