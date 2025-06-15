import forca
import advinhacao

print("Escolha seu jogo!")

print("(1) Forcar (2) Adivinhação")

jogo = int(input("Qual jogo ?"))

if (jogo == 1):
    print("Jogando da forca")
    forca.jogar()
elif (jogo == 2):
    advinhacao.jogar()
    print("Jogando da adivinhação")