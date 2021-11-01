def ejercicio_dos():
    ## Parte 1
    Datos_2021 = [15, 20, 3,91,4, 5, 6, 7,100,91,110,900,21,33,32, 2, 4,8,10,13,13,16,15,1302]
    arreglo_par = []
    arreglo_impar = []
    arreglo_atipico = []
    sumatoria = 0
    for dato in Datos_2021:
        if(dato % 2 == 0):
            arreglo_par.append(dato)
        else:
            arreglo_impar.append(dato)
        sumatoria = sumatoria + dato
    promedio = sumatoria / len(Datos_2021)
    for dato in Datos_2021:
        if(dato > promedio):
            arreglo_atipico.append(dato)
    print(f"Arreglo par: {arreglo_par}")
    print(f"Arreglo impar: {arreglo_impar}")
    print(f"Arreglo valores atipicos: {arreglo_atipico}")

    ## Parte 2

    password_texto = input("""
    Por favor ingrese su password cumpliendo estas validaciones:
    Debe contener al menos una letra minúscula entre las letras: a,b,c,d,e,f,g,h,i,j.
    Debe contener al menos una letra mayúscula entre las letras: K,L,M,N,O,P,Q,R,S,T.
    Debe contener al menos un número entre 0 y 9.
    Debe contener un símbolo especial entre: $,%,*,@
    Tamaño mínimo de 5 caracteres y máximo de 15.
    """)
    "a".count("a")

    def tiene_caracteres(arreglo_caracteres, texto):
        tiene_caracter = False
        for caracter in arreglo_caracteres:
            if(texto.count(caracter) > 0):
                tiene_caracter = True
        return tiene_caracter


    def validar_password(password):
        tiene_minuscula = tiene_caracteres(["a","b","c","d","e","f","g","h","i","j"], password)
        tiene_mayuscula = tiene_caracteres(["K","L","M","N","O","P","Q","R","S","T"], password)
        tiene_numero = tiene_caracteres(["0","1","2","3","4","5","6","7","8","9"], password)
        tiene_simbolo = tiene_caracteres(["$","%","*","@"], password)
        longitud = len(password)
        esta_entre_5_15 = longitud >= 5 and longitud <= 15
        if(tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_simbolo and esta_entre_5_15):
            return True
        else:
            return False
        
    password_valida = validar_password(password_texto)
    if(password_valida):
        print("Password valida")
    else:
        print("Password invalida")

    password_texto = input("""
    Por favor ingrese su password cumpliendo estas validaciones:
    Debe contener al menos una letra minúscula entre las letras: a,b,c,d,e,f,g,h,i,j.
    Debe contener al menos una letra mayúscula entre las letras: K,L,M,N,O,P,Q,R,S,T.
    Debe contener al menos un número entre 0 y 9.
    Debe contener un símbolo especial entre: $,%,*,@
    Tamaño mínimo de 5 caracteres y máximo de 15.
    """)
    "a".count("a")

    def tiene_caracteres(arreglo_caracteres, texto):
        tiene_caracter = False
        for caracter in arreglo_caracteres:
            if(texto.count(caracter) > 0):
                tiene_caracter = True
        return tiene_caracter


    def validar_password(password):
        tiene_minuscula = tiene_caracteres(["a","b","c","d","e","f","g","h","i","j"], password)
        tiene_mayuscula = tiene_caracteres(["K","L","M","N","O","P","Q","R","S","T"], password)
        tiene_numero = tiene_caracteres(["0","1","2","3","4","5","6","7","8","9"], password)
        tiene_simbolo = tiene_caracteres(["$","%","*","@"], password)
        longitud = len(password)
        esta_entre_5_15 = longitud >= 5 and longitud <= 15
        if(tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_simbolo and esta_entre_5_15):
            return True
        else:
            return False
        
    password_valida = validar_password(password_texto)
    if(password_valida):
        print("Password valida")
    else:
        print("Password invalida")

