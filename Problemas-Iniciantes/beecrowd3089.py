'''
Presentes de Natal - 3089
'''
while True:
    n = int(input())
    if n == 0:
        break
    precos = [int(x) for x in input().split()]
    
    maior_preco = precos[0] + precos[-1]
    menor_preco = precos[0] + precos[-1]
    
    for i in range(n):
        soma = precos[i] + precos[-(i+1)]
        if soma > maior_preco:
            maior_preco = soma
        if soma < menor_preco:
            menor_preco = soma
    print(maior_preco, menor_preco)
    