## Peça uma base e um expoente inteiro não negativo ao usuário e calcule a potência
## manualmente, sem usar operador de exponenciação, utilizando um for.

base = int(input('Digite uma base inteira e nao neagtivo: '))

expoente = int(input('Digite um expoente inteiro não negativo: '))

resultado = 1

for i in range(expoente):
    resultado = base * resultado
    i += 1
            
        
print(f'o {base} elevado a {expoente} é igual a {resultado}')