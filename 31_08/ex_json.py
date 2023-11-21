 #biblioteca para manipular arquivo json
import json

reg01={"nome": "transito", "idade": 10, "matriculado": True}
reg02={"nome": "otavio", "idade": 12, "matriculado": False}

dados= {"alunos":[reg01,reg02]}

json_str = json.dumps(dados)#serializa o dicionario para json/converte

print('Dicionario python')
print(dados)

print('Dicionario JSON')
print(json_str)

#salvar em arquivo
with open('basedados/dados.json', 'a') as json_file:
    json.dump(dados,json_file)
    