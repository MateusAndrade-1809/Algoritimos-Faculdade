def autorizar_voo(bateria, velocidade_vento):
    if bateria > 15 and velocidade_vento < 30:
        return True
    else:
        return False


bateria = int(input('Qual é a bateria do drone: '))

contador = 1
falhou = False
etapa_falha = 0
vento = 0

while contador <= 5 and not falhou:
    vento = int(input(f'Diga a velocidade do vento na etapa {contador}: '))

    if autorizar_voo(bateria, vento):
        bateria -= 2
        contador += 1
    else:
        falhou = True
        etapa_falha = contador

if falhou:
    print(f'Ocorreu uma falha na etapa {etapa_falha}')
    print(f'Bateria do drone: {bateria}')
    print(f'Velocidade do vento: {vento}')
else:
    print('Voo autorizado')
    print(f'Bateria restante: {bateria}')
