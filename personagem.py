import random

class Personagem:
    def __init__(self, nome, pontos_vida_max, pontos_vida_atual, pontos_ataque, pontos_defesa, mao_cartas, energia):
        self.nome = nome
        self.pontos_vida_max = 200
        self.pontos_vida_atual = 100
        self.pontos_ataque = 20
        self.pontos_defesa = 40
        self.mao_cartas = []
        self.energia = 10
        
    def atacar (self):
        pass
    
    def usar_carta (self):
        pass
    
    def comprar_carta (self, baralho_cartas):
        carta_comprada = random.sample (baralho_cartas, k = 1)
        self.mao_cartas.extend (carta_comprada)
        return (f"{self.nome} comprou a carta {carta_comprada.nome}")
    
    def levar_dano (self):
        pass
    
    def listar_mao_cartas (self):
        pass
    
    def curar (self):
        pass