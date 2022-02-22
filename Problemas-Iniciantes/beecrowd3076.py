'''
Exercício de História - 3076
'''

while True:
    try:
        ano = int(input())
        if ano % 100 == 0:
            print(ano // 100)
        else:
            seculo = (ano // 100) + 1
            print(seculo)
        
        
    except EOFError:
        break