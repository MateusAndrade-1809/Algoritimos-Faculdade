def classificar_desempenho(nota):
    if nota > 89 and nota < 101:
        return 'Excelente'
    elif nota > 69 and nota < 90:
        return 'Bom'
    elif nota > 59 and nota < 70:
        return 'Regular'
    else:
        return 'Insuficiente'
    
nota = int(input('Digite a nota: '))
res = classificar_desempenho(nota)

print(res)