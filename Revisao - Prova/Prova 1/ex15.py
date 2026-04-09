h = int(input('Digite o valor de horas que voce quer: '))

i = 0

if h <= 100:
    print(f'o total gasto sera de {h * 5}')
    
if h > 100 and h <= 500:
    valor_total = h * 4
    print(f'O valor total gasto sera de {valor_total + 100}')
    
if h > 500:
    valor_total = h * 2.5 - 150
    print(f'O valor total pago sera de {valor_total}')