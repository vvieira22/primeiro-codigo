#Declare a variable named company and assign it to an initial value "Coding For All".
from typing import ChainMap


company = "Coding For All"

#Print the variable company using print().
print(company)

#Print the length of the company string using len() method and print().
print(len(company))

#Change all the characters to uppercase letters using upper() method.
company_maiscula = company.upper()
#Change all the characters to lowercase letters using lower() method.
company_minuscula = company.lower()

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Cut(slice) out the first word of Coding For All string.
print(' '.join(company.split()[1:]))

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
#find
if(company.find("Coding")==-1):
    print("Não contém")
else:
    print("Contém!")

#index
try:
    company.index("Coding")
    print("Contém!")
except:
    print("Não Contém")

#split
print("Coding" in company.split()) #true or false

#Replace the word coding in the string 'Coding For All' to Python.
nova_company = company.replace("Coding For All","Python")

#Change Python for Everyone to Python for All using the replace method or other methods.
nova_company_2 = nova_company.replace("Python","Python for All")

#Split the string 'Coding For All' using space as the separator (split()) .
split_company = company.split(' ')
print(split_company)

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

redes_sociais = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(redes_sociais.split(','))

#What is the character at index 0 in the string Coding For All.
print(company[0])

#What is the last index of the string Coding For All.
print(company[-1])

#What character is at index 10 in "Coding For All" string.
print(company[10])

#Create an acronym or an abbreviation for the name 'Python For Everyone'.
py_for_evone = 'Python For Everyone'
#Create an acronym or an abbreviation for the name 'Coding For All'.
cod_for_all = 'Coding For All'

#Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))

#Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))

#Use rfind to determine the position of the last occurrence of l in Coding For All People.
print("Coding For All People".rfind('l'))

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
#'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.find('because'))

#Use rindex to find the position of the last occurrence of the word because in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.rindex("because"))

#Slice out the phrase 'because because because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'

print('You cannot end a sentence with because because because is a conjunction'.replace('because ',''))