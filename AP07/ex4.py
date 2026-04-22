turmas = int(input('Digite a quantidade de turmas: '))

aprovados = 0
reprovados = 0
recuperacao = 0
total = 0

for i in range(turmas):
    alunos = int(input('Quantidade de alunos por turma: '))
    for j in range(alunos):
        nota1 = int(input('Qual a primeira nota do aluno: '))
        nota2 = int(input('Qual a segunda nota do aluno: '))
        
        if (nota1 + nota2) / 2 < 5:
            print('Reprovado')
            reprovados += 1
        elif (nota1 + nota2) / 2 >= 5 and (nota1 + nota2) / 2 < 7:
            print('Rcuperação')
            recuperacao += 1
        elif (nota1 + nota2) / 2 >= 7:
            print('Aprovado')
            aprovados += 1
        total += nota1 + nota2
        
    print(f'A media geral da turma é de {total / alunos}')
    print(f'Quantidade de aprovados: {aprovados}')
    print(f'Alunos em recuperação: {recuperacao}')
    print(f'Alunos reprovados: {reprovados}')