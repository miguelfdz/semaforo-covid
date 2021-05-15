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
  if daily_cases < 0.5:
    green.on()
    sleep(10)
    green.off()
  elif daily_cases >= 0.5 and daily_cases <= 2.5:
    yellow.on()
    sleep(10)
    yellow.off()
  elif daily_cases >= 2.6 and daily_cases <= 5.0:
    orange.on()
    sleep(10)
    orange.off()
  elif daily_cases > 5.1:
    red.on()
    sleep(10)
    red.off()
  else:
    return 'error'

status = get_nl_status(daily_cases)