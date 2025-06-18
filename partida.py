import random
from enum import Enum
import cartas
from personagem import Personagem

class Escolha_jogador (Enum):
    escolha_ataque = 1
    escolha_usar_carta = 2

class Partida:
    def __init__(self, jogador1: Personagem, jogador2: Personagem):
        self.turno_jogo = 0
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.jogador_atual = None
        self.baralho_cartas = []
        
    def iniciar_jogo (self):
        self.jogador_atual = self.jogar_dados ()
        self.criar_baralho_cartas ()
        sorteio_cartas_iniciais = random.choices (self.baralho_cartas, k = 4)
        self.jogador1.mao_cartas.extend (sorteio_cartas_iniciais)
        self.jogador2.mao_cartas.extend (sorteio_cartas_iniciais)
        self.acao_jogador ()
    
    def jogar_dados (self):
        
        while True:
            valor_dado1 = random.randint (1, 6)
            valor_dado2 = random.randint (1, 6)

            print (f"{self.jogador1.nome} tirou {valor_dado1}")
            print (f"{self.jogador2.nome} tirou {valor_dado2}")

            if valor_dado1 > valor_dado2:
                print (f"\n{self.jogador1.nome} é o primeiro a jogar!")
                jogador_atual = self.jogador1
                self.jogador_inimigo = self.jogador2
                return jogador_atual
            elif valor_dado2 > valor_dado1:
                print (f"\n{self.jogador2.nome} é o primeiro a jogar!")
                jogador_atual = self.jogador2
                self.jogador_inimigo = self.jogador1
                return jogador_atual
            else:
                print("\nEmpate! Jogando os dados novamente...\n")
                
    def acao_jogador (self):
        escolha_jogador = int(input (f"\nEscolha umas das opções: \n1 - Usar Carta \n2 - Atacar \n3 - Comprar Carta \nOpção: "))
        if self.jogador_atual != self.jogador_inimigo:
            match escolha_jogador:
                case 1:
                    self.jogador_atual.usar_carta (self.jogador_inimigo, self.jogador_atual)
                case 2:
                    Personagem.atacar ()
                case 3:
                    Personagem.comprar_carta ()  
                
    
    def trocar_turno (self):
        pass
    
    def trocar_jogador (self):
        pass
    
    def acabar_jogo (self):
        pass
    
    def criar_baralho_cartas (self):
        # nome = ("carta aumento vida máxima")
        # energia_gasta = 10
        # descricao = ("sla")
        # tipo_aumento = 
        # pontos_aumentado = 
        
        # nome = ("carta aumento energia máxima")
        # energia_gasta = 10
        # descricao = ("sla")
        # tipo_aumento = 
        # pontos_aumentado = 
        
        # nome = ("carta aumento defesa")
        # energia_gasta = 10
        # descricao = ("sla")
        # tipo_aumento = 
        # pontos_aumentado = 
        
        # nome = ("carta aumento ataque")
        # energia_gasta = 10
        # descricao = ("sla")
        # tipo_aumento = 
        # pontos_aumentado = 
        
        nome = ("dois caras numa moto")
        energia_gasta = 25
        descricao = ("sla")
        
        carta_roubo = cartas.Carta_roubo (nome, energia_gasta, descricao)
        
        nome = ("casca de banana")
        energia_gasta = 30
        descricao = ("sla")
        
        carta_atordoamento = cartas.Carta_atordoamento (nome, energia_gasta, descricao)
        
        nome = ("super carta de dano")
        energia_gasta = 10
        descricao = ("sla")
        dano_causado = 15
        
        carta_dano = cartas.Carta_dano (nome, energia_gasta, descricao, dano_causado)
        
        nome = ("super carta de cura")
        energia_gasta = 20
        descricao = ("sla")
        vida_curada = 15
        
        carta_cura = cartas.Carta_cura (nome, energia_gasta, descricao, vida_curada)
        
        self.baralho_cartas.append (carta_roubo)
        self.baralho_cartas.append (carta_atordoamento)
        self.baralho_cartas.append (carta_dano)
        self.baralho_cartas.append (carta_cura)