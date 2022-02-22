'''
Dividindo os Trabalhos I - 2715
'''


while True:
    try:
        n = int(input())
        problemas = [int(x) for x in input().split()]
        
        rangel = sum(problemas)
        gugu = 0
        menor_diferenca = rangel - gugu
        for i in range(1,n+1):
            rangel -= problemas[-i]
            gugu += problemas[-i]
            d = abs(rangel - gugu)
            if d <= menor_diferenca:
                menor_diferenca = abs(d)
            else:
                break
        print(menor_diferenca)
        
    except EOFError:
        break