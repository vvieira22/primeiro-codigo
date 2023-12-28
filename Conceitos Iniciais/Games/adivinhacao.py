import os
import random

def jogar_adivinhacao():
    print("********************************")
    print("BEM VINDO AO JOGO DE ADIVINHAÇÃO")
    print("********************************\n")

    print("Qual nível de dificuldade ?\n")
    print("1 - FÁCIL  ")
    print("2 - MÉDIO  ")
    print("3 - DIFÍCIL")
    nivel_dificuldade = int(input())
    pontuacao = 100

    if(nivel_dificuldade == 1):
        total_tentativas = 10
    elif(nivel_dificuldade == 2):
        total_tentativas = 5
    else:
        total_tentativas = 3

    numero_secreto = random.randrange(1,11)

    for i in range(1, total_tentativas + 1):
        os.system('cls')
        print(numero_secreto)
        print(f"Total de tentativas: {i} de {total_tentativas}")
        numero_digitado = int(input("Digite um número: "))

        if(numero_digitado == numero_secreto):
            os.system('cls')
            print("Você acertou!! :)")
            print("Pontuação final: ", pontuacao)    
            break
        else:
            if(numero_digitado > numero_secreto):
                input("Você errou, foi maior que o número secreto.")
                pontuacao = pontuacao - abs((numero_secreto - numero_digitado))
            else:
                input("Você errou, foi menor que o número secreto.")
                pontuacao = pontuacao - abs((numero_secreto - numero_digitado))
        if(i == total_tentativas):
            print("Fim de jogo, acabaram as tentativas!")
            break
        continue