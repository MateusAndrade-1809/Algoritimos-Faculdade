bateria = int(input('Informe a bateria do drone: '))

etapas = 0
vento = 0

bateria_final = bateria * 0.85

while etapas <= 4:
    vento = int(input('Digite a velocidade do vento(km/h): '))
    if vento > 30 or bateria < 10:
        print('Decolagem foi cancelada por Vento Forte ou Bateria Fraca')
        if etapas == 0:
            print(f'Bateria em {bateria * 0.983}%')
        if etapas == 1:
            print(f'Bateria em {bateria * 0.966}%')
        if etapas == 2:
            print(f'Bateria em {bateria * 0.949}%')
        if etapas == 3:
            print(f'Bateria em {bateria * 0.932}%')
        if etapas == 4:
            print(f'Bateria em {bateria * 0.915}%')
        etapas += 5
        
    else:
        etapas += 1
        
if vento < 30:
    if bateria_final < 10 :
        print('Decolagem cancelada por falta de bateria')
        print(f'Bateria em {bateria_final}%')

    else:
        print('Decolagem autorizada')
        print(f'A sua bateria final foi de {bateria_final}%')

