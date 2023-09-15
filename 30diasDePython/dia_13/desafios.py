#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
lista = [i for i in numbers if i<=0]

#2 Exercicio confuso, deu bastante trabalho
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
lista = [item for items in list_of_lists for item in items[0]]

#3
""" 0-10
7 elementos, multiplicando
primeiro *1,2,3,4,5,6
 """
lista = [[i, 1, i, i**2, i**3, i**4, i**5] for i in range(11)]


#4 dificil entender o que foi feito aqui
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
lista = [item for subitem in countries for item in subitem]
lista = [list(item) for subitem in lista for item in [subitem]] #("lista" aqui seria fora do [], por isso botamos ele)
""" 
O do meio vai pegar elemento da lista, entao fica = ["a"],["b"],("b")
na sequencia o ultimo for vai cada pegar elemento dessa lista
e o item vai ser uma lista com cada elemento sendo a iteracao do ultimo for. """


#5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_limpa = ([list(cidade) for subitem in countries for cidade in subitem])
dicionario = [{"country":item[0],"city":item[1]} for item in countries_limpa]
print(dicionario)


#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
names = [item for subitem in names for item in subitem]
names = [item for subitem in names for item in subitem]

#7
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
y_intercept = lambda x1, y1, x2, y2: y1 - slope(x1, y1, x2, y2) * x1