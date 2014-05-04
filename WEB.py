from jinja2 import Environment, meta
from flask import Flask, render_template, request, redirect, url_for, abort, session
#import consultas_y_mantenimiento_datos
#se importa pyswip libreria que conecta prolog con python
from pyswip import *
#inicializacion del interprete de prolog
BaseConocimientos=Prolog()

#se carga el archivo que contiene la informacion de prolog
BaseConocimientos.consult("Base_de_conocimientos.pl")
#este es el metodo que sirve para imprimir en consola
def Imprimir(): lo puedo borrar despues
	Lista_Restaurantes=Mostrar_restaurantes()
	#se almacena como un diccionario
	print( Lista_Restaurantes[0]["Nombre"])
	print( Lista_Restaurantes[0]["TipoAlimentacion"])
	print( Lista_Restaurantes[0]["Lugar"])
	print( Lista_Restaurantes[0]["Tel"])
	print( Lista_Restaurantes[0]["DiasAtencion"])
	print( Lista_Restaurantes[0]["HorasAtencion"])
	print("\n")
	'''for e in InforRestaurante[0]["PlatilloF"]:
			print (e)'''

"""Ingresar informacion de platillo de  un restaurante, metodo recibe informacion de un platillo, nombre del restaurante, nombre de 
platillos, tipo de platillo (agridulce, dulce, salado), pais de oigen, lista de ingredientes del platillo []"""
def IngresarPlatillo(NombreR,NombrePlatillo,TipoPlatillo, PaisOrigen,ListaIngredientes):
	#convierte a minusculas los datos ingresados por el usuario
	'''NR=NombreR.lower()
	NP=NombrePlatillo.lower()
	TP=TipoPlatillo.lower()
	PO=PaisOrigen.lower()'''
	#convierte a minusculas la lista de elementos y cambia los espacios que existen en los elementos
	'''LI=convertirElementosMinuscula_QuitarEspacio(ListaIngredientes)
	#convierte los espacios en _
	NR= cambiar_espacios(NR)
	NP= cambiar_espacios(NP)
	TP= cambiar_espacios(TP)
	PO= cambiar_espacios(PO)'''
	
	try: #escribe en el archivo de prolog , (NO NECESARIO)ORDEN///FALTA EL METODO QUE INGRESE LA INFORMACION EN ORDEN, SEGUN COMO ESTA EL ARCHIVO DE PROLOG
		ArchivoBC = open('Base_de_conocimientos.pl','a') #escribe en el archivo de prolog
		inforPlatillo= "platillos("+NombreR+","+ NombrePlatillo +","+ TipoPlatillo + "," + PaisOrigen+ ","+ ListaIngredientes+").\n"
		ArchivoBC.write(inforPlatillo)
		ArchivoBC.close()
	
	except IOError: #Creacion del archivo si no esta creado,  meter las reglas
		ArchivoBC=open('Base_de_conocimientos.pl',"w")
		ArchivoBC.write(inforPlatillo)
		ArchivoBC.close()
	return ("Informacion almacenada exitosamente!!"	)

#Metodo que busca los restaurantes en la lista de conocimientos  y retorna la lista de restaurantes
def L_restaurantes():
	
	Lista_Restaurantes=list(BaseConocimientos.query("listarestaurantes(Nombre)"))
	if (Lista_Restaurantes!=[]):
		#print str(Lista_Restaurantes)#ver si puedo cambiar los _ por espacio, y colocar mayusculas
		return str(Lista_Restaurantes)
	else:
		#print("No se encuentra el elemento") #ver si puedo cambiar los _ por espacio, y colocar mayusculas
		return 	"No se encuentra el elemento"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'F34TF$($e34D';

@app.route('/')
def home():
    return render_template('indexx.html')
    '''mensaje=IngresarPlatillo("coffi","helado","dulce", "italia","azucar")
    return mensaje#render_template('index.html')'''

if __name__ == '__main__':
    app.run()
