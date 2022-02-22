'''
Umil Bolt - 2863
'''

while True:
    try:
        tentativas = int(input())
        menor = float(input())
        for i in range(1, tentativas):
            valor = float(input())
            if valor < menor:
                menor = valor
        print(menor)
    except EOFError:
        break