# Crie duas listas em python, uma para armazenar o nome e outra lista para armazenar a idade de 5 pessoas. posteriormente indique quais pessoas tem 18 anos ou maise quantas pessoas sao menores de idade
"""
jose, 10 anos
joaquim, 19 anos
jailton, 30 anos
juarez, 5 anos
joao, 18 anos
--> sao maiores de idade, joaquim jailton joao
--> sao menores de idade, jose juarez
"""

nomes = []
idade = []
total_nomes = 5
for i in range(total_nomes):
    tmp = input(f'Digite o {i + 1}* nome: ')
    nomes.append(tmp)
    tmp1 = int(input(f'Digite a {i +1}* idade: '))
    idade.append(tmp1)
    

