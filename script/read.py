import csv

with open('covid.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        row = dict(row)
        if row['nombre'] == "NUEVO LEON":
            for x in list(reversed(list(row)))[0:6]:
                print(x + " - " + row[x])