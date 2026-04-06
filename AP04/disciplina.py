m = int(input('Qual a media do aluno: '))
p = int(input('Qua o percentual de frequencia(em %): '))

if p < 75:
    print('Reprovado por falta')
elif m >= 60:
    print('Aprovado')
elif m > 40 and m <= 59:
    print('Recuperação')
elif m < 40:
    print('Reprovado por nota')