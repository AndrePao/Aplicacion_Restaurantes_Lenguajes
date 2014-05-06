#se importa pyswip libreria que conecta prolog con python
from pyswip import *
#inicializacion del interprete de prolog
BaseConocimientos=Prolog()

#se carga el archivo que contiene la informacion de prolog
BaseConocimientos.consult("Base_de_conocimientos.pl")

"""%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
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
	
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"""


"""***********************************CONSULTA DE INFORMACION EN LA BC***********************************"""
#Metodo que busca los restaurantes en la lista de conocimientos  y retorna la lista de restaurantes
def L_restaurantes():
	parse_query_string(cherrypy.request.query_string)
	#Lista_Restaurantes=list(BaseConocimientos.query("listarestaurantes(Nombre)"))
	if (Lista_Restaurantes!=[]):
		print str(Lista_Restaurantes)#ver si puedo cambiar los _ por espacio, y colocar mayusculas
		return str(2)
	else:
		#print("No se encuentra el elemento") #ver si puedo cambiar los _ por espacio, y colocar mayusculas
		return 	"No se encuentra el elemento"

#Metodo que busca los restaurantes de acuerdo al tipo de comida de estos
def buscar_restaurante_por_tipo_de_comida(tipoDeComida):
	tipoDeComida=tipoDeComida.lower()
	tipoDeComida=cambiar_espacios(tipoDeComida) 
	listaDeacuerdoATipoComida = list(BaseConocimientos.query("restaurantes_tipo_comida(X," + tipoDeComida +")"))
	if (listaDeacuerdoATipoComida!=[]):
		#print (listaDeacuerdoATipoComida)
		return (listaDeacuerdoATipoComida) 
	else:
		#print ("No se encuentran resultados")
		return ("No se encuentran resultados") #envio lista vacia

#Metodo que busca la informacion del restaurantes 
def buscar_restaurante(NombreR):
	NombreR= NombreR.lower()
	NombreR=cambiar_espacios(NombreR)
	InforRestaurante = list(BaseConocimientos.query("buscar_restaurante("+NombreR+",TipoComida,Lugar,Tel,DiasAtencion, HorasAtencion2)"))
	if (InforRestaurante !=[]):
		#print (InforRestaurante )
		return (InforRestaurante ) 
	else:
		#print ("No se encuentran resultados")
		return ("No se encuentran resultados")  #envio lista vacia
###jwpejudpsjaasjocnonoasncnaocnaosnconcniewceeinocnownconcnwciinscokanscnoancoandocnondciownioen
#Al metodo se le ingresa un pais y retorna la lista de platillos de ese pais, no funciona NO FUNCIONA
def buscar_platillos_pais_origen(NombrePais):
	NombrePais= NombrePais.lower()
	NombrePais=cambiar_espacios(NombrePais)
	
	listaDePlatillos =list(BaseConocimientos.query("platillos(NombreR,NombreP,_,"+NombrePais+",_)"))
	print(listaDePlatillos)
	if (listaDePlatillos !=[]):
		print (listaDePlatillos)
		return (listaDePlatillos ) 
	else:
		print ("No se encuentran resultados")
		return ("No se encuentran resultados")  #envio lista vacia
		
#el metodo ingresa un restaurante y devuelve la lista de los platillos del restaurante
def buscar_platillos_restaurante(NombreR):
	NombreR= NombreR.lower()
	NombreR=cambiar_espacios(NombreR)
	listaPlatillosR = list(BaseConocimientos.query("platillos_restaurantes("+NombreR+",NombrePlatillo)"))
	if (listaPlatillosR !=[]):
		#print (listaPlatillosR)
		return (listaPlatillosR ) 
	else:
		#print ("No se encuentran resultados")
		return ("No se encuentran resultados")  #envio lista vacia

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& A PARTIR DE AQUI
def buscar_ingrdiente_platillo_restaurante(NombreR,Ingrediente):
	NombreR=NombreR.lower()
	NombreR= cambiar_espacios(NombreR)
	Ingrediente= Ingrediente.lower()
	Ingrediente=cambiar_espacios(Ingrediente)
	listaDeacuerdoAIngrediente = list(BaseConocimientos.query("ingrediente_platillos_restaurante("+NombreR+",NombrePlatillo,"+Ingrediente+")"))
	if (listaDeacuerdoAIngrediente !=[]):
		print (listaDeacuerdoAIngrediente)
		return (listaDeacuerdoAIngrediente ) 
	else:
		print ("No se encuentran resultados")
		return ("No se encuentran resultados")  #envio lista vacia
	
"""***********************************MANTENIMIENTO DE DATOS, INFORMACION QUE INGRESA EL USUARIO SOBRE RESTAURANTES Y PLATILLOS***********************************"""

#metodos que acomodan la informacion de acuerdo a la forma de almacenarla en prolog
#metodo que recorre la lista de elementos ingresada por el usuario y convierte el elemento a minuscula y los espacios los cambia por _
def convertirElementosMinuscula_QuitarEspacio(ListaIngredientes):
	ListaConvertida=[]
	minusculas=""
	c=""
	for elemento in ListaIngredientes:
		minusculas=elemento.lower()
		for letra in minusculas:
			
			if (letra==" "):
				c+="_"
			else:
				c+=letra
				
	return c
				
