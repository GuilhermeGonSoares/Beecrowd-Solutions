numeroDeCasos = int(input())
for _ in range(numeroDeCasos):
    analisar = input()
    if "=" in analisar:
        print("skipped")
    else:
        posDoMais = analisar.find("+")
        numero1 = int(analisar[:posDoMais])
        numero2 = int(analisar[posDoMais + 1:])
        print(numero1 + numero2)