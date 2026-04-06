'''

Exercício 3 Boletim Simplificado
Leia três notas e calcule as seguintes informações:

Soma das notas
Média das notas
Pontos que faltam para o aluno ficar com total (máximo de pontos possíveis)
Observação: Cada prova vale 10 pontos.

Saída esperada:

Relatório de notas
------------------
Soma das notas: ...
Média: ...
Pontos para nota maxima: ...
'''

nota1 = int(input('Qual a nota da sua primeira prova: '))
total1 = int(input('Quanto falta para voce atingir a nota maxima: '))
nota2 = int(input('Qual a nota da sua segunda prova: '))
total2 = int(input('Quanto falta para voce atingir a nota maxima: '))
nota3 = int(input('Qual a nota da sua terceira prova: '))
total3 = int(input('Quanto falta para voce atingir a nota maxima: '))
soma_notas = print(f'a soma das notas é de {nota1 + nota2 + nota3}')
media_not = print(f'A media das notas é de {nota1 + nota2 + nota3 / 3}')
atingir_total = print(f'Falta {total1 + total2 + total3} para atingir o total')

