def ejercicio_dos():
    opcion = ""
            
    def obtener_valores(diccionario):
        arreglo_numeros = []
        valores_diccionario = diccionario.values()
        for valor in valores_diccionario:
            tipo = type(valor)
            lista = isinstance(valor, list) == True
            tupla = isinstance(valor, tuple) == True
            es_lista = isinstance(valor, list) == True
            es_tupla = isinstance(valor, tuple) == True
            if(es_lista or es_tupla):
                for valor_arreglo in valor:
                    arreglo_numeros.append(valor_arreglo)
            else:
                arreglo_numeros.append(valor)
        return arreglo_numeros

    def obtener_longitud(diccionario):
        arreglo_numeros = []
        valores_diccionario = diccionario.values()
        for valor in valores_diccionario:
            tipo = type(valor)
            es_lista = isinstance(valor, list) == True
            es_tupla = isinstance(valor, tuple) == True
            if(es_lista or es_tupla):
                for valor_arreglo in valor:
                    arreglo_numeros.append(valor_arreglo)
            else:
                arreglo_numeros.append(valor)
        return len(arreglo_numeros)

    while opcion != "2":
        opcion = input ("""
        Seleccione una de las opciones (Ej: 1):
        1) Demostración del cálculo de valores altos y bajos en diccionarios.
        2) Salir
        """)
        if(opcion == "1"):
            
            dic_uno = {"Raul":34,"Paula":19,"Jorge":43,"Richard":10,"Diana":3,"Isabel":76,"Gustavo":12,"Diego":37} 
            longitud_dic_uno = obtener_longitud(dic_uno)
            
            dic_dos = {"tplA":(4,-12,56,-34,98,102),"tplB":(9,0,1,10,-3,14),"tlpC":(87,12,56,987,-61)}
            longitud_dic_dos = obtener_longitud(dic_dos)
            
            dic_tres = {"val1":-12.5,"val2":12.5,"val3":83,"val4":2.1,"val5":23,"val6":100,"val7":13.4,"val8":92}
            longitud_dic_tres = obtener_longitud(dic_tres)
            
            dic_cuatro = {"lst1":[4,6,-12,56,-9,5.7,33,100],"lst2":[9,0,81,-2,-56,],"lst3":[12,31,87,1,0,4,-11]}
            longitud_dic_cuatro = obtener_longitud(dic_cuatro)
            
            opcion_diccionario = input("""
            Elija un diccionario para la demostración:
            1) {Raul:34,Paula:19,Jorge:43,Richard:10,Diana:3,Isabel:76,Gustavo:12,Diego:37}
            2) {tplA:(4,-12,56,-34,98,102),tplB:(9,0,1,10,-3,14),tlpC:(87,12,56,987,-61)}
            3) {val1:-12.5,val2:12.5,val3:83,val4:2.1,val5:23,val6:100,val7:13.4,val8:92}
            4) {lst1:[4,6,-12,56,-9,5.7,33,100],lst2:[9,0,81,-2,-56,],lst3:[12,31,87,1,0,4,-11]}
            """)
            if(opcion_diccionario == "1" or opcion_diccionario == "2" or opcion_diccionario == "3" or opcion_diccionario == "4"):
                longitud_maxima = 0
                if(opcion_diccionario == "1"):
                    longitud_maxima = longitud_dic_uno
                if(opcion_diccionario == "2"):
                    longitud_maxima = longitud_dic_dos
                if(opcion_diccionario == "3"):
                    longitud_maxima = longitud_dic_tres
                if(opcion_diccionario == "4"):
                    longitud_maxima = longitud_dic_cuatro
                numero_altos = int(input(f"Ingrese el numero de valores altos entre 0 y {longitud_maxima}: "))
                numero_bajos = int(input(f"Ingrese el numero de valores bajos entre 0 y {longitud_maxima}: "))
                if(numero_altos > longitud_maxima or numero_altos < 0 or numero_bajos > longitud_maxima or numero_bajos < 0):
                    print("El numero de bajos o altos fue seleccionado fuera del rango")
                else:
                    lista_valores = []
                    if(opcion_diccionario == "1"):
                        lista_valores = obtener_valores(dic_uno)
                    if(opcion_diccionario == "2"):
                        lista_valores = obtener_valores(dic_dos)
                    if(opcion_diccionario == "3"):
                        lista_valores = obtener_valores(dic_tres)
                    if(opcion_diccionario == "4"):
                        lista_valores = obtener_valores(dic_cuatro)
                    lista_valores.sort()
                    print("MENORES")
                    print("Lista menores tupla")
                    print(tuple(lista_valores[:numero_bajos]))
                    print("Lista menores lista")
                    print(lista_valores[:numero_bajos])
                    print("MAYORES")
                    print("Lista mayores tupla")
                    print(tuple(lista_valores[-1 * (numero_altos):]))
                    print("Lista mayores lista")
                    print(lista_valores[-1 * (numero_altos):])
                
            else:
                print("No selecciono una opcion de diccionario correcto")
        else:
            if(opcion != "2"):
                print("Seleccione una opcion correcta")

