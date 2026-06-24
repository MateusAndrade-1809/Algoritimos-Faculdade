def calcular_mdc(a, b):
    if b == 0:
        return a
    else:
        return calcular_mdc(b, a % b)