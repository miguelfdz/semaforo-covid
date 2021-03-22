#https://datos.covid-19.conacyt.mx/Downloads/Files/Casos_Diarios_Estado_Nacional_Confirmados_20210317.csv
from datetime import timedelta, date, datetime
import requests
import os

def urlNueva():
	#Metodo que obtiene el nombre y url del archivo con los datos mas recientes
	urlCovid= "https://datos.covid-19.conacyt.mx/Downloads/Files/Casos_Diarios_Estado_Nacional_Confirmados_"
	diaActual = str(date.today())
	diaActual = diaActual.replace('-', '')
	return urlCovid+diaActual+".csv"

def urlDiaAnterior():
    urlCovid= "https://datos.covid-19.conacyt.mx/Downloads/Files/Casos_Diarios_Estado_Nacional_Confirmados_"
    diaAnterior = str(date.today() - timedelta(days=1))
    diaAnterior = diaAnterior.replace('-', '')
    return urlCovid+diaAnterior+".csv"

def is_downloadable(status_code):
	if status_code == 404:
		return False
	else:
		return True

def descargarArchivo():
	#Si el archivo es correcto se descarga
	url = urlNueva()
	r = requests.get(url, allow_redirects=True)
	status_code = r.status_code
	if status_code == 404:
		url = urlDiaAnterior()
		r = requests.get(url, allow_redirects=True)
		writeFile(r)
	else:
		#Descargar archivo en el directorio actual con el nombre de covid.csv
		writeFile(r)

def writeFile(request):
	if os.path.exists('covid.csv'):
		os.remove('covid.csv')
	else:
		print("El archivo no existe, se descargara el mas actual")
	open('covid.csv', 'wb').write(request.content)

#--------MAIN--------
descargarArchivo()