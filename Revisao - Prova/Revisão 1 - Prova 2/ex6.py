alunos_algoritmos = set()

alunos_calculo = set()

n = int(input('Digite a quantidade de alunos em cada disciplina: '))

print('Alunos Algoritimos: ')

for i in range(n):
    matricula = input(f'Digite a matricula do aluno {i + 1}: ')
    alunos_algoritmos.add(matricula)
    
print('Alunos de Calculo: ')
for i in range(n):
    matricula = input(f'Digite a matricula do aluno {i + 1}: ')
    alunos_calculo.add(matricula)
    
ambas = alunos_algoritmos & alunos_calculo
apenas_uma = alunos_algoritmos ^ alunos_calculo

print(f'Alunos matriculados em ambas as disciplinas: {ambas}')
print(f'Alunos matriculados em apenas uma disciplina: {apenas_uma}')