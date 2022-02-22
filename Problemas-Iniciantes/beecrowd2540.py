'''
Impeachment do Líder - 2540
'''


while True:
    try:
        numero_jogadores = int(input())
        votos = [int(x) for x in input().split()]
        if votos.count(1) >= 2*numero_jogadores/3:
            print("impeachment")
        else:
            print("acusacao arquivada")
        
    except EOFError:
        break