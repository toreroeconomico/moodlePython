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
nombreCategoria = "ESO-MAT-x.x-MAC-2.2-sucesiones teoria"
numeroOperaciones = 1 # No hace falta que cada solución tenga más de una posibilidad, como sucede en criptografía.
# Esto no es muy eficiente, pero tiene la ventaja de que podemos reutilizar el código creado
# para las fichas de criptografía, en el que sí es necesario que haya más de una posibilidad para cada solución.
maximoPositivo = int(input("Introduce el máximo positivo: "))
parametros = [numeroOperaciones, maximoPositivo]
numeroEjercicios = int(input("Introduce el número de ejercicios de cada tipo: "))

#######################################################################################
# INICIO del código específico para esta ficha
#######################################################################################
def generaValoresDistintos(valorOriginal,numeroValoresDistintos,minimo,maximo):
    seguir = 1
    while seguir == 1:
        valoresDistintos = random.sample(range(minimo, maximo), numeroValoresDistintos)
        if valorOriginal not in valoresDistintos:
            return valoresDistintos

def generaEjercicioTipo1(parametros):
    numeroOperaciones = parametros[0]
    maximoPositivo = parametros[1]
    # Teoría
    enunciado = r"Una sucesión es recurrente cuando los nuevos términos a partir de una posición dependen de alguno de los anteriores."
    respuestaCorrecta = r"Verdadero"
    respuestaDistractor1 = r"Falso"
    respuestaDistractor2 = r""
    respuestaDistractor3 = r""
    return [enunciado,respuestaCorrecta,respuestaDistractor1,respuestaDistractor2,respuestaDistractor3]

def generaEjercicioTipo2(parametros):
    numeroOperaciones = parametros[0]
    maximoPositivo = parametros[1]
    # Teoría
    enunciado = r"Toda progresión aritmética es recurrente."
    respuestaCorrecta = r"Verdadero."
    respuestaDistractor1 = r"Falso"
    respuestaDistractor2 = r""
    respuestaDistractor3 = r""
    return [enunciado,respuestaCorrecta,respuestaDistractor1,respuestaDistractor2,respuestaDistractor3]
    
def generaEjercicioTipo3(parametros):
    numeroOperaciones = parametros[0]
    maximoPositivo = parametros[1]
    # Teoría
    enunciado = r"Para obtener nuevos términos de una sucesión recurrente necesitamos su término general."
    respuestaCorrecta = r"Inexacto."
    respuestaDistractor1 = r"Exacto"
    respuestaDistractor2 = r"Falso"
    respuestaDistractor3 = r""
    return [enunciado,respuestaCorrecta,respuestaDistractor1,respuestaDistractor2,respuestaDistractor3]
    
def generaEjercicioTipo4(parametros):
    numeroOperaciones = parametros[0]
    maximoPositivo = parametros[1]
    # Teoría
    enunciado = r"El término general de la sucesión de Fibonacci es:"
    respuestaCorrecta = r"$a_{n}=a_{n-1}+a_{n-2}$"
    respuestaDistractor1 = r"$a_{n}=a_{n+1}+a_{n-2}$"
    respuestaDistractor2 = r"$a_{n}=a_{n}+a_{n-2}$"
    respuestaDistractor3 = r"$a_{n}=a_{n-2}+a_{n-3}$"
    return [enunciado,respuestaCorrecta,respuestaDistractor1,respuestaDistractor2,respuestaDistractor3]
    
def generaEjercicioTipo5(parametros):
    numeroOperaciones = parametros[0]
    maximoPositivo = parametros[1]
    # Teoría
    enunciado = r"Para obtener nuevos términos de una sucesión recurrente necesitamos su término general y algunos de los primeros términos."
    respuestaCorrecta = r"Exacto"
    respuestaDistractor1 = r"Inexacto"
    respuestaDistractor2 = r"Falso"
    respuestaDistractor3 = r""    
    return [enunciado,respuestaCorrecta,respuestaDistractor1,respuestaDistractor2,respuestaDistractor3]
    
def generaEjercicioTipo6(parametros):
    numeroOperaciones = parametros[0]
    maximoPositivo = parametros[1]
    # Teoría
    enunciado = r"Toda sucesión tiene ley de formación."
    respuestaCorrecta = r"Falso"
    respuestaDistractor1 = r"Verdadero"
    respuestaDistractor2 = r""
    respuestaDistractor3 = r""    
    return [enunciado,respuestaCorrecta,respuestaDistractor1,respuestaDistractor2,respuestaDistractor3]

def generaEjercicioTipo7(parametros):
    numeroOperaciones = parametros[0]
    maximoPositivo = parametros[1]
    # Teoría
    enunciado = r"Si una sucesión tiene ley de formación, esta es única."
    respuestaCorrecta = r"Falso"
    respuestaDistractor1 = r"Verdadero"
    respuestaDistractor2 = r""
    respuestaDistractor3 = r""    
    return [enunciado,respuestaCorrecta,respuestaDistractor1,respuestaDistractor2,respuestaDistractor3]
    
