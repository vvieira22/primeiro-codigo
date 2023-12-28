import requests
import re
import os

def main():
    print("----------------CONSULTA DE CEP----------------")

    cep_consulta = input("Digite o cep (sem -) para consulta: ")

    if len(cep_consulta)!=8:
        print("Cep em formato inválido!")
    else:
        request = requests.get(f'https://viacep.com.br/ws/{cep_consulta}/json/')

        adress_data = request.json()
        if 'erro' not in adress_data:
            print("CEP encontrado")
            print(f"Logradouro: {adress_data['logradouro']}")
            print(f"Bairro: {adress_data['bairro']}")
            print(f"localidade: {adress_data['localidade']}")
            print(f"UF: {adress_data['uf']}")
            print(f"DDD: {adress_data['ddd']}")
        else:
            print("Cep inválido")
    
    opcao = int(input("Deseja realizar uma nova consulta? 1- sim 2-nao: "))

    if(opcao == 1):
        os.system('cls')
        main()
    else:
        exit()

if __name__ == '__main__':
    main()