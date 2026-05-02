def calcular_calorias(calorias_base, bonus=0):
    return calorias_base + bonus

def calcular_tempo_treino(tempo_principal, aquecimento=10):
    return tempo_principal + aquecimento

def analisar_desempenho(total_minutos):
    horas = total_minutos // 60
    minutos = total_minutos % 60
    return horas, minutos

def consolidar_treino(calorias, tempo, meta=300):
    atingido = False
    if calorias > meta:
        atingido = True
        return calorias - meta, atingido, 'Meta Atingida'
    else:
        return calorias - meta, atingido, 'Meta Não Atingida'
    