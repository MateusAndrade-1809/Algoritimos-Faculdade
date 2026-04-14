horas = int(input('Digite uma unidade(h/s): '))

if horas <= 50:
    print(f'Vai pagar {horas * 2} reais')

elif horas > 50 and horas < 101:
    print(f'Vai pagar {(horas - 50) * 1.5 + 100} reais')
    
elif horas > 100:
    print(f'Vai pagar {(horas - 100) * 1 + 175} reais')