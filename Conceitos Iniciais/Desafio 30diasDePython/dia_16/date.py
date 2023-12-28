#Python tem um modulo para lidar com horas
#Datetime

import datetime

#Obtendo informacoes data e hora
from datetime import datetime
now = datetime.now()
print(now)                      # 2021-07-08 07:34:46.549883
day = now.day                   # 8
month = now.month               # 7
year = now.year                 # 2021
hour = now.hour                 # 7
minute = now.minute             # 38
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38


#Formatando usando Strftime -> string
# https://strftime.org/
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S form
print(time_one)

#String -> Strftime
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)


#Diferença de tempo entre duas datas.
from datetime import date
t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff)

#Diferença de tempo entre duas datas -> timedelata
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)