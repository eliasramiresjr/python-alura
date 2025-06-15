import random

def jogar():

    print("Bem vindo ao jogo de adivinhação")

    numero_secreto = (random.randrange(1, 101))
    tentativas = 0
    pontos = 1000
    # rodada = 1

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível: "))
    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 15
    else:
        tentativas = 5

    # while (rodada <= tentativas):
    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Digite um entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez: {}".format(pontos))
            break
        else:
            if (maior):
                print("Você errou número maior")
            elif (menor):
                print("Você errou número menor")
            # rodada = rodada + 1
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

    print("O número era:", numero_secreto)
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()