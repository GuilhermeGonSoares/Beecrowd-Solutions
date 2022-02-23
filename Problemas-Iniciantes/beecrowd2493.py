def retorna_operador(lista):
    x = int(lista[0])
    y,z = map(int, lista[1].split("="))
    if x + y == z:
        return "+"
    if x*y == z:
        return "*"
    if x-y == z:
        return "-"
    return "I"


while True:
    try:
        expressoes = []
        pessoas_erraram = []
        
        quantidade_testes = int(input())
        for _ in range(quantidade_testes):
            expressoes.append(input().split())
        for _ in range(quantidade_testes):
            pessoa, indice, operador = map(str, input().split())
            indice = int(indice)
            operador_correto = retorna_operador(expressoes[indice-1])
            if operador_correto != operador:
                pessoas_erraram.append(pessoa)
        if len(pessoas_erraram) == quantidade_testes:
            print("None Shall Pass!")
        elif len(pessoas_erraram) == 0:
            print("You Shall All Pass!")
        elif len(pessoas_erraram) == 1:
            print(pessoas_erraram[0])
        else:
            pessoas_erraram = sorted(pessoas_erraram)
            for p in range(len(pessoas_erraram) - 1):
                print(pessoas_erraram[p], end = " ")
            print(pessoas_erraram[p+1])
                
        
    except EOFError:
        break