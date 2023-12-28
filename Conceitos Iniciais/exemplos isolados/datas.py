from datetime import date
#essa forma vem no padrão ANSI
data_atual = date.today()
print(data_atual)

#Formato Brasileiro precisa ser transformado assim
data_em_texto = data_atual.strftime("%d/%m/%Y")
print(data_em_texto)

#Data com Horário Formatado
from datetime import datetime
data_e_hora_atuais = datetime.now() #vai pegar data e horario formato ANSI
data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M") #vai converter para formato Brasileiro
print(data_e_hora_em_texto)

#Convertendo uma string em datetime
data_e_hora_em_texto = '01/03/2018 12:30'
data_e_hora = datetime.strptime(data_e_hora_em_texto, "%d/%m/%Y %H:%M")

#O código anterior pode não funcionar para outros computadores, imprimindo valores diferentes
#Esse problema é chamado de problema do fuso horário (timezone)
#A comunidade Python, frente a essa necessidade, criou diversas bibliotecas para facilitar 
# a manipulação de timezones, como a pytz. Para instalar a pytz, você pode instalar pelo terminal.
from datetime import datetime
from pytz import timezone

data_e_hora_atuais = datetime.now()
fuso_horario = timezone("America/Sao_Paulo")
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')

print(data_e_hora_sao_paulo_em_texto)
