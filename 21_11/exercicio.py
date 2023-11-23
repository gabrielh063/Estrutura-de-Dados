import random

def cria_matriz(N, M):
    matriz = [[random.randint(1, 100) for _ in range(M)] for _ in range(N)]    
    numeros_pares = 0
    for linha in matriz:
        for elemento in linha:
            if elemento % 2 == 0:
                numeros_pares += 1
    
    return matriz, numeros_pares
N = 3
M = 4
matriz_gerada, qtd_pares = cria_matriz(N, M)
print("Matriz gerada:")
for linha in matriz_gerada:
    print(linha)

print("\nQuantidade de números pares:", qtd_pares)
