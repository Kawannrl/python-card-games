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
        sorteio_cartas_iniciais = random.choices (self.baralho_cartas, k = 4)
        self.jogador2.mao_cartas.extend (sorteio_cartas_iniciais)
        
        while (self.jogador1.pontos_vida_atual > 0 and self.jogador2.pontos_vida_atual > 0):
            while self.jogador_atual.energia_atual > 0:
                if self.acao_jogador () == False:
                    break
                self.jogador_atual.mostrar_informacoes ()
                self.jogador_inimigo.mostrar_informacoes ()
            self.trocar_turno ()
            self.trocar_jogador ()
        print (self.acabar_jogo ())
    
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
        escolha_jogador = int(input (f"\n{self.jogador_atual.nome} escolha umas das opções: \n1 - Usar Carta \n2 - Atacar \n3 - Encerrar Turno\nOpção: "))
        if self.jogador_atual != self.jogador_inimigo:
            match escolha_jogador:
                case 1:
                    self.jogador_atual.usar_carta (self.jogador_inimigo, self.jogador_atual)
                    return True
                case 2:
                    mensagem = self.jogador_atual.atacar (self.jogador_inimigo, self.jogador_atual)
                    print (mensagem)
                    return True
                case 3:
                    print (f"Turno Encerrado! Vez de {self.jogador_inimigo.nome}")
                    return False
    
    def trocar_turno (self):
        self.turno_jogo += 1
        self.jogador1.energia_atual += 25
        self.jogador2.energia_atual += 25
        print (f"\n|||     {self.turno_jogo + 1}° Turno     |||\n")
    
    def trocar_jogador (self):
        self.trocas = self.jogador_atual
        self.jogador_atual = self.jogador_inimigo
        self.jogador_inimigo = self.trocas
        self.jogador_atual.comprar_carta (self.baralho_cartas)
    
    def acabar_jogo (self):
        if self.jogador1.pontos_vida_atual <= 0:
            return (f"\n|||||   PARABÉNS   |||||\n{self.jogador2.nome} venceu o jogo!")
        else:
            return (f"\n|||||   PARABÉNS   |||||\n{self.jogador1.nome} venceu o jogo!")
        
    def mostrar_mao (self):
        for carta in self.jogador_atual.mao_cartas:
            print (f"||     {carta.nome}      ||")
    
    def criar_baralho_cartas (self):
        nome = ("carta aumento vida máxima (Custo 30)")
        energia_gasta = 30
        descricao = ("sla")
        tipo_aumento = cartas.Tipo_Aumento.aumento_vida_max
        pontos_aumentado = 40
        
        nome = ("carta aumento energia máxima (Custo 20)")
        energia_gasta = 20
        descricao = ("sla")
        tipo_aumento = cartas.Tipo_Aumento.aumento_energia_max
        pontos_aumentado = 20
        
        nome = ("carta aumento defesa (Custo 20)")
        energia_gasta = 20
        descricao = ("sla")
        tipo_aumento = cartas.Tipo_Aumento.aumento_defesa
        pontos_aumentado = 30
        
        nome = ("carta aumento ataque (Custo 40)")
        energia_gasta = 40
        descricao = ("sla")
        tipo_aumento = cartas.Tipo_Aumento.aumento_ataque
        pontos_aumentado = 15
        
        carta_aumento = cartas.Carta_aumento (nome, energia_gasta, descricao, tipo_aumento, pontos_aumentado) 
        
        nome = ("dois caras numa moto (Custo 35)")
        energia_gasta = 35
        descricao = ("sla")
        
        carta_roubo = cartas.Carta_roubo (nome, energia_gasta, descricao)
        
        nome = ("casca de banana (Custo 80)")
        energia_gasta = 80
        descricao = ("sla")
        
        carta_atordoamento = cartas.Carta_atordoamento (nome, energia_gasta, descricao)
        
        nome = ("super carta de dano (Custo 40)")
        energia_gasta = 40
        descricao = ("sla")
        dano_causado = 15
        
        carta_dano = cartas.Carta_dano (nome, energia_gasta, descricao, dano_causado)
        
        nome = ("super carta de cura (Custo 25)")
        energia_gasta = 25
        descricao = ("sla")
        vida_curada = 35
        
        carta_cura = cartas.Carta_cura (nome, energia_gasta, descricao, vida_curada)
        
        self.baralho_cartas.append (carta_aumento)
        self.baralho_cartas.append (carta_roubo)
        self.baralho_cartas.append (carta_atordoamento)
        self.baralho_cartas.append (carta_dano)
        self.baralho_cartas.append (carta_cura)