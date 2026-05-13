biblioteca = {
    '123': ['Dom Casmurro', 'Machado de Assis', 3]
}


def emprestar_livro(isbn):
    if isbn in biblioteca:
        if biblioteca[isbn][2] > 0:
            biblioteca[isbn][2] = biblioteca[isbn][2] - 1
            return 'Disponivel'
        else:
            return 'Indisponivel'
    else:
        return 'Inexistente'


def devolver_livro(isbn):
    if isbn in biblioteca:
        biblioteca[isbn][2] = biblioteca[isbn][2] + 1
        return 'Devolvido'
    else:
        return 'Inexistente'


isbn = input('Informe o codigo do livro que voce queira utilizar: ')

verificar = emprestar_livro(isbn)

if verificar == 'Disponivel':
    print('Pode emprestar')
elif verificar == 'Indisponivel':
    print('Não há exemplares do livro')
elif verificar == 'Inexistente':
    print('Esse livro não existe')


devolver = input('Digite o codigo do livro que voce gostaria de devolver: ')

devolucao = devolver_livro(devolver)

if devolucao == 'Devolvido':
    print('Livro devolvido com sucesso')
elif devolucao == 'Inexistente':
    print('Esse livro não existe')
