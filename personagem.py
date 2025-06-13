class Personagem:
    def __init__(self, nome, pontos_vida_max, pontos_vida_atual, pontos_ataque, pontos_defesa, mao_cartas, energia):
        self.nome = nome
        self.pontos_vida_max = 100
        self.pontos_vida_atual = 100
        self.pontos_ataque = 10
        self.pontos_defesa = 20
        self.mao_cartas = []
        self.energia = 10
        
    def atacar (self):
        pass
    
    def usar_carta (self):
        pass
    
    def comprar_carta (self):
        pass
    
    def levar_dano (self):
        pass
    
    def listar_mao_cartas (self):
        pass
    
    def curar (self):
        pass