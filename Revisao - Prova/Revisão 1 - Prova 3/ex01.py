sensores = {}
invalidos = 0

maior_temperatura_geral = None
sensor_maior_temperatura = ''

try:
    with open('leituras.txt', 'r') as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(';')

            if len(dados) != 3:
                invalidos += 1
            else:
                codigo = dados[0]
                data = dados[1]

                try:
                    temperatura = float(dados[2])

                    if codigo not in sensores:
                        sensores[codigo] = {
                            'quantidade': 0,
                            'soma': 0,
                            'menor': temperatura,
                            'maior': temperatura
                        }

                    sensores[codigo]['quantidade'] += 1
                    sensores[codigo]['soma'] += temperatura

                    if temperatura < sensores[codigo]['menor']:
                        sensores[codigo]['menor'] = temperatura

                    if temperatura > sensores[codigo]['maior']:
                        sensores[codigo]['maior'] = temperatura

                    if maior_temperatura_geral is None or temperatura > maior_temperatura_geral:
                        maior_temperatura_geral = temperatura
                        sensor_maior_temperatura = codigo

                except ValueError:
                    invalidos += 1

    with open('relatorio_sensores.txt', 'w') as relatorio:
        for codigo in sensores:
            quantidade = sensores[codigo]['quantidade']
            menor = sensores[codigo]['menor']
            maior = sensores[codigo]['maior']
            media = sensores[codigo]['soma'] / quantidade

            linha_relatorio = f'{codigo};{quantidade};{menor:.2f};{maior:.2f};{media:.2f}\n'
            relatorio.write(linha_relatorio)

        relatorio.write(f'Linhas inválidas: {invalidos}\n')

        if maior_temperatura_geral is not None:
            relatorio.write(f'Sensor com maior temperatura: {sensor_maior_temperatura} - {maior_temperatura_geral:.2f}\n')

    print('Relatório gerado com sucesso.')
    print(f'Quantidade de linhas inválidas: {invalidos}')

    if maior_temperatura_geral is not None:
        print(f'Sensor com maior temperatura: {sensor_maior_temperatura}')
        print(f'Maior temperatura registrada: {maior_temperatura_geral:.2f}')

except FileNotFoundError:
    print('Arquivo leituras.txt não encontrado.')
        