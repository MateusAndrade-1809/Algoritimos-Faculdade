def eliminar_duplicatas(lista):
    nova_lista = []
    for numero in lista:
        if numero not in nova_lista:
            nova_lista.append(numero)
    return nova_lista
    
contador = 0
lista = []
while contador < 20:
    numero = int(input('Digite um numero inteiro: '))
    lista.append(numero)
    contador += 1

nova_lista = eliminar_duplicatas(lista)
print(nova_lista)

