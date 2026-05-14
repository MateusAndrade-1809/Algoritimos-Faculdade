def calcular_fatura(horas):
    if horas <= 100:
        return horas * 5
    elif horas > 100:
        return (horas - 100) * 4 + 500
    elif horas > 500:
        return (horas - 500) * 2,5 + 2100
    
id = int(input('Digite o ID do cliente: '))
faturamento_total = 0
fatura = 0
    
while id != 0:
    horas = int(input('Digite as horas consumidas do cliente: '))
    fatura = calcular_fatura(horas)
    print(f'O total a pagar do cliente {id} é de R${fatura}')
    faturamento_total += fatura
    id = int(input('Digite o ID do cliente: '))

print(f'Faturamento total da empresa é de R${faturamento_total}')