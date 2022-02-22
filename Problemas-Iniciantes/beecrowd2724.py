'''
Ajude Patatatitu - 2724
'''

alfabeto_minusculo = "abcdefghijklmnopqrstuvwxyz"
numero = "0123456789"

def verifica_perigo(s_maior, s_menor, alfabeto, numero):
    for i in range(len(s_maior)):
        if s_maior[i] == s_menor[0]:
            contador = 0
            j = 0
            while (i+j <= len(s_maior) - 1) and j <= len(s_menor) - 1:
                if s_maior[i+j] == s_menor[j]:
                    contador += 1
                j += 1
            if contador == len(s_menor):
                if i+j == len(s_maior):
                    return True
                else:
                    if s_maior[i+j] not in alfabeto and s_maior[i+j] not in numero:
                        return True
    return False
                
testes = int(input())
for _ in range(testes):
    qtd_perigosos = int(input())
    perigosos = []
    for i in range(qtd_perigosos):
        perigosos.append(input())
    qtd_teste = int(input())
    
    for i in range(qtd_teste):
        eh_perigoso = False
        analisar = input()
        for elemento in perigosos:
            tamanho_analisar = len(analisar)
            tamanho_elemento = len(elemento)
            if tamanho_analisar >= tamanho_elemento:
                if verifica_perigo(analisar, elemento, alfabeto_minusculo, numero):
                    eh_perigoso = True
                    break
        if eh_perigoso:
            print("Abortar")
        else:
            print("Prossiga")
    if _ == testes - 1:
        break
    else:
        print()
                    


