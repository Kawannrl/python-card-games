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
    pontos_defesa_max = 100
    mao_cartas = []
    energia_atual = 100
    energia_max = 140
    
    personegem1 = Personagem (nome1, pontos_vida_max, pontos_vida_atual, pontos_ataque, pontos_defesa, pontos_defesa_max, mao_cartas, energia_atual, energia_max)
    
    nome = ("Mago da Luz")
    pontos_vida_max = 200
    pontos_vida_atual = 100
    pontos_ataque = 20
    pontos_defesa = 50
    pontos_defesa_max = 100
    mao_cartas = []
    energia_atual = 100
    energia_max = 140
    
    personegem2 = Personagem (nome2, pontos_vida_max, pontos_vida_atual, pontos_ataque, pontos_defesa, pontos_defesa_max, mao_cartas, energia_atual, energia_max)
    
    partida = Partida (personegem1, personegem2)
    partida.iniciar_jogo ()