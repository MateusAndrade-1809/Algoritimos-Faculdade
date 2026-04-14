numero = -1

consecutivos = 0

ultimo_numero = 0

while numero != 0:
    numero = int(input('Digite numeros para verificação(0 para parar): '))
    
    if numero == ultimo_numero:
        consecutivos += 1
        
    ultimo_numero = numero
    
print(f'Teve um total de {consecutivos} numeros iguais consecutivos.')