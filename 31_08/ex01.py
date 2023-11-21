import json


#r abrir para leitura
#w abrir pra escrita(sobrescreve)
#a abrir pra escrita(anexa)
with open('basedados/dados.json', 'r') as arquivo:
    registros =json.load(arquivo)

print(arquivo)
