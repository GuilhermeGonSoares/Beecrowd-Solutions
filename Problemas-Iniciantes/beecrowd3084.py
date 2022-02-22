
def retorna_minutos(angulo):
    return angulo//6
def retorna_horas(angulo):
    return angulo//30

while True:
    try:
        angulo_horas, angulo_minutos = map(int, input().split())
        horas = retorna_horas(angulo_horas)
        minutos = retorna_minutos(angulo_minutos)
        print(f"{horas:02d}:{minutos:02d}")
    
    except EOFError:
        break