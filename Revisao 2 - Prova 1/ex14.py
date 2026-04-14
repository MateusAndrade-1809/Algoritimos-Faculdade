dia = int(input('Qual dia é hoje: '))
id_func = int(input('Digite o id do funcionario: '))

if id_func % 3 == 0:
    if dia % 3 == 0:
        print('Pode trabalhar hoje 👌')
    else:
        print('Não pode trabalhar hoje')
else:
    print('Pode trabalhar hoje 👌')