'''
TCC da Depressão Natalino - 2930
'''


e , d = map(int, input().split())

if e > d:
    print("Eu odeio a professora!")

elif d - e >= 3:
    print("Muito bem! Apresenta antes do Natal!")

else:
    print("Parece o trabalho do meu filho!")
    if d + 2 > 24:
        print("Fail! Entao eh nataaaaal!")
    else:
        print("TCC Apresentado!")