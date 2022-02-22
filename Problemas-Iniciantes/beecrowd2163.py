'''
O Despertar da Força - 2163
'''

n, m = map(int, input().split())
matriz = []

encontrouSabre = False

for i in range(n):
    matriz.append([int(x) for x in input().split()])

for i in range(1, n-1):
    for j in range(1,m-1):
        if matriz[i][j] == 42:
            if matriz[i-1][j] == matriz[i+1][j] == 7:
                if matriz[i][j+1] == matriz[i][j-1] == 7:
                    if matriz[i-1][j+1] == matriz[i-1][j-1] ==7:
                        if matriz[i+1][j+1] == matriz[i+1][j-1] == 7:
                            encontrouSabre = True
                            print(f"{i+1} {j+1}")
                            break
if not encontrouSabre:
    print(f"0 0")                        
            
            
            #elementoDeCima = matriz[i-1][j]
            #elementoDeBaixo = matriz[i+1][j]
            #elementoDireita = matriz[i][j+1]
            #elementoEsquerda = matriz[i][j-1]
            #elementoCimaDiagonalDir = matriz[i-1][j+1]
            #elementoCimaDiagonalEsq = matriz[i-1][j-1]
            #elementoBaixoDiagonalDir = matriz[i+1][j+1]
            #elementoBaixoDiagonalEsq = matriz[i+1][j-1]
        
                   