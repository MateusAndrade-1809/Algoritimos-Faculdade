senha = input('Digite sua senha: ')

validas = 0
invalidas = 0
maior_senha = ''

while senha != 'encerrar':
    tem_numero = False

    for c in senha:
        if c in '0123456789':
            tem_numero = True

    if len(senha) >= 8 and ' ' not in senha and tem_numero:
        print('Senha válida')
        validas += 1

        if len(senha) > len(maior_senha):
            maior_senha = senha
    else:
        print('Senha inválida')
        invalidas += 1

    senha = input('Digite sua senha: ')

if validas == 0:
    print('Nenhuma senha válida foi informada')
else:
    print(f'Total de senhas válidas:{validas}')
    print(f'Total de senhas inválidas:{invalidas}')
    print(f'A maior senha válida digitada foi:{maior_senha}')