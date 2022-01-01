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
import funcionesBasicas
from sys import argv
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_UP

#######################################################################################
# INICIO del código común para todas las fichas
#######################################################################################
start = time.time()
sys.path.insert(0, './')
directorioArchivosXML = "./archivosXML/"

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
numeroEjercicios = int(input("Introduce el número de ejercicios de cada tipo: "))

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

numeroEjerciciosDiferentes = 7
#######################################################################################
# INICIO del código común para todas las fichas
#######################################################################################
# Creamos el archivo fuente LaTeX.
rutaArchivoLaTeX = directorioArchivosXML + nombreCategoria + r"_" + str(numeroEjercicios) + r"ejercicios_" + str(numeroEjerciciosDiferentes) + r"tipos.tex"
fLaTeX = open(rutaArchivoLaTeX, "w", encoding="utf8")
fLaTeX.write(r"\documentclass{article}"+"\n")
fLaTeX.write(r"\usepackage{moodle}"+"\n")
fLaTeX.write(r""+"\n")
fLaTeX.write(r"\begin{document}"+"\n")
fLaTeX.write(r"\begin{quiz}{" + nombreCategoria + r"}" + "\n")
listaAleatoriaTiposEjercicio = funcionesBasicas.generaListaAleatoriaTiposEjercicio(numeroEjerciciosDiferentes,numeroEjercicios)

for koko in range(len(listaAleatoriaTiposEjercicio)):
    print(str(koko),"de",str(len(listaAleatoriaTiposEjercicio)))
    exec("cadenas = generaEjercicioTipo" + str(listaAleatoriaTiposEjercicio[koko]) + "(parametros)")
    fLaTeX.write(r"\setcategory{" + nombreCategoria + r" / " + str(listaAleatoriaTiposEjercicio[koko]) + r"}" + "\n")
    # Usamos esto para equilibrar bien los cuestionarios.
    #######################################################################################
    # INICIO del código específico LaTeX Moodle para estas preguntas
    #######################################################################################
    # Rellena huecos
    fLaTeX.write(r"\begin{numerical}{" + nombreCategoria  + r"}" + "\n")
    fLaTeX.write(funcionesBasicas.corrigeCaracteresEspeciales(r"Lee el enunciado e introduce la respuesta redondeada a las centésimas:" + "\n"))
    fLaTeX.write(r"" + "\n")    
    fLaTeX.write(r"" + funcionesBasicas.corrigeCaracteresEspeciales(cadenas[0]) + "\n")
    fLaTeX.write(r"" + "\n")        
    fLaTeX.write(r"    \item[tolerance={0.001}] " + str(cadenas[1]) + "\n")
    fLaTeX.write(r"\end{numerical}"+"\n")
    #######################################################################################
    # FIN del código específico LaTeX Moodle para estas preguntas
    #######################################################################################
fLaTeX.write(r"\end{quiz}"+"\n")
fLaTeX.write(r"\end{document}"+"\n")
fLaTeX.close()
subprocess.run(["pdflatex","--interaction=batchmode","-output-directory=archivosXML", rutaArchivoLaTeX])
#######################################################################################
# FIN del código común para todas las fichas
#######################################################################################
