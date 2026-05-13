maior = 0

sequencia = -1

total = 0

while sequencia != 0:
    sequencia = int(input('Digite uma sequencia (zero para parar): '))
    
    if sequencia > total:
        maior += 1
    total = sequencia
    
print(f'A maior sequencia foi de {maior - 1} numeros ')
    
    
    
    