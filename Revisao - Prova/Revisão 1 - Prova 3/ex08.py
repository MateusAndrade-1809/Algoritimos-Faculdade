def soma_digitos(numero):
    if numero < 10:
        return numero
    else:
        return numero % 10 + soma_digitos(numero // 10)
    
