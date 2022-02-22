'''
Evitando Chuva - 2813
'''



quantidade_de_dias = int(input())

ficou_casa, ficou_trabalho = 0,0
qtd_casa, qtd_trabalho = 0,0
for _ in range(quantidade_de_dias):
    ida, volta = map(str, input().split())
    if ida == "sol":
        if volta == "chuva":
            ficou_trabalho -= 1
            if ficou_trabalho < 0:
                ficou_trabalho = 0
                qtd_trabalho += 1
            ficou_casa += 1  
    if ida == "chuva":
        ficou_casa -= 1
        if ficou_casa < 0:
            ficou_casa = 0
            qtd_casa += 1
        ficou_trabalho += 1
        if volta == "chuva":
            ficou_trabalho -= 1
            if ficou_trabalho < 0:
                ficou_trabalho = 0
                qtd_trabalho += 1
            ficou_casa += 1

print(qtd_casa, qtd_trabalho)
            
                
        
            