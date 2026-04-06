contador = 1

numero = int(input("Digite o número 1: "))
maior = numero
menor = numero

contador = 2

while contador <= 8:
    numero = int(input(f"Digite o número {contador}: "))
    
    if numero > maior:
        maior = numero
    
    if numero < menor:
        menor = numero
    
    contador = contador + 1

print("Maior valor:", maior)
print("Menor valor:", menor)