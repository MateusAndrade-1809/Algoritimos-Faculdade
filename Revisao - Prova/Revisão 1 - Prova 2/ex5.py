def calcular_fatura(horas):
    if horas <= 100:
        return horas * 5
    elif horas > 100:
        return (horas - 100) * 4 + 500
    elif horas > 500:
        return (horas - 500) * 2,5 + 2100
    
horas = int(input('Digite as horas de instancia do servidor: '))

dinheiro = calcular_fatura(horas)
print(f'O valor foi de R${dinheiro}')
    
