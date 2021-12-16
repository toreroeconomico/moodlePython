#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 15:46:16 2020

@author: sergio
"""
import random
import subprocess
import numpy as np
import time
import math
import sys
from sys import argv
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_UP

#######################################################################################
# INICIO del código común para todas las fichas
#######################################################################################
start = time.time()
sys.path.insert(0, './')
directorioArchivosXML = "./archivosXML/"

def corrigeAcentos(cadena):
    # Moodle no acepta los acentos ni la ñ tal cual. Hay que escribirlos entre llaves.
    cadena = cadena.replace(r"á",r"\'{a}")
    cadena = cadena.replace(r"é",r"\'{e}")
    cadena = cadena.replace(r"í",r"\'{i}")
    cadena = cadena.replace(r"ó",r"\'{o}")
    cadena = cadena.replace(r"ú",r"\'{u}")
    cadena = cadena.replace(r"ñ",r"\~{n}")
    return cadena

def corrigeComa(cadena):
    # Moodle no acepta los acentos ni la ñ tal cual. Hay que escribirlos entre llaves.
    cadena = cadena.replace(r".",r",")
    return cadena

def generaListaAleatoriaTiposEjercicio(numeroEjerciciosDiferentes,numeroEjercicios):
    listaAleatoriaTiposEjercicio = []
    for kupi in range(int(numeroEjercicios/numeroEjerciciosDiferentes)+1):
        listaAleatoriaTiposEjercicio += random.sample(range(1,numeroEjerciciosDiferentes+1), numeroEjerciciosDiferentes)
    return listaAleatoriaTiposEjercicio

#######################################################################################
# FIN del código común para todas las fichas
#######################################################################################

#######################################################################################
# Parámetros
#######################################################################################
nombreCategoria = "ESO-MAT-2.5-MAC-x.x-calculo porcentajes"
numeroOperaciones = 1 # No hace falta que cada solución tenga más de una posibilidad, como sucede en criptografía.
# Esto no es muy eficiente, pero tiene la ventaja de que podemos reutilizar el código creado
# para las fichas de criptografía, en el que sí es necesario que haya más de una posibilidad para cada solución.
minimoValorParte = 120
maximoValorParte = 6000
minimoFactor = 1
maximoFactor = 20
minimoPorcentaje = 5
maximoPorcentaje = 150
maximoPositivo = int(input("Introduce el máximo positivo: "))
#minimo = 1
#maximo = 5
parametros = [minimoValorParte,maximoValorParte,minimoFactor,maximoFactor,minimoPorcentaje,maximoPorcentaje]
numeroEjercicios = int(input("Introduce el número de ejercicios: "))

numeroEjerciciosDiferentes = 7
#######################################################################################
# INICIO del código específico para esta ficha
#######################################################################################
def generaEjercicioTipo1(parametros):
    minimoValorParte = parametros[0]
    maximoValorParte = parametros[1]
    minimoFactor = parametros[2]
    maximoFactor = parametros[3]
    minimoPorcentaje = parametros[4]
    maximoPorcentaje = parametros[5]
    cadenas = [[] for i in range(2)]
    valorParte = random.randint(minimoValorParte,maximoValorParte)
    valorTodo = random.randint(minimoFactor*valorParte,maximoFactor*valorParte)/4
    porcentajeParte = round(valorParte/valorTodo*100,2)
    # Cálculo porcentaje parte
    cadenas[0] = str(valorParte).replace(r".",r",") + " de " + str(valorTodo).replace(r".",r",") + " supone un porcentaje del ..."
    cadenas[1] = porcentajeParte
    return cadenas
    
def generaEjercicioTipo2(parametros):
    minimoValorParte = parametros[0]
    maximoValorParte = parametros[1]
    minimoFactor = parametros[2]
    maximoFactor = parametros[3]
    minimoPorcentaje = parametros[4]
    maximoPorcentaje = parametros[5]
    cadenas = [[] for i in range(2)]
    # Cálculo valor parte
    porcentajeParte = random.randrange(minimoPorcentaje,maximoPorcentaje,5)
    valorTodo = random.randrange(minimoFactor*maximoValorParte,maximoFactor*maximoValorParte,25)
    valorParte = round(porcentajeParte*valorTodo/100,2)
    cadenas[0] = "El " + str(porcentajeParte).replace(r".",r",") + " por ciento de " + str(valorTodo).replace(r".",r",") + " es ..."
    cadenas[1] = valorParte
    return cadenas
    
def generaEjercicioTipo3(parametros):
    minimoValorParte = parametros[0]
    maximoValorParte = parametros[1]
    minimoFactor = parametros[2]
    maximoFactor = parametros[3]
    minimoPorcentaje = parametros[4]
    maximoPorcentaje = parametros[5]
    cadenas = [[] for i in range(2)]
    # Cálculo valor todo
    maximoPositivo = random.randint(1,20)
    valorParte = maximoPositivo*random.randint(minimoValorParte,maximoValorParte)
    porcentajeParte = 2*5*maximoPositivo
    valorTodo = valorParte/porcentajeParte*100
    cadenas[0] = "Si el " + str(porcentajeParte).replace(r".",r",") + " por ciento de una cantidad es " + str(valorParte).replace(r".",r",") + ", esa cantidad es ..."
    cadenas[1] = valorTodo
    return cadenas        

def generaEjercicioTipo4(parametros):
    minimoValorParte = parametros[0]
    maximoValorParte = parametros[1]
    minimoFactor = parametros[2]
    maximoFactor = parametros[3]
    minimoPorcentaje = parametros[4]
    maximoPorcentaje = parametros[5]
    cadenas = [[] for i in range(2)]
    # Cálculo valor todo
    maximoPositivo = random.randint(1,20)
    cantidadInicial = maximoPositivo*random.randint(minimoValorParte,maximoValorParte)
    cambioPorcentual = 2*5*maximoPositivo
    nuevaCantidad = cantidadInicial*(100+cambioPorcentual)/100
    cadenas[0] = "Si una cantidad por valor de " + str(cantidadInicial).replace(r".",r",") + r" ha aumentado un " + str(cambioPorcentual).replace(r".",r",") + " por ciento, la nueva cantidad será... "
    cadenas[1] = nuevaCantidad
    return cadenas        

def generaEjercicioTipo5(parametros):
    minimoValorParte = parametros[0]
    maximoValorParte = parametros[1]
    minimoFactor = parametros[2]
    maximoFactor = parametros[3]
    minimoPorcentaje = parametros[4]
    maximoPorcentaje = parametros[5]
    cadenas = [[] for i in range(2)]
    # Cálculo valor todo
    maximoPositivo = random.randint(1,8)
    cantidadInicial = maximoPositivo*random.randint(minimoValorParte,maximoValorParte)
    cambioPorcentual = 2*5*maximoPositivo
    nuevaCantidad = cantidadInicial*(100-cambioPorcentual)/100
    cadenas[0] = "Si una cantidad por valor de " + str(cantidadInicial).replace(r".",r",") + r" ha disminuido un " + str(cambioPorcentual).replace(r".",r",") + " por ciento, la nueva cantidad será... "
    cadenas[1] = nuevaCantidad
    return cadenas  

def generaEjercicioTipo6(parametros):
    minimoValorParte = parametros[0]
    maximoValorParte = parametros[1]
    minimoFactor = parametros[2]
    maximoFactor = parametros[3]
    minimoPorcentaje = parametros[4]
    maximoPorcentaje = parametros[5]
    cadenas = [[] for i in range(2)]
    # Cálculo valor todo
    maximoPositivo = random.randint(1,20)
    cantidadInicial = maximoPositivo*random.randint(minimoValorParte,maximoValorParte)
    cambioPorcentual = 2*5*maximoPositivo
    nuevaCantidad = cantidadInicial*(100+cambioPorcentual)/100
    cadenas[0] = "Si una cantidad ha aumentado un " + str(cambioPorcentual).replace(r".",r",") + " por ciento y ahora tiene un valor de " + str(nuevaCantidad).replace(r".",r",") + r", antes valía..."
    cadenas[1] = cantidadInicial
    return cadenas        

def generaEjercicioTipo7(parametros):
    minimoValorParte = parametros[0]
    maximoValorParte = parametros[1]
    minimoFactor = parametros[2]
    maximoFactor = parametros[3]
    minimoPorcentaje = parametros[4]
    maximoPorcentaje = parametros[5]
    cadenas = [[] for i in range(2)]
    # Cálculo valor todo
    maximoPositivo = random.randint(1,8)
    cantidadInicial = maximoPositivo*random.randint(minimoValorParte,maximoValorParte)
    cambioPorcentual = 2*5*maximoPositivo
    nuevaCantidad = cantidadInicial*(100-cambioPorcentual)/100
    cadenas[0] = "Si una cantidad ha disminuido un " + str(cambioPorcentual).replace(r".",r",") + " por ciento y ahora tiene un valor de " + str(nuevaCantidad).replace(r".",r",") + r", antes valía..."
    cadenas[1] = cantidadInicial
    return cadenas        


#######################################################################################
# INICIO del código específico LaTeX Moodle para estos ejercicios
#######################################################################################
# Creamos el archivo fuente LaTeX.
rutaArchivoLaTeX = directorioArchivosXML + nombreCategoria + r"_" + str(numeroEjercicios) + r"ejercicios_" + str(numeroEjerciciosDiferentes) + r"tipos.tex"
fLaTeX = open(rutaArchivoLaTeX, "w", encoding="utf8")
fLaTeX.write(r"\documentclass{article}"+"\n")
fLaTeX.write(r"\usepackage{moodle}"+"\n")
fLaTeX.write(r""+"\n")
fLaTeX.write(r"\begin{document}"+"\n")
fLaTeX.write(r"\begin{quiz}{" + nombreCategoria + r"}" + "\n")
listaAleatoriaTiposEjercicio = generaListaAleatoriaTiposEjercicio(numeroEjerciciosDiferentes,numeroEjercicios)

for koko in range(numeroEjercicios):
    print(str(koko),"de",str(numeroEjercicios))
    exec("cadenas = generaEjercicioTipo" + str(listaAleatoriaTiposEjercicio[koko]) + "(parametros)")
    # Rellena huecos
    fLaTeX.write(r"\begin{numerical}{" + nombreCategoria  + r"}" + "\n")
    fLaTeX.write(corrigeAcentos(r"Lee el enunciado e introduce la respuesta redondeada a las centésimas:" + "\n"))
    fLaTeX.write(r"" + "\n")    
    fLaTeX.write(r"" + corrigeAcentos(cadenas[0]) + "\n")
    fLaTeX.write(r"" + "\n")        
    fLaTeX.write(r"    \item[tolerance={0.001}] " + str(cadenas[1]) + "\n")
    fLaTeX.write(r"\end{numerical}"+"\n")    
fLaTeX.write(r"\end{quiz}"+"\n")
fLaTeX.write(r"\end{document}"+"\n")
fLaTeX.close()
subprocess.run(["pdflatex","--interaction=batchmode","-output-directory=archivosXML", rutaArchivoLaTeX])
