import forca
import adivinhacao

def escolher_jogo():
    print("***********************")
    print("Qual jogo deseja jogar?")
    print("***********************\n")

    print("1- Adivinhação")
    print("2- Jogo da Forca")

    jogo = int(input())

    if(jogo == 1):
        adivinhacao.jogar_adivinhacao()
    elif(jogo == 2):
        forca.jogar_forca()

if(__name__ == "__main__"):
    escolher_jogo()