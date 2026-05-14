import math

def calcular_distancia_total(percurso):
    distancia_total = 0.0
    for i in range(1, len(percurso)):
        x1, y1 = percurso[i - 1]
        x2, y2 = percurso[i]
        distancia = math.sqrt((x2 - x1)  **2 + (y2 - y1)  **2)
        distancia_total += distancia
    return distancia_total

percurso = [(0, 0), (3, 4), (6, 8)]
distancia_total = calcular_distancia_total(percurso)
print(f"Distância total percorrida: {distancia_total}")
