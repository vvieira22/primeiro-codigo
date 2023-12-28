# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Nível 1

#1
len(it_companies)

#2
it_companies.add("Twitter (x)")

#3
it_companies.update(['Whatsapp', 'Meta'])

#4
it_companies.remove("Twitter (x)")

#5
# discard() nao gera erros ao tentar remover elemento do conjunto


#Nível 2

#1
a_b = A.union(B)

#2
a_intersacao_b = A.intersection(B)

#3
print(A.issubset(B))

#4
print(A.isdisjoint(B))

#5
print(A.union(B))
print(B.union(A))

#6
print(A.symmetric_difference(B))

#7
del A
del B


#Nível 3

#1
age = list(age)
max(age)

#2
"""
String é tipo de dado escrita, como a que estou fazendo agora

Lista: Conjunto ordenado mutavel de dados com index.

Conjunto: Conjunto nao ordenado mutavel sem index de dados.
"""

#3
string = "I am a teacher and I love to inspire and teach people."
lista_palavras_unicas = string.split()
print(len(lista_palavras_unicas))