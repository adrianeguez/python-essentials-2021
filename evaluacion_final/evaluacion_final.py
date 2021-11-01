#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 08:22:35 2021

@author: adrian
"""

import fun_ejercicio_1_1
import fun_ejercicio_1_2
import fun_ejercicio_2
import fun_ejercicio_3

opcion = ""
while opcion != "0":
    opcion = input ("""
    Seleccione una de las opciones (Ej: 1):
    1) Ejercicio 1
    2) Ejercicio 2
    0) Salir
    """)
    if(opcion == "1"):
        fun_ejercicio_1_1.ejercicio_uno_uno()
    if(opcion == "2"):
        fun_ejercicio_1_2.ejercicio_uno_dos()
    if(opcion == "3"):
        fun_ejercicio_2.ejercicio_dos()
    if(opcion == "4"):
        fun_ejercicio_3.ejercicio_uno_dos()
