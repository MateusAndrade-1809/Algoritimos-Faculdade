contador = 1

while contador < 4:
    def nome_aluno(nome):
        return f'Aluno: {nome}'
    def fechamento_atividade(nota):
        if nota > 100 and nota < 0:
            return 'Nota invalida, por favor digite uma nota valida...'
        else:
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
        
    def resumo_geral(nome, nota):
        aluno = nome_aluno(nome)
        desempenho = fechamento_atividade(nota)
        situacao = situacao_final(nota)
        return aluno, desempenho, situacao
    
    nome = input('Digite o nome do Aluno: ')
    nota = int(input('Digite a nota do aluno: '))
    
    aluno, desempenho, situacao = resumo_geral(nome, nota)
    
    print('Fechamento Nota: ')
    print(aluno)
    print(desempenho)
    print(situacao)
    
    contador += 1

        