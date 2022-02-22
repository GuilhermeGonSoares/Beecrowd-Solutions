'''
Tempestade de Corvos - 2203

'''
from math import sqrt
def distancia_a_ser_percorrida(xf,yf,xi,yi,vi):
    distancia_inicial = sqrt((xf-xi)**2 +(yf-yi)**2)
    distancia_fuga = 1.5*vi
    
    return distancia_inicial + distancia_fuga

while True:
    try:
        xf, yf, xi, yi, vi, r1, r2 = map(int, input().split())
        distancia_necessaria = distancia_a_ser_percorrida(xf,yf,xi,yi,vi)
        distancia_possivel = r1 + r2
        if distancia_possivel >= distancia_necessaria:
            print("Y")
        else:
            print("N")
    except EOFError:
        break
