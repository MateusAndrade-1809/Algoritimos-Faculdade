def calcular_situacao(nota):
    if nota >= 70:
        return 'Aprovado'
    elif nota >= 50 and nota <= 69:
        return 'Recuperação'
    else:
        return 'Reprovado'
    
nota = int(input('Digite a nota: '))

res = calcular_situacao(nota)

print(res)