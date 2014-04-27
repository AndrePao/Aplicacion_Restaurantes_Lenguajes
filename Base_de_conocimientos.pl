restaurante(banquetes,hawaiana, san_diego,22334455,sabado_lunes,7000).
restaurante(mussio,chatarra, tres_rios,22334455,lunes_sabado,32090).
restaurante(mc_donalds,chatarra, san_jose,22334455,lunes_viernes,4006).
restaurante(kfc,chatarra, terramall,22334455,domingo_viernes,40045).

platillos(banquetes,pizza,salado,francia,[pan,pina,queso]).
platillos(kfc,wrap,salado,francia,[tortilla,pollo,lechuga,tomate,queso]).

listarestaurantes(NombreR):-restaurante(NombreR,_,_,_,_,_).
restaurantes_tipo_comida(NombreR,TipoComida):-restaurante(NombreR,TipoComida,_,_,_,_).
buscar_restaurante(NombreR,TipoComida,Lugar,Tel,DiasAtencion, HorasAtencion2):-restaurante(NombreR,TipoComida,Lugar,Tel,DiasAtencion, HorasAtencion2).

restaurantes_pais(NombreR,NombrePais):- platillos(NombreR,_,_,NombrePais,_).
platillos_restaurantes(NombreR,NombrePlatillo):-platillos(NombreR,NombrePlatillo,_,_,_).

ingrediente_platillos_restaurante(NombreR,NombrePlatillo,Ingrediente):-platillos(NombreR,NombrePlatillo,_,_ListaI), member(Ingrediente,[Ingrediente|).
