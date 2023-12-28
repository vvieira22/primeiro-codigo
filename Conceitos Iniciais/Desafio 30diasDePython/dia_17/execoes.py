#Python utiliza try e except para lidar com erros.
'''

try:
    code in this block if things go well
except:
    code in this block run if things go wrong

'''

# try:
#     name = input('Enter your name:')
#     year_born = input('Year you were born:')
#     age = 2019 - year_born
#     # print(f'You are {name}. And your age is {age}.')
# except TypeError:
#     print('Type error occured')
# except ValueError:
#     print('Value error occured')
# except ZeroDivisionError:
#     print('zero division error occured')

#Encurtar o codigo de cima para pegar qualquer erro
#Ira pegar toda exception que ocorrer.
# except Exception as e:
#     print(e)


#Empacotando e descompactando argumentos
# Usamos dois operadores:

# * para tuplas
# ** para dicionários

def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
# print(sum_of_five_nums(lst))
#Erro acontece, pq a funcao aceita numero e nao lista.

#Agora sim vai funcionar, pq empacotamos a lista
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e
lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15

#podemos utilizar tambem nafuncao integrada range por exemplo
lista = [1,2]
range(*lista)


#Descompactando Dicionário
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.


#Spreading in Python
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]

country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']


#Enumerar - Enumarated
#Se estivermos interessados apenas no indice de uma lista, podemos
#utilizar a funcao integrada enumarate para obter indide de cada item da lista

for index, item in enumerate(["vitor","thiago","jose"]):
    print(index,item)


#Zip.
#As vezes gostariamos de combinar listas para percorrelas, veja o exemplo
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)
