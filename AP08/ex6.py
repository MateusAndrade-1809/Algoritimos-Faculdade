def nota_valida(nota):
    if nota < 0 and nota > 100:
        return False 
    else:
        return True        
nota = int(input('Diga uma nota: '))
res = nota_valida(nota)

print(res)