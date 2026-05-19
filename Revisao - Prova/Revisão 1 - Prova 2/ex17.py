def matriz_simetrica(M):
    n = len(M)

    for i in range(n):
        for j in range(n):
            if M[i][j] != M[j][i]:
                return False

    return True