'''
Uma pequena empresa de entregas deseja estimar o gasto semanal de combustível de um de seus veículos. Para isso, o gerente decidiu criar um pequeno programa que ajude a fazer essa estimativa rapidamente.

O programa deve considerar que o veículo realiza várias entregas por dia, percorrendo uma certa distância média em cada entrega. Além disso, o veículo trabalha durante vários dias na semana.

Para realizar a estimativa, o programa deve solicitar ao usuário as seguintes informações:

distância média percorrida em cada entrega (em km)

número médio de entregas realizadas por dia

número de dias de trabalho na semana

consumo médio do veículo em quilômetros por litro (km/l)

preço do combustível em reais por litro

A partir dessas informações, o programa deve calcular:

a distância total percorrida por dia

a distância total percorrida na semana

a quantidade de combustível necessária na semana

o custo total estimado de combustível na semana
'''

distancia_entrega = int(input('Qual a distancia meida de cada entrega: '))
entregas_dia = int(input('Qual o numero de entregas realizadas por dia(km): '))
trabalho_semana = int(input('Qual o numero de dias trabalhados na semana: '))
consumo_veiculo = int(input('Qual o consumo medio do veiculo(km/l): '))
preco_combustivel = int(input('Qual o preço do combustivel: '))

distancia_total_dia = distancia_entrega * entregas_dia
distancia_total_semana = distancia_total_dia * trabalho_semana
combustivel_semana = distancia_total_semana / consumo_veiculo
custo_total_combustivel = combustivel_semana * preco_combustivel

print(f'A distancia total percorrida por dia é de {distancia_total_dia}km')
print(f'A dsitancia total percorrida na semana é de {distancia_total_semana}km')
print(f'O combustivel total gasto na semana é de {combustivel_semana} litros')
print(f'O custo total gasto de combustivel na semana é de R${custo_total_combustivel}')