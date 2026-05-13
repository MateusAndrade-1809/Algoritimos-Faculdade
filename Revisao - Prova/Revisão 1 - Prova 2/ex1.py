def validar_senha(senha):
    if len(senha) < 8:
        return 'Invalida'
    else:
        tem_maiuscula = False
        tem_numero = False
        for caracter in senha:
            if caracter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                tem_maiuscula = True
            else:
                if caracter in '1234567890':
                    tem_numero = True
    
    if tem_maiuscula and tem_numero:
        return 'Valida'
    else:
        return 'Invalida'

senha = input('Digite uma senha: ')
invalida = 0
valida = 0
while senha != 'sair':
    validar = validar_senha(senha)
    if validar == 'Invalida':
        print('Senha Invalida')
        invalida += 1
    else:
        valida += 1
        print('Senha Valida')
    senha = input('Digite uma senha: ')

print(f'A porcentagem de senhas validas testadas foi de {valida} em {valida + invalida}, ou seja, {valida * 100 / (invalida + valida):.2f}%')