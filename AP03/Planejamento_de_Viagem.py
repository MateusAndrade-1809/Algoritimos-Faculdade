'''
Um motorista deseja estimar o custo de combustível de uma viagem.

Leia:

distância da viagem (km)
consumo do carro (km/l)
preço do combustível (R$/l)
Calcule o quantidade de litros necessários para a viagem, e o custo total da viagem. Imprima os resultados na tela.

Saída esperada:

Planejamento de viagem
----------------------
Litros necessários: ...
Custo estimado: ...
'''
distancia = int(input('Qual a distancia da viagem (em km): '))
consumo_carro = float(input('Qual o consumo do carro (em km/l): '))
preco_combustivel = float(input('Qual o preço do combustivel: '))
litros_nec = distancia / consumo_carro
custo_estimado = preco_combustivel * litros_nec
print(f'os litros necessarios é de {litros_nec:.2f}')
print(f'o consumo estimado é de {custo_estimado}')
