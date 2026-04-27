def eh_par(numero):
    return numero % 2 == 0


def contar_pares_faixa(inicio, fim):
    pares = 0
    
    for numero in range(inicio, fim + 1):
        if eh_par(numero):
            pares += 1
    
    return pares


inicio = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))

resultado = contar_pares_faixa(inicio, fim)

print(f'Quantidade de pares: {resultado}')