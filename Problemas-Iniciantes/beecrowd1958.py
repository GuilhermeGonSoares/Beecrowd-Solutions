'''
Notação Científica - 1958
'''
contador = 0
numero = input()
if float(numero) == 0:
    positivo = True
    if numero[0] == '-':
        positivo = False
        numero = numero[1:]
    if positivo:
        print(f"+{float(numero):.4f}E+00")
    else:
        print(f"-{float(numero):.4f}E+00")
        
else:

    numero = float(numero)

    if numero >= 1 or numero <= -1:
        while abs(numero) // 10 >= 1:
            contador += 1
            numero = numero / 10
        if numero > 0:
            print(f"+{numero:.4f}E+{contador:02d}")
        else:
            print(f"{numero:.4f}E+{contador:02d}")

    else:
        while abs(numero) < 1:
            contador += 1
            numero = numero*10
        if numero > 0:
            print(f"+{numero:.4f}E-{contador:02d}")
        else:
            print(f"{numero:.4f}E-{contador:02d}")

