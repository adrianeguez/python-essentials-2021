#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 08:24:56 2021

@author: adrian
"""

def ejercicio_uno_uno():
    print("""
    Empezando a trabajar con Python
    Realizado por: "Vicente Adrian Eguez Sarzosa"
    """)
    print("Consultando los tipos de valores:")
    print("El tipo de dato de 875 es")
    print(type(875))
    # Se uso type para validar el tipo de dato del valor
    
    print("El tipo de dato de 4.89 es")
    print(type(4.89))
    # Se uso type para validar el tipo de dato del valor
    
    print("El tipo de dato del texto 'Now is better than never' es:")
    print(type("Now is better than never"))
    # Se uso type para validar el tipo de dato del valor
    
    print("El tipo de dato de 1.32 es")
    print(type(1.32))
    # Se uso type para validar el tipo de dato del valor
    
    print("¿El valor 5 + 8i corresponde a un valor entero?")
    print(isinstance(complex(2, 3), int))
    # Se uso isinstance para saber si la suma de un numero complejo es entero, es Falso
    
    print("¿El texto: 'Readability counts.' corresponde a un string?")
    print(isinstance("Readability counts.", str))
    # Se uso isinstance para saber si una cadena de caracteres es instancia de un str, es Verdadero