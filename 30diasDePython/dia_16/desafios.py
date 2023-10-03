#1
from datetime import *
now = datetime.now()
times = now.timestamp()
t = now.strftime("%d/%m/%Y %H:%M:%S")

#2
now.strftime("%m/%d/%Y %H:%M:%S")

#3
date_string = "5 December, 2019"
formatedDate = datetime.strptime(date_string, "%d %B, %Y")
print(formatedDate)

#4
data_atual = datetime.now()
future_date = datetime(year=2024,month=1,day=1)

#5
old_date = datetime(year=1970,month=1,day=1)
print(data_atual - old_date)

#6
''' 
Obter hora para registros de dados, para logs
com isso rastrear possiveis erros.
'''