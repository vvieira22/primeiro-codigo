from re import L
from turtle import back


lista = [] #1

lista =  [1,2,3,4,5,6,7,9] #2

# print(len(lista)) #3

#4
lista[0] #primeiro elemento
lista[int(len(lista)/2)] #elemento do meio
lista[len(lista)-1] #ultimo elemento

#5
lista = ["vitor", 0.1, True, False, 1, 3]

#6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#7
print(it_companies)

#8
print(len(it_companies))

#9
print(it_companies[0]) #primeiro elemento
print(it_companies[int(len(it_companies)/2)]) #elemento do meio
print(it_companies[len(it_companies)-1]) #ultimo elemento

#10
it_companies[0] = "Slack"
print(it_companies)

#11
it_companies.append("Sony")

#12
index_meio_lista = int(len(it_companies)/2)
it_companies.insert(index_meio_lista, "Asus")
print(it_companies)

#13
for companys in it_companies:
    it_companies[it_companies.index(companys)] =  companys.upper()
print(it_companies)

#14
# it_companies = it_companies + "#;" #nao entendi

#15
print("EVGA" in it_companies)

#16
it_companies.sort()
print(it_companies)

#17
it_companies.reverse()
print(it_companies)

#18
print(it_companies[0:3])

#19
tamanho_lista = len(it_companies)
print(it_companies[-1:-4:-1])

#20
print(it_companies[int(len(it_companies)/2)])

#21
it_companies.pop(0)

#22
it_companies.pop(int(len(it_companies)/2))

#23
it_companies.pop()

#24
it_companies = []
print(it_companies)

#25
it_companies.clear()

#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

#27
full_stack = front_end + back_end
full_stack.insert(full_stack.index("Redux")+1,"Python")
full_stack.insert(full_stack.index("Python")+1,"SQL")
print(full_stack)