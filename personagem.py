import random
import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')      

class Personagem:
    def __init__(self, nome, pontos_vida_max, pontos_vida_atual, pontos_ataque, pontos_defesa, mao_cartas, energia):
        self.nome = nome
        self.pontos_vida_max = pontos_vida_max
        self.pontos_vida_atual = pontos_vida_atual
        self.pontos_ataque = pontos_ataque
        self.pontos_defesa = pontos_defesa
        self.mao_cartas = mao_cartas
        self.energia = energia
        
    def atacar (self, jogador_inimigo, jogador_atual = None):
        jogador_inimigo.pontos_vida_atual -= jogador_atual.pontos_ataque
    
    def usar_carta (self, prejudicado = None, beneficiado = None):
        from cartas import Carta_roubo
        from cartas import Carta_atordoamento
        from cartas import Carta_dano
        from cartas import Carta_cura
        limpar_tela ()
        print ("\n||      Mão de Cartas     ||\n")
        for i, cartas in enumerate (self.mao_cartas):
            print (f"Carta {i+1}: {cartas.nome}")     
        numero_carta_escolhida = int (input ("\nQual carta você quer usar?\n"))
        carta_escolhida = self.mao_cartas [numero_carta_escolhida - 1]
        if isinstance (carta_escolhida, Carta_roubo):
            carta_escolhida.usar_carta (prejudicado, beneficiado)
            print ("Carta de roubo usada")
        elif isinstance (carta_escolhida, Carta_atordoamento):
            carta_escolhida.usar_carta (prejudicado)
            print ("Carta de atordoamento usada")
        elif isinstance (carta_escolhida, Carta_dano):
            carta_escolhida.usar_carta (prejudicado, beneficiado)
            print ("Carta de dano usada")
        elif isinstance (carta_escolhida, Carta_cura):
            carta_escolhida.usar_carta (beneficiado)
            print ("Carta de cura usada")
            
    def comprar_carta (self, baralho_cartas):
        carta_comprada = random.sample (baralho_cartas, k = 1)
        self.mao_cartas.extend (carta_comprada)
        return (f"{self.nome} comprou a carta {carta_comprada}")
    
    def levar_dano (self):
        pass
    
    def listar_mao_cartas (self):
        print (self.mao_cartas)
        
    def mostrar_informacoes (self):
        print (f"\n{self.nome}\nVida: {self.pontos_vida_atual}\nAtaque: {self.pontos_ataque}\nDefesa: {self.pontos_defesa}\nEnergia: {self.energia}")
    
    def curar (self):
        pass