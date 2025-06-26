import random
import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')      

class Personagem:
    def __init__(self, nome, pontos_vida_max, pontos_vida_atual, pontos_ataque, pontos_defesa, pontos_defesa_max, mao_cartas, energia_atual, energia_max):
        self.nome = nome
        self.pontos_vida_max = pontos_vida_max
        self.pontos_vida_atual = pontos_vida_atual
        self.pontos_ataque = pontos_ataque
        self.pontos_defesa = pontos_defesa
        self.pontos_defesa_max = pontos_defesa_max
        self.mao_cartas = mao_cartas
        self.energia_atual = energia_atual
        self.energia_max = energia_max
        
    def atacar (self, jogador_inimigo, jogador_atual):
        
        if jogador_inimigo.pontos_defesa == 0:
            jogador_inimigo.pontos_vida_atual -= jogador_atual.pontos_ataque
        elif jogador_inimigo.pontos_defesa < jogador_atual.pontos_ataque:
            dano = jogador_atual.pontos_ataque - jogador_inimigo.pontos_defesa
            jogador_inimigo.pontos_defesa = 0
            jogador_inimigo.pontos_vida_atual -= dano
        else:
            jogador_inimigo.pontos_defesa -= jogador_atual.pontos_ataque
        # if jogador_inimigo.pontos_defesa <= 0:
        #     jogador_inimigo.pontos_vida_atual -= jogador_atual.pontos_ataque
        # else:
        #     jogador_inimigo.pontos_defesa = max (0, jogador_inimigo.pontos_defesa - jogador_atual.pontos_ataque)
        #     if jogador_inimigo.pontos_defesa < 0:
        #         jogador_inimigo.pontos_vida_atual -= jogador_atual.pontos_ataque
        jogador_atual.pontos_energia_atual = max (0, jogador_atual.pontos_energia_atual - 25)
        return (f"O {jogador_atual.nome} causou {jogador_atual.pontos_ataque} de dano à {jogador_inimigo.nome}")
    
    def usar_carta (self, prejudicado = None, beneficiado = None):
        from cartas import Carta_roubo
        from cartas import Carta_atordoamento
        from cartas import Carta_dano
        from cartas import Carta_cura
        from cartas import Carta_aumento
        limpar_tela ()
        print ("\n||      Mão de Cartas     ||\n")
        if self.energia_atual >= 0:
            for i, cartas in enumerate (self.mao_cartas):
                print (f"Carta {i+1}: {cartas.nome}")     
            numero_carta_escolhida = int (input ("\nQual carta você quer usar?\n"))
            carta_escolhida = self.mao_cartas.pop (numero_carta_escolhida - 1)
            if isinstance (carta_escolhida, Carta_roubo):
                carta_escolhida.usar_carta (prejudicado, beneficiado)
                return ("Carta de roubo usada")
            elif isinstance (carta_escolhida, Carta_atordoamento):
                carta_escolhida.usar_carta (beneficiado, prejudicado)
                return ("Carta de atordoamento usada")
            elif isinstance (carta_escolhida, Carta_dano):
                carta_escolhida.usar_carta (prejudicado, beneficiado)
                return ("Carta de dano usada")
            elif isinstance (carta_escolhida, Carta_cura):
                carta_escolhida.usar_carta (beneficiado)
                return ("Carta de cura usada")
            elif isinstance (carta_escolhida, Carta_aumento):
                carta_escolhida.usar_carta (beneficiado)
                return ("Carta de aumento usada")
            else:
                return (f"Você não tem energia suficiente para usar a carta")
        else:
            print ("Voce não tem mais energia para mais nenhuma ação")
            return
            
    def comprar_carta (self, baralho_cartas):
        carta_comprada = random.sample (baralho_cartas, k = 1)
        self.mao_cartas.extend (carta_comprada)
        return (f"{self.nome} comprou a carta {carta_comprada}")
        
    def mostrar_informacoes (self):
        print (f"     \n{self.nome}     ")
        print (f"     Vida: {self.pontos_vida_atual}/{self.pontos_vida_max}")
        print (f"     Ataque: {self.pontos_ataque}")
        print (f"     Defesa: {self.pontos_defesa}/{self.pontos_defesa_max}")
        print (f"     Energia: {self.energia_atual}/{self.energia_max}")