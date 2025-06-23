import os
from personagem import Personagem
from partida import Partida


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')  

if __name__ == "__main__":
    limpar_tela ()
    nome1 = input ("Informe o nome do Primeiro Jogador: ")
    nome2 = input ("Informe o nome do Segundo Jogador: ")
    
    nome = ("Mago Sombrio")
    pontos_vida_max = 200
    pontos_vida_atual = 100
    pontos_ataque = 20
    pontos_defesa = 50
    mao_cartas = []
    energia = 100
    
    personegem1 = Personagem (nome1, pontos_vida_max, pontos_vida_atual, pontos_ataque, pontos_defesa, mao_cartas, energia)
    
    nome = ("Mago da Luz")
    pontos_vida_max = 200
    pontos_vida_atual = 100
    pontos_ataque = 20
    pontos_defesa = 50
    mao_cartas = []
    energia = 100
    
    personegem2 = Personagem (nome2, pontos_vida_max, pontos_vida_atual, pontos_ataque, pontos_defesa, mao_cartas, energia)
    
    partida = Partida (personegem1, personegem2)
    partida.iniciar_jogo ()