"""
Conjuntos em python, sao uma coleção de elementos distintos
nao ordenados e nao indexados. Usado para armezar itens únicos
sendo possível encontrar, união, interseção, diferença, diferença simétrica,
subconjunto, superconjunto e conjunto disjunto entre conjuntos.
"""

#Criando um conjunto entre { }

#usamos a funcao interna set()
st = set()

#Conjunto com itens iniciais
st = {1,2,'1',1.8,'item'}


#comprimento do conjunto
print(len(st))


#Verificando um item dentro do conjunto
print(1.8 in st)


#Adicionando um item dentro do conjunto
st.add("Maionese")
print(st)
#Adicionando vários itens de uma vez no conjunto
st.update(["maicon","thiago"])
print(st)


#Removento itens de um conjunto
#Metodo remove()
#discard() remove mas nao gera erros se nao conseguir
st.remove(1.8)
print(st)

#Removento item aleatorio do conjunto
#retorna o item removido
print(st.pop())
print(st)

#Limpando itens em um conjunto
st = {'item1','item2','item3'}
st.clear()
print(st)

#Excluindo  o proprio conjunto
del st


#Convertendo lista em conjunto e vice versa.
# Podemos converter lista em conjunto e conjunto em lista. A conversão de lista em 
# conjunto remove duplicatas e apenas itens exclusivos serão reservados.

# syntax
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered


#Uniao de conjuntos
#Podemos unir dois conjuntos usando o método union() ou update()

#Union() retorna um novo conjunto
st1 = {'item1','item2','item3'}
st2 = {'item4','item5','item6'}
st3 = st1.union(st2)

#Update() Este metodo insere um conjunto em um determinado conjunto
st1 = {'item1','item2','item3'}
st2 = {'item4','item5','item6'}
st1.update(st2) #st2 vai ser adicionado em st1


#Intersecção de conjuntos
#Intersction() retorna um conjunto de itens que estao em ambos os conjuntos
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}

#Exemplo mais concreto
numeros_1 = {0,1,2,3,4,5,6}
numeros_2 = {0,5,3,2,1,20,35}
print(numeros_2.intersection(numeros_1)) #numeros no 2 que tem no 1.
print(numeros_1.intersection(numeros_2)) #numeros no 1 que tem no 2.


#Verificando Subconjunto e Superconjunto
#Um conjunto pode ser um subconjunto ou superconjunto de outros conjuntos:

#Subconjunto: issubset()
#Superconjunto: issuperset
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True  (st2 é SUBconjunto de st1 ?)
st1.issuperset(st2) # True (st1 é SUPERconjunto st2 ?)


#Diferença entre dois conjuntos
#Vai retornar a diferença entre dois conjuntos

conjunto_1 = {"Thiago", "Maria", "Jose", "Benedita"}
conjunto_2 = {"Thiago", "Maria", "Ivone", "Julia"}
diferenca_que_tem_no_1_mas_n_no_2 = conjunto_1.difference(conjunto_2)
diferenca_que_tem_no_2_mas_n_no_1 = conjunto_2.difference(conjunto_1)


"""
Encontrando diferença simétrica entre dois conjuntos

Ele retorna a difrença simétrica entre dois conjuntos. Significa que retorna um
conjunto que contém todos os itens de ambos os conjuntos, exceto os itens que
estão presentes em ambos os conjuntos 
(A\B) ∪ (B\A)
"""
conjunto_1 = {"Thiago", "Maria", "Jose", "Benedita"}
conjunto_2 = {"Thiago", "Maria", "Ivone", "Julia"}
tem_no1_tem_no2_mas_nao_em_ambos_ao_mesmo_tempo = conjunto_1.symmetric_difference(conjunto_2)
print(tem_no1_tem_no2_mas_nao_em_ambos_ao_mesmo_tempo)


#Unindo conjuntos
#Se dois conjunts nao possuem um ou mais itens comuns, chamamos de conjunto
#disjuntos. Podemos verificar se dois conjuntos são conjuntos ou disjuntos
#usando método isdisjoint()

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st3 = {'item9'}
st2.isdisjoint(st1) # False (ele tem elemento no st1 e no st2 igauis)
st3.isdisjoint(st2) # True (ele nao elemento do st3 no st2)
