import os
import random

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def menu():
    resposta = ""
    while(resposta!= "-1"):
        os.system('cls')
        print("**************************")
        print("BEM VINDO AO JOGO DE FORCA")
        print("**************************")

        print("(1)-> JOGAR")
        print("(2)-> CADASTRAS PALAVRAS")
        print("(3)-> VER PALAVRAS CADASTRADAS")
        print("(-1)-> SAIR")
        print("**************************")
        resposta = input()
        if(resposta == "1"):
            jogar()
        if(resposta == "2"):
            cadastrar_palavra_secreta()
        if(resposta == "3"):
            print("Em Desenvolvimento")
        elif(resposta == "-1"):
            os.system('cls')
            print("Obrigado por jogar! :)")
        else:
            os.system('cls')
            print("Você Digitou uma opção inválida!")

def definir_palavra_secreta():
    palavras = []
    with open("lista_palavras.txt", "r", encoding="utf-8") as arquivo:
        for palavra in arquivo:
            palavras.append(palavra.strip())
    return palavras[random.randrange(0, len(palavras))]

def cadastrar_palavra_secreta():
    palavra = ""
    while(not palavra=="-1"):
        print("Digite a palavra a ser cadastrada!")
        print("-1 para cancelar e sair.")
        palavra = input()
        if(palavra=="-1"):
            break

        with open("lista_palavras.txt", "r", encoding="utf-8") as arquivo:
            if palavra not in arquivo.read():
                with open("lista_palavras.txt", "a", encoding="utf-8") as arquivo:
                    arquivo.write(palavra)
                    arquivo.write("\n")
                    os.system('cls')
                    print("Cadastrado com sucesso!")
            else:
                os.system('cls')
                print(f'Ocorreu um erro, talvez {palavra} já esteja cadastrada!')

def esconder_palavra_secreta(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def jogar():
    palavra_secreta = definir_palavra_secreta().lower()
    enforcou = False
    acertou = False
    erros = 0
    letras_chutadas = []
    lista_letras_palavra_secreta = esconder_palavra_secreta(palavra_secreta)
    
    print("Palavra: ", lista_letras_palavra_secreta)
    
    while(not enforcou and not acertou):
        chute = input("Qual letra ? ")
        chute = chute.strip().lower()
        index = 0
        #ele n é repetido
        if(chute not in letras_chutadas):
            #ele está dentro da palavra secreta
            if(chute in palavra_secreta):
                for letra in palavra_secreta:
                    if(letra == chute):
                        lista_letras_palavra_secreta[index] = chute
                        if(chute not in letras_chutadas):
                            letras_chutadas.append(chute)
                    index += 1
            else:
                if(chute not in letras_chutadas):
                    letras_chutadas.append(chute)
                    print(f'a letra {chute} não está na palavra secreta!')
                    erros += 1
                    desenha_forca(erros)
                    print("você errou! Faltam {} tentativas.".format(7-erros))
        else:
            print("Letra já Digitada!")

        print("Letras Digitadas: ", letras_chutadas)
        print(lista_letras_palavra_secreta)

        enforcou = (erros == 7)
        if("_" not in lista_letras_palavra_secreta and not enforcou):
            acertou = True
            break
        if(enforcou == True):
            break

    if(acertou):
        print("Parabéns, você acertou !!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
        input()
    else:
        os.system("cls")
        print(f'A Palavra era {palavra_secreta.upper()}')
        desenha_forca(erros)
        print(">>>>> GAME OVER <<<<<")
        input()
        
if(__name__ == "__main__"):
    menu()