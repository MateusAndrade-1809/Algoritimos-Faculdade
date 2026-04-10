palavra = input('Digite uma palavra: ').lower()

c = 0
for l in palavra:
    if l in "aeiou": c += 1
print(c)
