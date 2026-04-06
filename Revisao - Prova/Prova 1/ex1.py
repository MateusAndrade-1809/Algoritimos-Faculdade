numero = int(input("Digite um número inteiro positivo: "))

divisor = 2
eh_primo = True

if numero <= 1:
    eh_primo = False
else:
    while divisor < numero and eh_primo:
        if numero % divisor == 0:
            eh_primo = False
        divisor = divisor + 1

if eh_primo:
    print("É primo")
else:
    print("Não é primo")