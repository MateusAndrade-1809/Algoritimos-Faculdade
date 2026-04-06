'''
Uma competição escolar de programação classifica participantes com base em:

pontuação obtida
tempo gasto na prova
O programa deve ler:

pontuação total do participante
tempo total gasto (em minutos)
Classificação:

pontuação ≥ 90 → Ouro
pontuação ≥ 70 → Prata
pontuação ≥ 50 → Bronze
caso contrário → sem medalha
Regra adicional:

Se o participante obtiver Ouro e terminar a prova em menos de 120 minutos, ele recebe:

Participante destaque da competição
'''

pt = int(input('Quual foi a pontuação do participante: '))
tg = int(input('Qual foi o tempo do participante (em minutos): '))

if pt >= 90:
    print('Ouro')
elif pt >= 70:
    print('Prata')
elif pt >= 50:
    print('Bronze')
elif pt < 50:
    print('Sem medalha')
if pt >= 90 and tg < 120:
    print('Participante destaque da competição')


