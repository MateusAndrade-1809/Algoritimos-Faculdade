linha = int(input(f"Informe o numero de linhas: "))
coluna = int(input(f"Informe o numero de coluna: "))
res = ''
i = 0
j = 0
while i < linha:
    if i == 0:
        res += '*'
    else:
        res += '\n*'
    j = 1
    while j < coluna:
        res += '*'
        j += 1
    i += 1
print(f"{res}")