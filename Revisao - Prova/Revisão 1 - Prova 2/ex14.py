def calcular_bonus(pontos):
    if pontos > 50:
        return 100
    else:
        return 10
    
numero_funcionarios = int(input('Digite o numero de funcionarios da empresa: '))

for i in range(numero_funcionarios):    
    funcionarios = set()

    nome = int(input('Digite a nota do funcionario na sua empresa: '))

    funcionarios.add(nome)