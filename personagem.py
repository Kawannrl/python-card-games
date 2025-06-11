class Personagem:
    def __init__(self, nome, pontos_vida_max, pontos_vida_atual, pontos_ataque, pontos_defesa, mao_cartas, energia):
        self.nome = nome
        self.pontos_vida_max = 100
        self.pontos_vida_atual = pontos_vida_atual
        self.pontos_ataque = 10
        self.pontos_defesa = 20
        self.mao_cartas = mao_cartas
        self.energia = 10
        
    