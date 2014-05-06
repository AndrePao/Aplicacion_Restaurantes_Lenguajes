from flask import Flask, render_template, request, redirect, url_for, abort, session
#import consultas_y_mantenimiento_datos
#se importa pyswip libreria que conecta prolog con python
from pyswip import *
#inicializacion del interprete de prolog
BaseConocimientos=Prolog()

#se carga el archivo que contiene la informacion de prolog
BaseConocimientos.consult("Base_de_conocimientos.pl")


####que pasa si el archivo no esta creado... colocar los hechos
"""El metodo agrega un nuevo restaurante a la base de conocimiento en prolog, el usuario ingresa el nombre del restaurante, el tipo 
de comida, el lugar, el numero de telefono y el horario de atencion"""
def IngresarINFORestaurante(NombreR,TipoComida,Lugar,Tel,DiasAtencion):
	#la funcion anterior (front-end)debe validar que en los espacios se haya introducido bien la informacion de numeros y letras
	#Primero se debe convertir a minusculas lo ingresado por el usuario
	"""NR=NombreR.lower()
	TC=TipoComida.lower()
	L=Lugar.lower()
	T=Tel.lower()
	DA1=DiaAtencion1.lower()
	DA2=DiaAtencion2.lower()"""
	
	#Concateno los dias de atencion y las horas de atencion
	#DiasAtencion=DA1+"_"+DA2
	#HorasAtencion= HoraAtencion1+":"+HoraAtencion2
	#si exiten espacios en la informacion ingresada por el usuario se cambian por _
	'''NR= cambiar_espacios(NR)
	TC=cambiar_espacios(TC)
	L=cambiar_espacios(L)
	T=cambiar_espacios(T)
	DiasAtencion=cambiar_espacios(DiasAtencion)
	HorasAtencion=cambiar_espacios(HorasAtencion)'''
	
	try: #escribe en el archivo de prolog , FALTA EL METODO QUE INGRESE LA INFORMACION EN ORDEN, SEGUN COMO ESTA EL ARCHIVO DE PROLOG
		ArchivoBC = open('Base_de_conocimientos.pl','a') #escribe en el archivo de prolog
		inforRestaurante= "restaurante("+NombreR+","+ TipoComida +", "+ Lugar + "," + Tel+ ","+ DiasAtencion+","+ DiasAtencion+").\n"
		ArchivoBC.write(inforRestaurante)
		ArchivoBC.close()
	
	except IOError: #Creacion del archivo si no esta creado,  meter las reglas
		ArchivoBC=open('Base_de_conocimientos.pl',"w")
		ArchivoBC.write(inforRestaurante)
		ArchivoBC.close()
	return "Informacion almacenada exitosamente!!"

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
	return "Informacion almacenada exitosamente!!"

#Metodo que busca los restaurantes en la lista de conocimientos  y retorna la lista de restaurantes
def L_restaurantes():
	
	Lista_Restaurantes=list(BaseConocimientos.query("listarestaurantes(Nombre)"))
	if (Lista_Restaurantes!=[]):
		#print str(Lista_Restaurantes)#ver si puedo cambiar los _ por espacio, y colocar mayusculas
		return Lista_Restaurantes
	else:
		#print("No se encuentra el elemento") #ver si puedo cambiar los _ por espacio, y colocar mayusculas
		return 	"No se encuentra el elemento"
#Metodo que busca los restaurantes de acuerdo al tipo de comida de estos
def buscar_restaurante_por_tipo_de_comida(tipoDeComida):
	#tipoDeComida=tipoDeComida.lower()
	#tipoDeComida=cambiar_espacios(tipoDeComida) 
	listaDeacuerdoATipoComida = list(BaseConocimientos.query("restaurantes_tipo_comida(X," + tipoDeComida +")"))
	if (listaDeacuerdoATipoComida!=[]):
		
		return listaDeacuerdoATipoComida
	else:
		
		return ("No se encuentran resultados") #envio lista vacia

#Metodo que busca la informacion del restaurantes 
def buscar_restaurante(NombreR):
	#NombreR= NombreR.lower()
	#NombreR=cambiar_espacios(NombreR)
	InforRestaurante = list(BaseConocimientos.query("buscar_restaurante("+NombreR+",TipoComida,Lugar,Tel,DiasAtencion, HorasAtencion2)"))
	if (InforRestaurante !=[]):
		
		return InforRestaurante 
	else:
		
		return ["No se encuentran resultados"] #envio lista vacia

#Al metodo se le ingresa un pais y retorna la lista de platillos de ese pais,
"""lista"""
def buscar_platillos_pais_origen(NombrePais):
	#NombrePais= NombrePais.lower()
	#NombrePais=cambiar_espacios(NombrePais)
	listaDePlatillos =list(BaseConocimientos.query("platillos(NombreR,NombreP,_,"+NombrePais+",_)"))
	if (listaDePlatillos !=[]):
		
		return listaDePlatillos 
	else:
		return ["No se encuentran resultados"] #envio lista vacia

