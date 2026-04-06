'''Um laboratório de informática possui regras específicas para acesso durante a noite.

O programa deve ler:

idade do usuário
se possui matrícula ativa (1 = sim, 0 = não)
se possui autorização especial (1 = sim, 0 = não)
Regras de acesso:

Estudantes com matrícula ativa e idade ≥ 18 podem entrar.
Estudantes com matrícula ativa menores de 18 só entram com autorização.
Pessoas sem matrícula ativa só entram com autorização.
O programa deve indicar:

Acesso permitido
ou
Acesso negado
'''

id = int(input('Qual a idade do usuario: '))
ma = int(input('Possui matricula ativa 1 = sim, 0 = não: '))
ae = int(input('Possui autorização espeical 1 = sim, 0 = não'))

if ma == 1 and id > 17:
    print('Acesso permitido')
elif ma == 1 and id < 18 and ae == 0:
    print('Acesso Negado')
elif ma == 1 and id < 18 and ae == 1:
    print('Acesso permitido')
elif ma == 0 and id < 18 and ae == 1:
    print('Acesso permitido')
elif ma == 0 and id < 18 and ae == 0:
    print('Acesso negado')

