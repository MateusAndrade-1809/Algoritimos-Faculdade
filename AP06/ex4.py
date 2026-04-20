palavra = input('Digite uma palavra: ')
contagem = 0

for vogais in palavra:
    if vogais in 'aeiou':
        contagem += 1
        
print(f'A palvra {palavra} tem {contagem} vogais')