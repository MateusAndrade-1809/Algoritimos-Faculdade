contador = 1
soma = 0

while contador <= 5:
    nota = float(input(f"Digite a nota {contador}: "))
    soma = soma + nota
    contador = contador + 1

media = soma / 5

print("Média:", media)