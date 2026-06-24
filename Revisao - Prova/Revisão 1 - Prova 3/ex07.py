def existe(lista, valor, i):
    if i >= len(lista):
        return False
    if lista[i] == valor:
        return True
    
    return existe(lista, valor, i + 1)