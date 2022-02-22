'''
Desviando de Árvores de Natal - 3042
'''


while True:
    m = int(input())
    if m == 0:
        break
    pos_personagem = 1 # 0 -> esquerda / 1-> meio / 2 -> direita
    toques = 0
    for _ in range(m):
        estagio = [int(x) for x in input().split()]
        if 1 in estagio:
            nova_posicao = estagio.index(0)
            if nova_posicao != pos_personagem:
                toques += abs(pos_personagem - nova_posicao)
                pos_personagem = nova_posicao
    print(toques)
