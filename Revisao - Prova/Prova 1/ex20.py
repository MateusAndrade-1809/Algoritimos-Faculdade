## nome item, quantidade disponivel, quantidade minima para funcionamento

nome_produto = input('Pressione enter para entrar no programa').lower()

critica = 0
baixo = 0
adequado = 0

while nome_produto != 'fim':
    nome_produto = input('Informe o nome do produto: ').lower()
    estoque = int(input('Qual a quantidade disponivel para estoque: '))
    quantidade_minima = int(input('Qual a quantidade minima ideal para o funcionamento: '))
    
    if estoque < 0 or quantidade_minima < 0:
        print('Quantidade nao validada pelo sistema.')
        
    else:
        if estoque < (quantidade_minima / 2):
            print('Estoque critico')
            critica += 1
        elif estoque > (quantidade_minima / 2) and estoque < quantidade_minima:
            print('Estoque baixo')
            baixo += 1
        elif estoque >= quantidade_minima:
            print('Estoque adequado')
            adequado +=1
    
if critica <= 0 and baixo <= 0 and baixo <= 0:
    print('O sistema nao localizou nenhum produto valido')

else:
    print(f'Quantidade de produtos criticos é de {critica} produtos')
    print(f'Quantidade de produtos em estoque baixo é de {baixo} produtos')
    print(f'Quantidade de produtos em estoque adequado é de {adequado} produtos')
        
    
    