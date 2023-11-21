import json

bancodados = {}
with open('basedados/dados_prova.json', 'r') as arquivo:
    bancodados = json.load(arquivo)

nomes = []

for nome in bancodados.values():
    nomes.append(nome['nome'])
print(sorted(nomes))
print('='*100)
idades = [func['idade'] for func in bancodados.values()]

idade_max = max(idades)

velho = [func for func in bancodados.values() if func['idade'] == idade_max]

for funcionario in velho:
    print("funcionario mais velho:", funcionario['nome'])
print('='*100)
idades = [funcionario['idade'] for funcionario in bancodados.values()]

idade_min = min(idades)

novo = [funcionario for funcionario in bancodados.values() if funcionario['idade'] == idade_min]

for funcionario in novo:
    print("funcionario mais novo:", funcionario['nome']) 
print('='*100)
salario = [funcionario['salario'] for funcionario in bancodados.values()]

salario_max= max(salario)

maior_salario = [funcionario for funcionario in bancodados.values() if funcionario['salario'] == salario_max]

for funcionario in maior_salario:
    print("Funcionário com maior salário:", funcionario['nome'])

print('='*100)

salario = [funcionario['salario'] for funcionario in bancodados.values()]

salario_min = min(salario)

menor_salario = [funcionario for funcionario in bancodados.values() if funcionario['salario'] == salario_min]

for funcionario in menor_salario:
    print("Funcionário com menor salário:", funcionario['nome'])