'''
Death Knight Hero - 3249
'''

numero_batalhas = int(input())

vitorias = 0
for _ in range(numero_batalhas):
    jogada = input()
    armazena_jogada = ""
    venceu = True
    for habilidade in jogada:
        if habilidade == "D" and armazena_jogada == "C":
            venceu = False
        armazena_jogada = habilidade
    if venceu:
        vitorias += 1
print(vitorias)