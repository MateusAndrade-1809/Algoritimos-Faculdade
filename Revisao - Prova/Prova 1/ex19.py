##idade, treinamento previo, autorização para o professor

idade = int(input('informe sua idade: '))

acesso_liberado = 0
acesso_negado = 0
total = 0

while idade != 0:
    idade = int(input('Informe sua idade: '))
    if idade < 0:
        print('idade invaldia')
    
    treinamento = input('Possui treinamento previo (sim ou nao): ').lower()
    autorizacao = input('Tem autorização para usar o laboratorio (sim ou nao):').lower()
    
    if idade < 0:
        print('Idade invalida, registro nao foi considerado')
    
    if idade > 17 and treinamento == 'sim':
        print('Acesso Liberado')
        acesso_liberado += 1
        total += 1
    
    elif idade < 18 and treinamento == 'sim' and autorizacao == 'sim':
        print('Acesso Liberado')
        acesso_liberado += 1
        total += 1
        
    else:
        print('Acesso negado')
        acesso_negado += 1
        total += 1
        
if total == 0:
    print('Não há dados suficientes para analise')
    
else:
    print(f'Tiveram {acesso_liberado} acesso(s) liberados')
    print(f'Tiveram {acesso_negado} acesso(s) negados')
    print(f'O percentual de acessos liberados foi {(acesso_liberado / total) * 100:.2f}%')