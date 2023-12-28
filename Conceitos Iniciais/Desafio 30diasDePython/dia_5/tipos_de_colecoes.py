'''Existem quatro tipos de dados de coleção em Python:

>Lista: é uma coleção que é ordenada e mutável (modificável). Permite membros duplicados.
>Tupla: é uma coleção que é ordenada e imutável ou não modificável (imutável). Permite membros duplicados.
>Conjunto: é uma coleção não ordenada, não indexada e não modificável, mas podemos adicionar novos itens ao conjunto. Membros duplicados não são permitidos.
>Dicionário: é uma coleção não ordenada, mutável (modificável) e indexada. Nenhum membro duplicado.'''

'''LISTA
Para criar listas temos duas formas:'''

lista_forma_1 = list() #build-in
lista_forma_2 = []  #entre chaves

'''Exemplo de criação'''
frutas = ['banana', 'pera', "uva", 'limão'] # list of frutas

'''Inserção e modificação'''
frutas.append('maça') #Insere elemento novo na ultima posição
frutas[3] = "melancia" #modifiquei o "valor" uva para melancia
frutas.insert(2, "melao") #insere o valor nessa posição, deslocando os anteriores para direita.

'''Acessar elementos individualmente, sempre na ordem 0,1,2,3...
posicoes negativas sao inversos aos positivos        -4,-3,-2,-1'''
print(frutas[0]) #banana
print(frutas[len(frutas)-1]) #ultimo elemento da lista

'''Fatiamento de itens na lista, resultados de um fatiamento
será uma outra lista contendo os valores entre o intervalo definido
(start = 0, end = len(frutas) }- 1 (last item), step = 1)'''
print(frutas[0:]) #primeiro elemento até o último
print(frutas[0:2]) # banana e pera
print(frutas[::-1]) #vai retornar a lista de trás pra frente, começando do ultimo ao primeiro

'''Verificando se item está na lista'''
print('pera' in frutas) #verdade, 'pera' esta em frutas

'''Remoção de item numa lista e limpeza'''
frutas.remove("melancia")
frutas.pop(3) #remove o item baseado no index, caso nao seja passado remove o últim
del frutas[0:1] #remove intervalo  de valores forrnecidos
#frutas.clear() #limpa totalmente a lista, zera ela
print(frutas)

'''Copiando uma lista
Muitas vezes precisamos copiar uma lista, mas dizer lista1=lista2, pode causar problemas
lista 2 pode ser modificado e interferindo na lista 1, por isso deve utilizar  o comando copy'''
frutas2 = frutas.copy()

'''Existem diversas formas de você adicionar, 
entrar e concatenar listas em python'''

lista_1 = [7,2,3,8,5]
lista_2 = [0]
lista_3 = [1,7,8,9,2]

'''Incrementar com operador soma'''
lista_somada = lista_1+lista_2+lista_3 
#resultado = [7,2,3,8,5,0,1,7,8,9,2]

'''Usando extend para dar append numa lista na outra, modifica a original'''
# lista_append = lista_1.append(lista_2)
#resultado = [7,2,3,8,5,0]

'''Contando elementos numa Lista'''
contagem = lista_1.count(1) #=1, existem 1 número 1 na lista

'''Achando index de um elemento na lista'''
print(lista_1.index(8)) #=3

'''Invertendo uma Lista'''
lista_1_invertida = lista_1.reverse() #[5,8,3,2,7]

'''Ordenar uma lista'''
lista_ordenada_crescente = sorted(lista_1)
lista_ordenada_decrescente = sorted(lista_1,reverse=True)