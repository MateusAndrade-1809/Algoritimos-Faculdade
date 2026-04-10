p = input()
ok = True

for i in range(len(p)):
    if p[i] != p[-1-i]:
        ok = False

print("É palíndromo" if ok else "Não é palíndromo")