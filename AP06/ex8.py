n = int(input('Digite um numero: '))
for i in range(n):
    linha = ""
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            linha += "1"
        else:
            linha += "0"
    print(linha)