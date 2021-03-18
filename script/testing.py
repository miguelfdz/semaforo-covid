#https://datos.covid-19.conacyt.mx/Downloads/Files/Casos_Diarios_Estado_Nacional_Confirmados_20210317.csv
import datetime
import requests

def urlNueva():
	#Metodo que obtiene el nombre y url del archivo con los datos mas recientes
	urlCovid= "https://datos.covid-19.conacyt.mx/Downloads/Files/Casos_Diarios_Estado_Nacional_Confirmados_"
	dt = datetime.date.today()
	fecha = str(dt)
	fecha = fecha.replace('-', '')
	return urlCovid+fecha+".csv"

def is_downloadable(url):
	#Metodo para revisar que tipo de archivo se va a descargar (Validacion)
	h = requests.head(url, allow_redirects=True)
	header = h.headers
	content_type = header.get('content-type')
	#Solo descargar si el archivo es CSV
	if 'text/csv' in content_type.lower():
		return True
	return False

def descargarArchivo():
	#Si el archivo es correcto se descarga
	url = urlNueva()
	if is_downloadable(url):
		r = requests.get(url, allow_redirects=True)
		#Descargar archivo en el directorio actual con el nombre de covid.csv
		open('covid.csv', 'wb').write(r.content)

#--------MAIN--------
descargarArchivo()