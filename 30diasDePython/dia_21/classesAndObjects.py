# Pyhon é uma linguagem orientada a objetos. Tudo em Python é um objeto, com suas propriedades e métodos.


# Criamos classe para criar um objeto. Uma classe é como um construtor de objetos ou um “modelo” para criar objetos. 
# Instanciamos uma classe para criar um objeto. A classe define os atributos e o comportamento do objeto,
# enquanto o objeto, por outro lado, representa a classe.


#Criando uma classe

# syntax
# class ClassName:
  #code here

# example
class Person:
    pass
print(Person) #<class '__main__.Person'>

# Criando um objeto
# syntax
p = Person()


#Construtor de uma classe 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)
print(p1.name) #John
print(p1.age) #36


#Métodos de objeto
# Os métodos são funções dentro de uma classe. 
# Eles são usados ​​para executar operações com os atributos de nossos objetos.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myFunc(self):
        print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myFunc() #Hello my name is John


#Métodos padrão de objeto
# Em python podemos querer valores padroes para metodos de objetos.
# Se fornecemos um valor padrão para um parâmetro, esse parâmetro pode ser omitido ao chamar o método.
class Person:
    def __init__(self, name, age = 18):
        self.name = name
        self.age = age
    def myFunc(self):
        print("Hello my name is " + self.name + " and I am " + str(self.age) + " years old")	
p1 = Person("John") #podemos ignorar a idade na declaracao ele vai pegar 18.
p1.myFunc() #Hello my name is John


#Método para modificar valores padrão de classe
# Podemos alterar os valores padrão de uma classe.
class Person:
    def __init__(self, name, age = 18):
        self.name = name
        self.age = age
    def aumentarIdade(self):
        self.age += 1

p1 = Person("John", 30)
print(p1.age) #30
p1.aumentarIdade()
print(p1.age) #31


#Herança
# A herança permite que uma classe herde os métodos e atributos de 
# outra classe.
# A classe pai é a classe de que herdamos, também chamada de superclasse.
# A classe filha é a classe que herda de outra classe, também chamada de 
# classe derivada.

class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.graduationyear = year
s1 = Student("Mike", 36, 2020)
print(s1.name) #Mike
print(s1.age) #36
s1.aumentarIdade()
print(s1.age) #37
print(s1.graduationyear) #2020
#Se ignoramos o método __init__() na classe filha, a classe filha herdará
# todos os atributos da classe pai. (Isso se a classe pai tiver atributos padroes e sem construtor.)


#Substituindo o método pai
# Podemos substituir o método pai na classe filha.
class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.graduationyear = year
    def aumentarIdade(self):
        self.age += 2

s1 = Student("Mike", 36, 2020)
print(s1.age) #36
s1.aumentarIdade() #aumenta 2 diferente de 1 da classe pai.
print(s1.age) #38