def verifica_impar(numero):
    if numero % 2 == 1:
        return True
    return False

numero_de_estrelas = int(input())
quantidade_carneiros  = [int(x) for x in input().split()]

i = 0
encontrou_par = False
contador = 0
while  0 <= i < len(quantidade_carneiros):
    if verifica_impar(quantidade_carneiros[i]):
        if quantidade_carneiros[i] == 1:
            contador += 1
        if quantidade_carneiros[i] > 0:
            quantidade_carneiros[i] -= 1
        i += 1
    else:
        encontrou_par = True
        if quantidade_carneiros[i] > 0:
            quantidade_carneiros[i] -= 1
        break


carneiros_nao_roubados = sum(quantidade_carneiros)
if encontrou_par:
    print(i+1 , carneiros_nao_roubados -i + contador)
else:
    print(i, carneiros_nao_roubados)

'''
#Essa segunda solução passa novamente pela lista ao encontrar um par o que deixou o tempo de execução maior

def verifica_impar(numero):
    if numero % 2 == 1:
        return True
    return False

numero_de_estrelas = int(input())
quantidade_carneiros  = [int(x) for x in input().split()]

i = 0
estrelas_roubadas = 0
encontrou_par = False
while  0 <= i < len(quantidade_carneiros):
    if verifica_impar(quantidade_carneiros[i]):
        if quantidade_carneiros[i] > 0:
            quantidade_carneiros[i] -= 1
        i += 1
        estrelas_roubadas += 1
    else:
        encontrou_par = True
        if quantidade_carneiros[i] > 0:
            quantidade_carneiros[i] -= 1
        i -= 1
carneiros_nao_roubados = sum(quantidade_carneiros)
if encontrou_par:
    print(estrelas_roubadas +1 , carneiros_nao_roubados)
else:
    print(estrelas_roubadas, carneiros_nao_roubados)
'''