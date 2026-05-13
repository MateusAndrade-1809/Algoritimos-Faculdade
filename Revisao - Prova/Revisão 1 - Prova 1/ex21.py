tempo_previsto = int(input('Digite o tempo previsto(em minutos): '))

prazo = 0
adiantada = 0
atrasado = 0
tempo_amais = 0
atraso_medio = 0
tempo_gasto2 = 0

while tempo_previsto != 0:
    if tempo_previsto < 0:
        print('Tempo desconsiderado do processo')
    
    else:
        tempo_gasto = int(input('Qual foi o tempo gasto para a conclusão da entrega(em minutos): '))
    
        if tempo_gasto < tempo_previsto:
            print('Adiantada ')
            adiantada += 1
            
        elif tempo_gasto == tempo_previsto:
            print('no prazo')
            prazo += 1
        
        elif tempo_gasto > tempo_previsto:
            print('Atrasada')
            atrasado += 1
            tempo_gasto = tempo_gasto2
            tempo_amais = tempo_gasto2 - tempo_previsto
            atraso_medio = tempo_amais / atrasado
            
    tempo_previsto = int(input('Digite o tempo previsto(em minutos): '))
            
print(f'A quantidade de entregas adiantadas foi de {adiantada} entregas')
print(f'A quantidade de entregas no prazo foi de {prazo} entregas')
print(f'A quantidade de entregas atrasadas foi de {atrasado} entregas')

if atrasado == 0:
    print('Não há atraso medio a calcular')
else:
    print(f'Atraso médio entre as entregas classificadas como atrasadas foi de {atraso_medio} minutos')
                    