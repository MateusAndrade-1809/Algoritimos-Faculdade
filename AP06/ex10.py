senha = input('digite sua senha: ')

letra_maiuscula = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letra_minuscula = 'abcdefghijklmnopqrstuvwxyz'
numero = '1234567890'
caracter = '!@#$%¨&*()_-`´^~"][]{};.,<>'

tem_maiuscula = tem_minuscula = tem_numero = tem_caracter = 0

for i in range(len(senha)):
    if senha[i] in letra_maiuscula:
        tem_maiuscula += 1
    if senha[i] in letra_minuscula:
        tem_minuscula += 1
    if senha[i] in numero:
        tem_numero += 1
    if senha[i] in caracter:
        tem_caracter += 1
        

print(f'Quantidade de caracteres: {len(senha)}')

print(f'Letras maiusculas: {tem_maiuscula}')

print(f'Letras minusculas: {tem_minuscula}')

print(f'Numeros: {tem_numero}')

print(f'Caracteres especiais: {tem_caracter}')



if tem_caracter > 0 and tem_maiuscula > 0 and tem_minuscula > 0 and tem_numero > 0:
    print('Senha forte: sim')
else:
    print('Senha forte: não')
    
        
        