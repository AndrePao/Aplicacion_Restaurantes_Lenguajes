#se importa pyswip libreria que conecta prolog con python
from pyswip import *
#inicializacion del interprete de prolog
BaseConocimientos=Prolog()

#se carga el archivo que contiene la informacion de prolog
BaseConocimientos.consult("Base_de_conocimientos.pl")
#ArchivoBC=open("Base_de_conocimientos.pl","r") #lee el archivo de prolog
#ArchivoBC = open('Base_de_conocimientos.pl','a') #escribe en el archivo de prolog

#este es el metodo que sirve para imprimir en consola
def Imprimir():
	Lista_Restaurantes=Mostrar_restaurantes()
	#se almacena como un diccionario
	print( Lista_Restaurantes[0]["Nombre"])
	print( Lista_Restaurantes[0]["TipoAlimentacion"])
	print( Lista_Restaurantes[0]["Lugar"])
	print( Lista_Restaurantes[0]["Tel"])
	print( Lista_Restaurantes[0]["DiasAtencion"])
	print( Lista_Restaurantes[0]["HorasAtencion"])
	print("\n")
	
#metodo que imprime la lista de restaurantes de la base de conocimientos
def Mostrar_restaurantes():
	
	Lista_Restaurantes=list(BaseConocimientos.query("restaurante(Nombre, TipoAlimentacion, Lugar, Tel, DiasAtencion, HorasAtencion)"))
	
	return Lista_Restaurantes
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
def L_restaurantes():
	
	Lista_Restaurantes=list(BaseConocimientos.query("listarestaurantes(Nombre)"))
	
	print( Lista_Restaurantes)
	

#Metodo que busca los restaurantes de acuerdo al tipo de comida de estos
def buscar_restaurante_por_tipo_de_comida():
	tipoDeComida= "chatarra"
	listaDeacuerdoATipoComida = list(BaseConocimientos.query("restaurantes_tipo_comida(X," + tipoDeComida +")"))
	print (listaDeacuerdoATipoComida)

#Metodo que busca los restaurantes de acuerdo al tipo de comida de estos
def buscar_restaurante():
	NombreR= "mc_donalds"
	listaDeacuerdoATipoComida = list(BaseConocimientos.query("buscar_restaurante("+NombreR+",TipoComida,Lugar,Tel,DiasAtencion, HorasAtencion2)"))
	print (listaDeacuerdoATipoComida)
	
def buscar_platillos_pais_origen():
	NombrePais= "francia"
	listaDeacuerdoATipoComida = list(BaseConocimientos.query("platillos_pais(NombreR,"+NombrePais+")"))
	print (listaDeacuerdoATipoComida)

def buscar_platillos_restaurante():
	NombreR= "kfc"
	listaDeacuerdoATipoComida = list(BaseConocimientos.query("platillos_restaurantes("+NombreR+",NombrePlatillo)"))
	print (listaDeacuerdoATipoComida)

def buscar_ingrdiente_platillo_restaurante():
	NombreR="kfc"
	Ingrediente= "queso"
	listaDeacuerdoATipoComida = list(BaseConocimientos.query("ingrediente_platillos_restaurante("+NombreR+",NombrePlatillo,"+Ingrediente+")"))
	print (listaDeacuerdoATipoComida)

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

"""El metodo agrega un nuevo restaurante a la base de conocimiento en prolog, el usuario ingresa el nombre del restaurante, el tipo 
de comida, el lugar, el numero de telefono y el horario de atencion"""
def IngresarINFORestaurante(NombreR,TipoComida,Lugar,Tel,DiaAtencion1,DiaAtencion2, HoraAtencion1,HoraAtencion2):
	#la funcion anterior debe validar que en los espacios se haya introducido bien la informacion de numeros y letras
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

#Ingresar platillos de  un restaurante
#def IngresarPlatillo(NombreR,NombrePlatillo,tipoPlatillo, PaisOrigen)


#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
#Imprimir()	
#IngresarINFORestaurante("KFC","ChaTaRRa", "TERRAMALL","22334455","domingo","Viernes","4:00","6:45")
#Mostrar_restaurantes()
#buscar_restaurante_por_tipo_de_comida()
#L_restaurantes()
#buscar_restaurante()
#buscar_platillos_pais_origen()
#buscar_platillos_restaurante()
buscar_ingrdiente_platillo_restaurante()
"""


restaurante(casaluna,costarricense,teccartago,66666666,lunes_sabado_7_5).
restaurante(banquetes,hawaiana, sandiego,22334455,sabadolunes,45).
restaurante(pizza,saprisema, puntarenas,22567855,sabadolunes,0987)."""
