def classificar_desempenho(nota):
    if nota > 89 and nota < 101:
        return 'Excelente'
    elif nota > 69 and nota < 90:
        return 'Bom'
    elif nota > 59 and nota < 70:
        return 'Regular'
    else:
        return 'Insuficiente'
def situacao_final(nota):
    if nota >= 60:
        return 'Aprovado'
    else:
        return 'Reprovado'
        
def resumo_geral(nota):
    desempenho = classificar_desempenho(nota)
    situacao = situacao_final(nota)
    return desempenho, situacao

nota = int(input('Digite a nota do aluno: '))

desempenho, situacao = resumo_geral(nota)

print(f'Desempenho: {desempenho}')
print(f'Situação: {situacao}')
