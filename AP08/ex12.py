def converter_tempo(total_segundos):
    horas = total_segundos // 3600
    resto = total_segundos % 3600
    
    minutos = resto // 60
    segundos = resto % 60
    
    return horas, minutos, segundos

total = int(input('Digite o tempo em segundos: '))

h, m, s = converter_tempo(total)

print(f'Horas: {h}')
print(f'Minutos: {m}')
print(f'Segundos: {s}')