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
"""lista"""
def L_restaurantes():
	Lista_Restaurantes=list(BaseConocimientos.query("restaurante(Nombre,_,_,_,_,_,_)"))
	if (Lista_Restaurantes!=[]):
		print( Lista_Restaurantes) #ver si puedo cambiar los _ por espacio, y colocar mayusculas
		return (Lista_Restaurantes)
	else:
		print("No se encuentra el elemento") #ver si puedo cambiar los _ por espacio, y colocar mayusculas
		return ("No se encuentran resultados")
	

#Metodo que busca los restaurantes de acuerdo al tipo de comida de estos
"""lista"""
def buscar_restaurante_por_tipo_de_comida(tipoDeComida):
	tipoDeComida=tipoDeComida.lower()
	tipoDeComida=cambiar_espacios(tipoDeComida) 
	listaDeacuerdoATipoComida = list(BaseConocimientos.query("restaurante(NombreR,"+tipoDeComida+",_,_,_,_,_)"))
	if (listaDeacuerdoATipoComida!=[]):
		print (listaDeacuerdoATipoComida)
		return (listaDeacuerdoATipoComida) 
	else:
		print ("No se encuentran resultados")
		return ("No se encuentran resultados") #envio lista vacia

#Metodo que busca la informacion del restaurantes , arreglar la hora y la comida favorita
"""lista"""
def buscar_restaurante(NombreR):
	NombreR= NombreR.lower()
	NombreR=cambiar_espacios(NombreR)
	InforRestaurante = list(BaseConocimientos.query("restaurante("+NombreR+",TipoComida,Lugar,Tel,DiasAtencion, HorasAtencion2,PlatilloF)"))
	if (InforRestaurante !=[]):
		print (InforRestaurante[0]["TipoComida"] )
		print (InforRestaurante[0]["Lugar"] )
		print (InforRestaurante[0]["Tel"] )
		print (InforRestaurante[0]["DiasAtencion"] )
		print (InforRestaurante[0]["HorasAtencion2"] )
		for e in InforRestaurante[0]["PlatilloF"]:
			print (e)
		return (InforRestaurante ) 
	else:
		print ("No se encuentran resultados")
		return ("No se encuentran resultados")  #envio lista vacia
		

#Al metodo se le ingresa un pais y retorna la lista de platillos de ese pais,
"""lista"""
def buscar_platillos_pais_origen(NombrePais):
	NombrePais= NombrePais.lower()
	NombrePais=cambiar_espacios(NombrePais)
	listaDePlatillos =list(BaseConocimientos.query("platillos(NombreR,NombreP,_,"+NombrePais+",_)"))
	if (listaDePlatillos !=[]):
		print (listaDePlatillos)
		return (listaDePlatillos ) 
	else:
		print ("No se encuentran resultados")
		return ("No se encuentran resultados")  #envio lista vacia
		
#el metodo ingresa un restaurante y devuelve la lista de los platillos del restaurante
"""lista"""
def buscar_platillos_restaurante(NombreR):
	NombreR= NombreR.lower()
	NombreR=cambiar_espacios(NombreR)
	listaPlatillosR = list(BaseConocimientos.query("platillos("+NombreR+",NombrePlatillo,_,_,_)"))
	if (listaPlatillosR !=[]):
		print (listaPlatillosR)
		return (listaPlatillosR ) 
	else:
		print ("No se encuentran resultados")
		return ("No se encuentran resultados")  #envio lista vacia

#Al metodo le ingresa el nombre del restaurante y un ingrediente, el metodo retorna la lista de platillos de ese restaurante que tienen ese ingrediente.
def buscar_ingrediente_platillo_restaurante(NombreR,Ingrediente):
	NombreR=NombreR.lower()
	NombreR= cambiar_espacios(NombreR)
	Ingrediente= Ingrediente.lower()
	Ingrediente=cambiar_espacios(Ingrediente)
	listaDeacuerdoAIngrediente = list(BaseConocimientos.query("platillos("+NombreR+",NombrePlatillo,_,_,[IngredienteL|ListaI]), member("+Ingrediente+",[IngredienteL|ListaI])"))
	if (listaDeacuerdoAIngrediente !=[]):
		print (listaDeacuerdoAIngrediente[0]["NombrePlatillo"])
		print (listaDeacuerdoAIngrediente[1]["NombrePlatillo"])

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
		if (letra== " "): 
			nuevaP+="_"
		else: 
			nuevaP+=letra
	return nuevaP
####que pasa si el archivo no esta creado... crearlo ingresar lista de platillos favoritos
"""El metodo agrega un nuevo restaurante a la base de conocimiento en prolog, el usuario ingresa el nombre del restaurante, el tipo 
de comida, el lugar, el numero de telefono y el horario de atencion"""
def IngresarINFORestaurante(NombreR,TipoComida,Lugar,Tel,DiaAtencion1,DiaAtencion2, HoraAtencion1,HoraAtencion2, LPlatilloF):
	#la funcion anterior (front-end)debe validar que en los espacios se haya introducido bien la informacion de numeros y letras
	#Primero se debe convertir a minusculas lo ingresado por el usuario
	NR=NombreR.lower()
	TC=TipoComida.lower()
	L=Lugar.lower()
	T=Tel.lower()
	DA1=DiaAtencion1.lower()
	DA2=DiaAtencion2.lower()
	L_PlatillosFavoritos=convertirElementosMinuscula_QuitarEspacio(LPlatilloF)

	#Concateno los dias de atencion y las horas de atencion
	DiasAtencion=DA1+"_"+DA2
	HorasAtencion= HoraAtencion1+""+HoraAtencion2
	#si exiten espacios en la informacion ingresada por el usuario se cambian por _
	NR= cambiar_espacios(NR)
	TC=cambiar_espacios(TC)
	L=cambiar_espacios(L)
	T=cambiar_espacios(T)
	DiasAtencion=cambiar_espacios(DiasAtencion)
	HorasAtencion=cambiar_espacios(HorasAtencion)
	
	try: #escribe en el archivo de prolog , FALTA EL METODO QUE INGRESE LA INFORMACION EN ORDEN, SEGUN COMO ESTA EL ARCHIVO DE PROLOG
		ArchivoBC = open('Base_de_conocimientos.pl','a') #escribe en el archivo de prolog
		inforRestaurante= "restaurante("+NR+","+ TC +", "+ L + "," + T+ ","+ DiasAtencion+","+ HorasAtencion+","+ L_PlatillosFavoritos +").\n"
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
#IngresarINFORestaurante("pan e vino","italiana", "TERRAMALL","89497239","domingo","Viernes","0400","0645","[PIZZA,lasagna,chiverre]")
#IngresarPlatillo("CRUSTASEO CASCARUDO","CANGREburguer","SALADO", "Fondo de bikini","[pan,lechuga,tomate,pepinillos,carne]")

#buscar_restaurante_por_tipo_de_comida("chRA")
#L_restaurantes()
#buscar_restaurante("Mussio")
#buscar_platillos_pais_origen("franciA")
#buscar_platillos_restaurante("banquetES")
buscar_ingrediente_platillo_restaurante("banquetes","queso")
