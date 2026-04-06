massa = float(input("Digite a massa inicial (g): "))

massa_inicial = massa
tempo = 0

while massa >= 0.5:
    massa = massa / 2
    tempo = tempo + 50

print("Massa inicial:", massa_inicial, "g")
print("Massa final:", massa, "g")
print("Tempo total:", tempo, "segundos")