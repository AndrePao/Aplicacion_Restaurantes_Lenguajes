listarestaurantes(NombreR):-restaurante(NombreR,_,_,_,_,_).
restaurantes_tipo_comida(NombreR,TipoComida):-restaurante(NombreR,TipoComida,_,_,_,_).
buscar_restaurante(NombreR,TipoComida,Lugar,Tel,DiasAtencion, HorasAtencion2):-restaurante(NombreR,TipoComida,Lugar,Tel,DiasAtencion, HorasAtencion2).

restaurantes_pais(NombreR,NombrePais):- platillos(NombreR,_,_,NombrePais,_).
platillos_restaurantes(NombreR,NombrePlatillo):-platillos(NombreR,NombrePlatillo,_,_,_).

ingrediente_platillos_restaurante(NombreR,NombrePlatillo,Ingrediente):-platillos(NombreR,NombrePlatillo,_,_,[IngredienteL|ListaI]), member(Ingrediente,[IngredienteL|ListaI]).
platillos_pais(nombrep,nombrepais):-platillos(_,nombrep,_,nombrepais,_).

restaurante(banquetes,hawaiana, san_diego,22334455,sabado_lunes,7:00:10:00).
restaurante(mussio,chatarra, tres_rios,22334455,lunes_sabado,3:20:9:50).
restaurante(mc_donalds,chatarra, san_jose,22334455,lunes_viernes,4:00:6:00).
restaurante(kfc,chatarra, terramall,22334455,domingo_viernes,4:00:4:15).

platillos(banquetes,pizza,salado,francia,[pan,pina,queso]).
platillos(kfc,wrap,salado,francia,[tortilla,pollo,lechuga,tomate,queso]).
platillos(crustaseo_cascarudo,cangreburguer,salado,fondo_de_bikini,[pan,lechuga,tomate,pepinillos,carne]).
platillos(coffee,cafe,amargo,colombia,[cafe,azucar]).
platillos(chatarra,cafe,amargo,colombia,[cafe,azucar]).
platillos(chatarra,cafe,amargo,colombia,[cafe,azucar]).
platillos(coffi,helado,dulce,italia,azucar).
