def eh_primo(numero, divisor):
    if numero < 2:
        return False

    if divisor * divisor > numero:
        return True

    if numero % divisor == 0:
        return False

    return eh_primo(numero, divisor + 1)
