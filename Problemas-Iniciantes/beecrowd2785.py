def soma_elementos_coluna(matriz, linha_inicial, coluna):
    soma = 0
    for i in range(linha_inicial, dimensao):
        soma += matriz[i][coluna]
    return soma
            
def coluna_principal(matriz, linha):
    menor_soma = 100*dimensao
    coluna_principal = 0
    for j in range(dimensao):
        soma = soma_elementos_coluna(matriz,0,j)
        if  soma < menor_soma:
            menor_soma = soma
            coluna_principal = j
        elif soma == menor_soma:
            a = verifica(matriz,linha +1, coluna_principal, j)
            menor_soma = a[0] + matriz[linha][a[1]]
            coluna_principal = a[1]

    return (menor_soma, coluna_principal)

def verifica(matriz,linha, coluna1, coluna2):
    soma1 = soma_elementos_coluna(matriz, linha, coluna1)
    soma2 = soma_elementos_coluna(matriz, linha, coluna2)
    
    if soma1 < soma2:
        return (soma1, coluna1)
    
    elif soma1 > soma2:
        return (soma2, coluna2)
    else:
        return verifica(matriz, linha + 1, coluna1, coluna2)
    
   
dimensao = int(input())
matriz = []
colunas_testadas = []

peso_minimo = 0
for _ in range(dimensao):
    matriz.append([int(x) for x in input().split()])

resultado = coluna_principal(matriz,0)
peso_minimo += resultado[0]
coluna_principal = resultado[1]
colunas_testadas.append(coluna_principal)


for linha in range(1, dimensao):
    colunas = sorted(colunas_testadas)
    coluna1 = colunas[0] - 1
    coluna2 = colunas[len(colunas_testadas) - 1] + 1
    if coluna1 >= 0 and coluna2 <= dimensao - 1:
        resultado = verifica(matriz,linha, coluna1, coluna2)
        peso_minimo += resultado[0] 
        colunas_testadas.append(resultado[1])
    else:
        if coluna1 >= 0 :
            peso_minimo += soma_elementos_coluna(matriz, linha, coluna1)
            colunas_testadas.append(coluna1)
        else:
            peso_minimo += soma_elementos_coluna(matriz, linha, coluna2)
            colunas_testadas.append(coluna2)
print(peso_minimo)

