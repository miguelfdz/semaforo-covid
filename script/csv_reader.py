import csv
import os
from gpiozero import LED
from time import sleep

#Pines de cada LED
yellow = LED(26)
green = LED(5)
red = LED(10)
orange = LED(11)
#--------
summatory = 0
avg = 0.0
daily_cases = 0.0
status = ""
nl_population = 5784000

os.system('python3 download_covid_cases.py')

with open('covid.csv', mode='r') as csv_file:
  csv_reader = csv.DictReader(csv_file)
  for row in csv_reader:
    row = dict(row)
    if row['nombre'] == "NUEVO LEON":
      for x in list(reversed(list(row)))[0:7]:
        summatory += int(row[x])
      avg = summatory/7
      daily_cases = (avg/nl_population)*100000

def get_nl_status(daily_cases):
  print("Desplegando semaforo epidemiologico de Nuevo Leon:")
  if daily_cases < 0.5:
    green.on()
    print("Semaforo: Verde\nPodemos salir pero con precaución y prevención.")
    sleep(30)
    green.off()
  elif daily_cases >= 0.5 and daily_cases <= 2.5:
    yellow.on()
    print("Semaforo: Amarillo\nHay más actividades pero con precaución.")
    sleep(30)
    yellow.off()
  elif daily_cases >= 2.6 and daily_cases <= 5.0:
    orange.on()
    print("Semaforo: Naranja\nSi puedes, quédate en casa.")
    sleep(30)
    orange.off()
  elif daily_cases > 5.1:
    red.on()
    print("Semaforo: Rojo\nNo salgas si no es estrictamente necesario.")
    sleep(30)
    red.off()
  else:
    return 'error'
  print("Ejecucion finalizada, apagando el semaforo...")

get_nl_status(daily_cases)