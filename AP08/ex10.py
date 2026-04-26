
def nota_valida(nota):
    return nota >= 0 and nota <= 100


def classificar_desempenho(nota):
    if nota >= 90:
        return 'Excelente'
    elif nota >= 70:
        return 'Bom'
    elif nota >= 60:
        return 'Regular'
    else:
        return 'Insuficiente'


def situacao_final(nota):
    if nota >= 60:
        return 'Aprovado'
    else:
        return 'Reprovado'


def gerar_resumo_correcao(nome, nota):
    if nota_valida(nota):
        classificacao = classificar_desempenho(nota)
        situacao = situacao_final(nota)
        return True, classificacao, situacao
    else:
        return False, 'Não calculada', 'Não calculada'

contador = 1

while contador <= 3:
    nome = input('Digite o nome do aluno: ')
    nota = int(input('Digite a nota do aluno: '))

    valida, classificacao, situacao = gerar_resumo_correcao(nome, nota)

    print('\nFechamento da nota:')
    print(f'Aluno: {nome}')
    print(f'Nota informada: {nota}')
    print(f'Nota válida: {valida}')
    print(f'Classificação: {classificacao}')
    print(f'Situação final: {situacao}')
    print()

    contador += 1

        