#funcion que cambia el espacio por un _, es para luego ingresar la informacion a prolog
def cambiar_espacios(palabra):
	nuevaP=""
	for letra in palabra:
		#if ((letra== " ") or (letra==":")):
		if (letra== " "): 
			nuevaP+="_"
		else: 
			nuevaP+=letra
	return nuevaP
####que pasa si el archivo no esta creado... colocar los hechos
"""El metodo agrega un nuevo restaurante a la base de conocimiento en prolog, el usuario ingresa el nombre del restaurante, el tipo 
de comida, el lugar, el numero de telefono y el horario de atencion"""
def IngresarINFORestaurante(NombreR,TipoComida,Lugar,Tel,DiaAtencion1,DiaAtencion2, HoraAtencion1,HoraAtencion2):
	#la funcion anterior (front-end)debe validar que en los espacios se haya introducido bien la informacion de numeros y letras
	#Primero se debe convertir a minusculas lo ingresado por el usuario
	NR=NombreR.lower()
	TC=TipoComida.lower()
	L=Lugar.lower()
	T=Tel.lower()
	DA1=DiaAtencion1.lower()
	DA2=DiaAtencion2.lower()
	
	#Concateno los dias de atencion y las horas de atencion
	DiasAtencion=DA1+"_"+DA2
	HorasAtencion= HoraAtencion1+":"+HoraAtencion2
	#si exiten espacios en la informacion ingresada por el usuario se cambian por _
	NR= cambiar_espacios(NR)
	TC=cambiar_espacios(TC)
	L=cambiar_espacios(L)
	T=cambiar_espacios(T)
	DiasAtencion=cambiar_espacios(DiasAtencion)
	HorasAtencion=cambiar_espacios(HorasAtencion)
	
	try: #escribe en el archivo de prolog , FALTA EL METODO QUE INGRESE LA INFORMACION EN ORDEN, SEGUN COMO ESTA EL ARCHIVO DE PROLOG
		ArchivoBC = open('Base_de_conocimientos.pl','a') #escribe en el archivo de prolog
		inforRestaurante= "restaurante("+NR+","+ TC +", "+ L + "," + T+ ","+ DiasAtencion+","+ HorasAtencion+").\n"
		ArchivoBC.write(inforRestaurante)
		ArchivoBC.close()
	
	except IOError: #Creacion del archivo si no esta creado,  meter las reglas
		ArchivoBC=open('Base_de_conocimientos.pl',"w")
		ArchivoBC.write(inforRestaurante)
		ArchivoBC.close()
	return ("Informacion almacenada exitosamente!!")

"""Ingresar informacion de platillo de  un restaurante, metodo recibe informacion de un platillo, nombre del restaurante, nombre de 
platillos, tipo de platillo (agridulce, dulce, salado), pais de oigen, lista de ingredientes del platillo []"""
def IngresarPlatillo(NombreR,NombrePlatillo,TipoPlatillo, PaisOrigen,ListaIngredientes):
	#convierte a minusculas los datos ingresados por el usuario
	NR=NombreR.lower()
	NP=NombrePlatillo.lower()
	TP=TipoPlatillo.lower()
	PO=PaisOrigen.lower()
	#convierte a minusculas la lista de elementos y cambia los espacios que existen en los elementos
	LI=convertirElementosMinuscula_QuitarEspacio(ListaIngredientes)
	#convierte los espacios en _
	NR= cambiar_espacios(NR)
	NP= cambiar_espacios(NP)
	TP= cambiar_espacios(TP)
	PO= cambiar_espacios(PO)
	
	try: #escribe en el archivo de prolog , (NO NECESARIO)ORDEN///FALTA EL METODO QUE INGRESE LA INFORMACION EN ORDEN, SEGUN COMO ESTA EL ARCHIVO DE PROLOG
		ArchivoBC = open('Base_de_conocimientos.pl','a') #escribe en el archivo de prolog
		inforPlatillo= "platillos("+NR+","+ NP +","+ TP + "," + PO+ ","+ LI+").\n"
		ArchivoBC.write(inforPlatillo)
		ArchivoBC.close()
	
	except IOError: #Creacion del archivo si no esta creado,  meter las reglas
		ArchivoBC=open('Base_de_conocimientos.pl',"w")
		ArchivoBC.write(inforPlatillo)
		ArchivoBC.close()
	return ("Informacion almacenada exitosamente!!"	)
"""validar si no encontro el archivo.pl en las consultas"""
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
#Imprimir()	 lo puedo borrar despues
#IngresarINFORestaurante("KFC","ChaTaRRa", "TERRAMALL","22334455","domingo","Viernes","4:00","6:45")
#IngresarPlatillo("CRUSTASEO CASCARUDO","CANGREburguer","SALADO", "Fondo de bikini","[pan,lechuga,tomate,pepinillos,carne]")
#Mostrar_restaurantes()
#buscar_restaurante_por_tipo_de_comida("chATARRA")
#L_restaurantes()
#buscar_restaurante("bk")
#buscar_platillos_pais_origen("fondo de bikini")
#buscar_platillos_restaurante("BK")
#buscar_ingrdiente_platillo_restaurante("kf","lechuga")

