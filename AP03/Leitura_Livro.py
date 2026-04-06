'''
Uma pessoa deseja planejar quanto tempo levará para terminar a leitura de um livro. Para isso, ela decidiu criar um pequeno programa que faça uma estimativa do tempo total necessário para concluir a leitura, considerando alguns fatores relacionados ao tamanho do livro e ao ritmo de leitura.

O programa deve solicitar ao usuário informações sobre o livro e sobre seus hábitos de leitura: o número total de páginas do livro, o número médio de palavras por página, a velocidade média de leitura em palavras por minuto e a quantidade de minutos disponíveis para leitura por dia.

A partir dessas informações, o programa deve estimar primeiro o número total de palavras do livro. Em seguida, deve calcular quanto tempo total de leitura será necessário, primeiro em minutos e depois convertido para horas. Por fim, considerando o tempo diário disponível para leitura, o programa deve estimar quantos dias aproximadamente serão necessários para terminar o livro.

Ao final, o programa deve apresentar um pequeno relatório organizado contendo essas informações calculadas.

Saída esperada:

Planejamento de leitura
-----------------------
Total de palavras no livro: ...
Tempo total de leitura (minutos): ...
Tempo total de leitura (horas): ...
Dias estimados para terminar o livro: ... 
'''

paginas = int(input('Qual o total de paginas do livro: '))
palavras_pagina = int(input('Qual o numero medio de palavras por pagina: '))
velocidade_leitura = int(input('Qual a velocidade media de leitura(palavras por minuto): '))
disponibilidade = int(input('Quanto tempo em minutos voce tem para ler por dia: '))
total_palavras_livro = palavras_pagina * paginas
tempo_total_leitura = total_palavras_livro / velocidade_leitura
terminar_livro = tempo_total_leitura / disponibilidade
print(f'o total de palavras do livro é de {total_palavras_livro}')
print(f'O tempo total de leitura é de {tempo_total_leitura} minutos')
print(f'O tempo que sera para terminar o livro sera de {terminar_livro} dias')