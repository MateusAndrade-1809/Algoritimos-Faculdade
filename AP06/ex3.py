n = int(input('Digite um numero:'))
m = int(input('Digite outro numero: '))
res = 0

if n > m:
    print('O primeiro digito deve ser maior que o segundo')
    
else:
    for i in (n, (m+1), 1):
        res += 1
    print(res)
    