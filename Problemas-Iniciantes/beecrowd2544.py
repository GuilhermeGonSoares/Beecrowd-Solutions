'''
Kage Bunshin no Jutsu - 2544
'''

while True:
    try:
        copias = int(input())
        for i in range(copias):
            if 2**i == copias:
                print(i)
                break
        
    except EOFError:
        break