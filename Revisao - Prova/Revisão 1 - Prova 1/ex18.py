classe = input('Qual sua classe (economica ou executiva): ').lower()
atrasado = input('Voce esta atrasado (sim ou nao): ').lower()
prioridade = input('Possui alguma prioridade (sim ou nao): ').lower()

if atrasado == 'sim':
    print('Voce embarcara por ultimo')


elif prioridade == 'sim':
    print('Voce esta no grupo de prioridade e embarcara em primeira instancia.')
    

elif classe == 'economica':
    categoria = input('Qual sua ategoria(comum, prata ou ouro): ').lower()
    if categoria == 'ouro':
        print('Voce esta no grupo de classe economica ouro e embarcara em terceira instancia.')
    
    elif 'prata':
        print('Voce esta no grupo de classe economica prata e embarcara em quarta instancia.')
        
    else:
        print('Voce esta no grupo de classe economica bronze e embarcara em quinta instancia.')

elif classe == 'executiva':
    print('Voce esta no grupo de classe executiva e embarcara em segunda instancia.')

print()
print('Tenha uma otima viagem!!')