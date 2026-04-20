def verificar_prefixos_palindromos():
    palavra = input('Digite uma palavra: ').lower()
    n = len(palavra)
    prefixos_palindromos = []

    print(f'\nAnalisando a palavra: {palavra}')

    for i in range(1, n + 1):
        prefixo = palavra[:i]
        
        
        is_palindromo = True
        
        len_prefixo = len(prefixo)
        for j in range(len_prefixo // 2):
            if prefixo[j] != prefixo[len_prefixo - 1 - j]:
                is_palindromo = False
                break
        
        if is_palindromo:
            prefixos_palindromos.append(prefixo)

    print(f'Prefixos palíndromos encontrados: {prefixos_palindromos}')

verificar_prefixos_palindromos()