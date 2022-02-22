def verifica_placa(x,y,x1,y1):
        if x1 <= x and y1 <= y:
            return True
        if x1 <= y and y1 <= x:
            return True
        return False

while True:
    try:
        x ,y, m = map(int, input().split())
        for _ in range(m):
            x1,y1 = map(int, input().split())
            if verifica_placa(x,y,x1,y1):
                print("Sim")
            else:
                print("Nao")
    except EOFError:
        break
