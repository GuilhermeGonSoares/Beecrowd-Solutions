'''
Attack on Gasparini - 3343
'''

tamanho_tita = {}

qtd_tita , tamanho_muralha = map(int, input().split())
todos_tita = input()
tamanho_tita["P"], tamanho_tita["M"], tamanho_tita["G"] = map(int, input().split())
lista_muralhas = [tamanho_muralha]*qtd_tita

pos_pequeno_parou = 0
pos_medio_parou = 0
pos_grande_parou = 0

for tipo in todos_tita:
    altura_tita = tamanho_tita[tipo]
    
    if tipo == "P":
        while lista_muralhas[pos_pequeno_parou] < altura_tita:
            pos_pequeno_parou += 1
        lista_muralhas[pos_pequeno_parou] -= altura_tita
    
    elif tipo == "M":
        while lista_muralhas[pos_medio_parou] < altura_tita:
            pos_medio_parou += 1
        lista_muralhas[pos_medio_parou] -= altura_tita
    
    else:
        while lista_muralhas[pos_grande_parou] < altura_tita:
            pos_grande_parou += 1
        lista_muralhas[pos_grande_parou] -= altura_tita

print(sorted([pos_pequeno_parou,pos_medio_parou,pos_grande_parou])[2] + 1)


'''

#### Nessa resolução estava dando Time limit Excessed mesmo apelando para uma busca binária
### Era só me atentar ao fato simples que se um tita médio ja conseguiu atravessar todas as muralhas anteriores e morreu na 
### muralha k, o próximo tita medio que virá tbm ira conseguir atravessar todas as outras k-1 muralhas, logo basta verifica
### a partir da muralha k.




def busca(lista, esquerda, direita, item):
    # 1) O elemento é maior que todos os elementos da lista:
    if direita == esquerda:
        return (esquerda+direita)//2
    if direita < esquerda:
        return esquerda
    meio = (esquerda + direita) // 2
    
    #2) Nosso palpite estava certo: o elemento está no meio do arranjo. Temos que verificar se a primeira ocorrência dele é no meio, antes do meio ou depois do meio
    if lista[meio] >= item:
        if lista[meio - 1] >= item:
            return busca(lista, esquerda, meio-1, item)
        else:
            return meio
    
    #3)Nosso palpite esta errado e o elemendo está mais a direita da lista:
    if lista[meio] < item:
        return busca(lista, meio + 1,direita,item)    

tamanho_tita = {}

qtd_tita , tamanho_muralha = map(int, input().split())
todos_tita = input()
tamanho_tita["P"], tamanho_tita["M"], tamanho_tita["G"] = map(int, input().split())
lista_muralhas = [tamanho_muralha]


qtd_muralha = 1

for i in range(qtd_tita):
    tipo_tita = todos_tita[i]
    altura_tita = tamanho_tita[tipo_tita]
    
    if len(lista_muralhas) == 0:
        lista_muralhas.append(tamanho_muralha)
        qtd_muralha += 1
    
    pos = busca(lista_muralhas,0, len(lista_muralhas) - 1, altura_tita)
    if pos == len(lista_muralhas) - 1:
        if lista_muralhas[-1] < altura_tita:
            lista_muralhas.append(tamanho_muralha - altura_tita)
            qtd_muralha += 1
        else:
            lista_muralhas[pos] -= altura_tita
            if lista_muralhas[pos] == 0:
                lista_muralhas.pop(pos)
    else:
        lista_muralhas[pos] -= altura_tita
        if lista_muralhas[pos] == 0:
            lista_muralhas.pop(pos)


print(qtd_muralha)
'''