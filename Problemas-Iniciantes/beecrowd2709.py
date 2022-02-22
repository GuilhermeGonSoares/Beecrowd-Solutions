'''
As Moedas de Robbie - 2709
'''

from math import sqrt

def verifica_primo(numero):
    if numero == 0 or numero == 1:
        return False
    for i in range(2, int(sqrt(numero)) + 1): #Não é necessário fazer um for por todos os elementos até o próprio numero, o Bizu é fazer até a raiz dele
        if numero % i == 0:
            return False
    return True

while True:
    try:
        soma_moedas = 0
        
        qtd_moedas = int(input())
        
        pilha_moedas = []
        for _ in range(qtd_moedas):
            pilha_moedas.append(int(input()))
        
        salto = int(input())
        
        for i in range(1,qtd_moedas+1,salto):
            soma_moedas += pilha_moedas[-i] # Preciso pegar o último elemento que foi colocado (É uma pilha de moedas)
        
        if verifica_primo(soma_moedas):
            print("You’re a coastal aircraft, Robbie, a large silver aircraft.")        
        else:
            print("Bad boy! I’ll hit you.")    
      
        
    except EOFError:
        break