def generaEjercicioTipo8(parametros):
    numeroOperaciones = parametros[0]
    maximoPositivo = parametros[1]
    # Teoría
    enunciado = r"Toda ley de formación se puede expresar algebraicamente."
    respuestaCorrecta = r"Falso"
    respuestaDistractor1 = r"Verdadero"
    respuestaDistractor2 = r""
    respuestaDistractor3 = r""    
    return [enunciado,respuestaCorrecta,respuestaDistractor1,respuestaDistractor2,respuestaDistractor3]

def generaEjercicioTipo9(parametros):
    numeroOperaciones = parametros[0]
    maximoPositivo = parametros[1]
    # Teoría
    enunciado = r"En una sucesión de Fibonacci, el número de oro aparece:"
    respuestaCorrecta = r"al dividir un elemento entre el anterior."
    respuestaDistractor1 = r"al dividir cualquier pareja de elementos."
    respuestaDistractor2 = r"al dividir un elemento entre el primero."
    respuestaDistractor3 = r"al dividir el primer elemento entre el último."
    return [enunciado,respuestaCorrecta,respuestaDistractor1,respuestaDistractor2,respuestaDistractor3]

def generaEjercicioTipo10(parametros):
    numeroOperaciones = parametros[0]
    maximoPositivo = parametros[1]
    # Teoría
    enunciado = r"¿Cuál de estas sucesiones habrá crecido más al cabo de 15 términos?"
    respuestaCorrecta = r"$a_{n}=(1,6)^n$"
    respuestaDistractor1 = r"$a_{n}=4n^2+3n$"
    respuestaDistractor2 = r"$a_{n}=60n+5$"
    respuestaDistractor3 = r"$a_{n}=500+10n$"
    return [enunciado,respuestaCorrecta,respuestaDistractor1,respuestaDistractor2,respuestaDistractor3]

def generaEjercicioTipo11(parametros):
    numeroOperaciones = parametros[0]
    maximoPositivo = parametros[1]
    # Teoría
    enunciado = r"Para que aparezca el número de oro en una sucesión de Fibonacci, es preciso que los dos primeros términos sean iguales."
    respuestaCorrecta = r"Falso"
    respuestaDistractor1 = r"Verdadero"
    respuestaDistractor2 = r""
    respuestaDistractor3 = r""
    return [enunciado,respuestaCorrecta,respuestaDistractor1,respuestaDistractor2,respuestaDistractor3]
    
def generaEjercicioTipo12(parametros):
    numeroOperaciones = parametros[0]
    maximoPositivo = parametros[1]
    # Teoría
    enunciado = r"¿Qué particularidad tendrá una sucesión con el siguiente término general: $a_{n}=(-1)^{n}\cdot{}(2n+1)$"
    respuestaCorrecta = r"Que genera números impares con signo alterno."
    respuestaDistractor1 = r"Que genera números impares."
    respuestaDistractor2 = r"Que genera números con signo alterno."
    respuestaDistractor3 = r"Ninguna."
    return [enunciado,respuestaCorrecta,respuestaDistractor1,respuestaDistractor2,respuestaDistractor3]
    
def generaEjercicioTipo13(parametros):
    numeroOperaciones = parametros[0]
    maximoPositivo = parametros[1]
    # Teoría
    enunciado = r"¿Qué particularidad tendrá una sucesión con el siguiente término general: $a_{n}=\dfrac{n^2+1}{n^2}$"
    respuestaCorrecta = r"Todas las opciones son ciertas."
    respuestaDistractor1 = r"Que el denominador de cada término es un cuadrado perfecto."
    respuestaDistractor2 = r"Que genera fracciones irreducibles."
    respuestaDistractor3 = r"Que genera términos cada vez más cercanos a 1."
    return [enunciado,respuestaCorrecta,respuestaDistractor1,respuestaDistractor2,respuestaDistractor3]     

numeroEjerciciosDiferentes = 13
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
    # Tipo test
    fLaTeX.write(r"\begin{multi}{" + nombreCategoria  + r"}" + "\n")
    fLaTeX.write(funcionesBasicas.corrigeCaracteresEspeciales(r"Lee el enunciado y elige la opción correcta:" + "\n"))
    fLaTeX.write(r"" + "\n")    
    fLaTeX.write(r"" + funcionesBasicas.corrigeCaracteresEspeciales(cadenas[0]) + "\n")
    fLaTeX.write(r"" + "\n")
    fLaTeX.write(r"    \item* " + funcionesBasicas.corrigeCaracteresEspeciales(cadenas[1]) + "\n") # El segundo elemento es la respuesta correcta.
    fLaTeX.write(r"    \item " + funcionesBasicas.corrigeCaracteresEspeciales(cadenas[2]) + "\n") # El resto de elementos son los distractores.
    if cadenas[3] != "":
        fLaTeX.write(r"    \item " + funcionesBasicas.corrigeCaracteresEspeciales(cadenas[3]) + "\n")
    if cadenas[4] != "":
        fLaTeX.write(r"    \item " + funcionesBasicas.corrigeCaracteresEspeciales(cadenas[4]) + "\n")
    fLaTeX.write(r"\end{multi}"+"\n")
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
