'''
Picos e Vales - 2162
'''

def verificaPaisagem(lista):
    analisa = lista[0]
    vale = False
    pico = False
    
    for i in range(1,len(lista)):
        if lista[i] == analisa:
            return 0
        if lista[i] > analisa:
            if pico:
                return 0
            else:
                pico = True
                vale = False
                
        if lista[i] < analisa:
            if vale:
                return 0
            else: 
                vale = True
                pico = False
        analisa = lista[i]
    
    return 1          
        

numero_de_medidas = int(input())

medidas = [int(x) for x in input().split()]

print(verificaPaisagem(medidas))


    