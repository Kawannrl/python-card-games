import random
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

class Jogador:
    def __init__ (self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2

    def jogar_dados (self):
        
        while True:
            limpar_tela()
            valor_dado1 = random.randint (1, 6)
            valor_dado2 = random.randint (1, 6)

            print (f"{self.jogador1} tirou {valor_dado1}")
            print (f"{self.jogador2} tirou {valor_dado2}")

            if valor_dado1 > valor_dado2:
                print (f"{self.jogador1} é o primeiro a jogar!")
                break
            elif valor_dado2 > valor_dado1:
                print (f"{self.jogador2} é o primeiro a jogar!")
                break
            else:
                print("Empate! Jogando os dados novamente...\n")

if __name__ == "__main__":
    nome1 = input ("Informe o nome do Primeiro Jogador: ")
    nome2 = input ("Informe o nome do Segundo Jogador: ")

    jogador = Jogador (nome1, nome2)
    jogador.jogar_dados ()
