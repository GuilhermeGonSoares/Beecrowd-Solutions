    
casoTeste = 0
while True:
    meteoritoNaFazenda = 0
    x1,y1,x2,y2 = map(int, input().split())
    if x1 == y1 == x2 == y2 == 0: #Verifica se a entrada é X1 = Y1 = X2 = Y2 = 0. Isso simboliza final da entrada
        break
   
    casoTeste += 1
    quantidadeCasos = int(input())
    
    for i in range(quantidadeCasos):
        x, y = map(int, input().split())
        if (x1 <= x <= x2) and (y2 <= y <= y1): #Verifica se está dentro do retângulo.
            meteoritoNaFazenda += 1 #Incrementa no contador de meteoritos que acertaram a fazenda.
    print(f"Teste {casoTeste}")
    print(meteoritoNaFazenda)

