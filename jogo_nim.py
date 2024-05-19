# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 19:02:31 2024
Jogo NIM

# n = qt. inicial de peças
# m = nro. máximo de peças máximo possível de retirar em uma rodada.

@author: probe
"""


def computador_escolhe_jogada(n,m):
    x = 1
    while x <= m:
        if (n - x) % (m + 1) == 0:
            return x
        x += 1
    return m

def usuario_escolhe_jogada(n,m):
    while True:
        y = int(input("Quantas peças você vai tirar? "))
        if 1 <= y <= m and y <= n:
            return y
        else:
            print()
            print("Oops! Jogada inválida!. Tente de novo.")

def partida():
    global a
    global z
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    # Verifica a jogada inicial conforme a estratégia vencedora
    if n % (m + 1) == 0:
        print("Você começa!")
        jogador_atual = 'usuario'
    else:
        print("O computador começa!")
        jogador_atual = 'computador'
    # Inicia o loop do jogo
    while n > 0:
        if jogador_atual == 'usuario':
            jogada = usuario_escolhe_jogada(n, m)
            print()
            print("Você tirou", jogada, "peças.")
            print("Agora restam apenas", (n - jogada), "peças no tabuleiro.")
        else:
            jogada = computador_escolhe_jogada(n, m)
            print()
            print("O computador tirou", jogada, "peças.")
            print("Agora restam", (n - jogada), "peças no tabuleiro.")
        n -= jogada
        # Troca o jogador atual
        
        if jogador_atual == 'usuario':
            jogador_atual = 'computador'
        
        elif jogador_atual == 'computador' and n == 0:
            jogador_atual == 'computador'
        
        else:
            jogador_atual = 'usuario'
        
    # Exibe a mensagem de vitória para o vencedor
    if jogador_atual == 'usuario':
        print("Parabéns! Você ganhou!")
    elif a == 1:
        print("Fim do jogo! O computador ganhou!")
   
   
    if a == 2 and z <= 3:
        print("Fim do jogo! O computador ganhou!")
        return campeonato()
    
    elif a == 1:
        print()
        print("Fim do jogo! O computador ganhou!")
    
        
    
    else:
        print("Fim do jogo! O computador ganhou!")
        print()
        print("**** Final do campeonato! ****")
        print()
        print("Placar: Você 0 X 3 Computador")

def campeonato():
## Só precisa chamar a função partida() três vezes
    global a
    global z
    
    while z <= 3:
        print()
        print("**** Rodada", z, "****")
        z = z + 1
        return partida()
        
    

def main():
## Serve para iniciar o jogo
    global a
    global z
    print("\nBem-vindo ao jogo do NIM! Escolha:\n")
  
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    a = int(input("Digite a sua opção: "))
    if a == 1:
        print()
        print("\nVocê escolheu uma partida isolada!\n")
        return partida()
    if a == 2:
        print()
        print("Você escolheu um campeonato!")
        z = 1
        return campeonato()
    else:
        print()
        print("Opção inválida!")
        return main()

main()