#el metodo ingresa un restaurante y devuelve la lista de los platillos del restaurante
def buscar_platillos_restaurante(NombreR):
	#NombreR= NombreR.lower()
	#NombreR=cambiar_espacios(NombreR)
	listaPlatillosR = list(BaseConocimientos.query("platillos_restaurantes("+NombreR+",NombrePlatillo)"))
	if (listaPlatillosR !=[]):
		return listaPlatillosR 
	else:
		return ["No se encuentran resultados"]  #envio lista vacia

def buscar_ingrediente_platillo_restaurante(NombreR,Ingrediente):
	#NombreR=NombreR.lower()
	#NombreR= cambiar_espacios(NombreR)
	#Ingrediente= Ingrediente.lower()
	#Ingrediente=cambiar_espacios(Ingrediente)
	listaDeacuerdoAIngrediente = list(BaseConocimientos.query("ingrediente_platillos_restaurante("+NombreR+",NombrePlatillo,"+Ingrediente+")"))
	if (listaDeacuerdoAIngrediente !=[]):
		return listaDeacuerdoAIngrediente  
	else:
		return ["No se encuentran resultados"]  #envio lista vacia

app = Flask(__name__)
app.config['SECRET_KEY'] = 'F34TF$($e34D';


@app.route('/')
def home():
    return render_template('principal.html')

@app.route('/AgregaPlatillo')
def AgregaPlatillo():
    return render_template('plaagre.html')

@app.route('/AgregaPlatillo2', methods=['POST'])
def AgregaPlatillo2():
    NombreR=request.form['Restaurante']
    NombreP=request.form['Platillo']
    TipC=request.form['TipoComida']
    PaisO=request.form['PaisOrigen']
    Ingre1=request.form['Ingre1']
    Ingre2=request.form['Ingre2']
    Ingre3=request.form['Ingre3']
    Ingre4=request.form['Ingre4']
    Ingre5=request.form['Ingre5']
    ListaIngre=[Ingre1,Ingre2,Ingre3,Ingre4,Ingre5]
    mensaje=IngresarPlatillo(NombreR,NombreP,TipC, PaisO,ListaIngre)
    return render_template('plaagre.html')

@app.route('/AgregaRestaurante')
def AgregaRestaurante():
    return render_template('restagre.html')

@app.route('/AgregaRestaurante2', methods=['POST'])
def AgregaRestaurante2():
    NombreR=request.form['Restaurante']
    TipoCom=request.form['TipoComida']
    Ubic=request.form['Ubicacion']
    Tel=request.form['Telefono']
    Inic=request.form['Inicio']
    Fin=request.form['Final']
    Horario=Inic+"_"+Fin
    mensaje=IngresarINFORestaurante(NombreR,TipoCom,Ubic,Tel,Horario)
    return render_template('restagre.html', mensaje=mensaje)

@app.route('/PlatilloxRestaurante')
def PlatilloxRestaurante():
    return render_template('restpla.html')

@app.route('/PlatilloxRestaurante2', methods=['POST'])
def PlatilloxRestaurante2():
    PlatilloN= request.form['Platillo']
    lista=buscar_platillos_restaurante(PlatilloN)
    return render_template('restpla2.html', lista=lista, Nombre=PlatilloN)

@app.route('/PlatilloxIngrediente')
def PlatilloxIngrediente():
    return render_template('plaing.html')

@app.route('/PlatilloxIngrediente2', methods=['POST'])
def PlatilloxIngrediente2():
    NombreR= request.form['Restaurante']
    IngredienteR= request.form['Ingrediente']
    lista=buscar_ingrediente_platillo_restaurante(NombreR,IngredienteR)
    return render_template('plaing2.html', lista=lista, Nombre=NombreR, Ing=IngredienteR)

@app.route('/ResPaisOrigen')
def ResPaisOrigen():
    return render_template('restpais.html')

@app.route('/ResPaisOrigen2', methods=['POST'])
def ResPaisOrigen2():
    PaisO= request.form['Pais']
    lista= buscar_platillos_pais_origen(PaisO)
    return render_template('restpais2.html', lista=lista, Nombre=PaisO)

@app.route('/RestauranteEspecifico')
def RestauranteEspecifico():
    return render_template('restesp.html')

@app.route('/RestauranteEspecifico2', methods=['POST'])
def RestauranteEspecifico2():
    NombreR= request.form['Nombre']
    lista= buscar_restaurante(NombreR)
    return render_template('restesp2.html', lista=lista, Nombre=NombreR)


@app.route('/Platillo')
def Platillo():
    return render_template('platillo.html')

@app.route('/Platillo2', methods=['POST'])
def Platillo2():
    TipoComida= request.form['Tipo']
    lista= buscar_restaurante_por_tipo_de_comida(TipoComida)
    return render_template('platillo2.html', lista=lista)# lista=[1,2,1])#render_template('index.html')#mensaje#render_template('index.html')

@app.route('/Principal')
def Principal():
    mensaje=L_restaurantes()#IngresarPlatillo("coffi","helado","dulce", "italia","azucar")
    return render_template('home.html', lista=mensaje)
if __name__ == '__main__':
    app.run()
