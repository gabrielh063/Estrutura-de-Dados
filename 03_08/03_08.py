nomes = []
total_nomes = 5
for i in range(total_nomes):
    tmp = input('digite um nome: ')
    nomes.append(tmp)
print('='*17)
for a in range(len(nomes)):
    print(f'Seja bem vindo {nomes[a].upper()}')