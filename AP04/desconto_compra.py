id = int(input('Qual a idade do cliente: '))
vc = int(input('Qual o valor da compra: '))

if id >= 60 and vc > 200:
    print('Cliente elegível para desconto')
else:
    print('Cliente sem desconto')