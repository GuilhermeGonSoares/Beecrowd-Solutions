import math

def partesDoCirculo(numeroLados):
    return 1 + math.comb(numeroLados, 2) + math.comb(numeroLados, 4) #Forma de divir um circulo

n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    print(int(partesDoCirculo(n)))
    