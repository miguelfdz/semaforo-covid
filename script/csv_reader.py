import csv
summatory = 0
avg = 0.0
daily_cases = 0.0
status = ""
nl_population = 5784000

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
    return 'Verde'
  elif daily_cases >= 0.5 and daily_cases <= 2.5:
    return 'Amarillo'
  elif daily_cases >= 2.6 and daily_cases <= 5.0:
    return 'Naranja'
  elif daily_cases > 5.1:
    return 'Rojo'
  else:
    return 'error'

status = get_nl_status(daily_cases)
print(status)