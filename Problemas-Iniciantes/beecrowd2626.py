'''
Turma do JB8 - 2626
'''



def define_ganhador(lista, palavra):
    pos= lista.index(palavra)
    if pos == 0:
        print("Os atributos dos monstros vao ser inteligencia, sabedoria...")
    elif pos == 1:
        print("Iron Maiden's gonna get you, no matter how far!")
    else:
        print("Urano perdeu algo muito precioso...")

while True:
    try:
        dodo, leo, pepper = map(str,input().split())
        jogadas = [dodo, leo, pepper] #para quem jogou pedra ou tesoura ou papel(index = 0 ->dodo, index = 1 ->leo, index = 2->pepper)
        dic = {"papel" : 0, "pedra": 0, "tesoura": 0}
        dic[dodo] += 1
        dic[leo] += 1
        dic[pepper] += 1
        if dic["papel"] == dic["pedra"] == dic["tesoura"] == 1:
            print("Putz vei, o Leo ta demorando muito pra jogar...")
        elif dodo == leo == pepper:
            print("Putz vei, o Leo ta demorando muito pra jogar...")
        
        elif dic["tesoura"] == 2 and dic["papel"] == 1:
            print("Putz vei, o Leo ta demorando muito pra jogar...")
        
        elif dic["pedra"] == 2 and dic["tesoura"] == 1:
            print("Putz vei, o Leo ta demorando muito pra jogar...")
        
        elif dic["papel"] == 2 and dic["pedra"] == 1:
            print("Putz vei, o Leo ta demorando muito pra jogar...")
            
        elif dic["tesoura"] == 1 and dic["papel"] == 2:
            define_ganhador(jogadas,"tesoura")
        elif dic["pedra"] == 1 and dic["tesoura"] == 2:
            define_ganhador(jogadas, "pedra")
        elif dic["papel"] == 1 and dic["pedra"] == 2:
            define_ganhador(jogadas, "papel")
            
    except EOFError:
        break