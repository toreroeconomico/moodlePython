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
nombreCategoria = "ESO-MAT-x.x-MAC-2.2-sucesiones ejercicios"
numeroOperaciones = 1 # No hace falta que cada solución tenga más de una posibilidad, como sucede en criptografía.
# Esto no es muy eficiente, pero tiene la ventaja de que podemos reutilizar el código creado
# para las fichas de criptografía, en el que sí es necesario que haya más de una posibilidad para cada solución.
maximoPositivo = int(input("Introduce el máximo positivo: "))
parametros = [numeroOperaciones, maximoPositivo]
numeroEjercicios = int(input("Introduce el número de ejercicios de cada tipo: "))

#######################################################################################
# INICIO del código específico para esta ficha
#######################################################################################
def generaEjercicioTipo1(parametros):
    numeroOperaciones = parametros[0]
    maximoPositivo = parametros[1]
    # Continúa una sucesión de primer orden
    posicionInicial = random.randrange(1, maximoPositivo)
    # Creamos el término general de la sucesión y de las distractoras
    ACorrecta = (-1)**random.randrange(2)*random.randrange(round(maximoPositivo/2), maximoPositivo)
    BCorrecta = (-1)**random.randrange(2)*random.randrange(round(maximoPositivo/2), maximoPositivo)
    numeroValoresDistintos = 1 # Queremos tres sucesiones distractoras.
    ADistractores = funcionesBasicas.generaValoresDistintos(ACorrecta,numeroValoresDistintos,2,maximoPositivo)
    BDistractores = funcionesBasicas.generaValoresDistintos(BCorrecta,numeroValoresDistintos,2,maximoPositivo)
    respuestaCorrecta = "("
    distractor1 = "("
    distractor2 = "("
    for nuji in range(4):
        respuestaCorrecta += str(ACorrecta*(posicionInicial+nuji)+BCorrecta) + r","
        distractor1 += str(ACorrecta*(posicionInicial+nuji+1)+BCorrecta) + r"," # La posición es incorrecta
        distractor2 += str(ACorrecta*(posicionInicial+nuji-1)+BCorrecta) + r"," # La posición es incorrecta
    distractor3 = "("    
    for nuji in range(2):
        distractor3 += str(ACorrecta*(posicionInicial+nuji)+BCorrecta) + r"," # Las dos primeras están bien.
    for nuji in range(2):
        distractor3 += str(ADistractores[0]*(posicionInicial+nuji+2)+BDistractores[0]) + r"," # Las dos últimas están mal.

    respuestaCorrecta = respuestaCorrecta[0:-1] + r")" # Para quitar la coma final y poner el paréntesis de cierre.
    distractor1 = distractor1[0:-1] + r")" # Para quitar la coma final y poner el paréntesis de cierre.
    distractor2 = distractor2[0:-1] + r")" # Para quitar la coma final y poner el paréntesis de cierre.
    distractor3 = distractor3[0:-1] + r")" # Para quitar la coma final y poner el paréntesis de cierre.
    if BCorrecta > 0:
        enunciado = r"De la sucesión con término general $a_{n}=" + str(ACorrecta) + r"n+" + str(BCorrecta) + r"$ se han obtenido los términos $a_{" + str(posicionInicial) + r"}$," + r"$a_{" + str(posicionInicial+1) + r"}$," + r"$a_{" + str(posicionInicial+2) + r"}$," + r"$a_{" + str(posicionInicial+3) + r"}$. Estos cuatro términos son:"
    else:
        enunciado = r"De la sucesión con término general $a_{n}=" + str(ACorrecta) + r"n" + str(BCorrecta) + r"$ se han obtenido los términos $a_{" + str(posicionInicial) + r"}$," + r"$a_{" + str(posicionInicial+1) + r"}$," + r"$a_{" + str(posicionInicial+2) + r"}$," + r"$a_{" + str(posicionInicial+3) + r"}$. Estos cuatro términos son:"
    return [enunciado,respuestaCorrecta,distractor1,distractor2,distractor3]

def generaEjercicioTipo2(parametros):
    numeroOperaciones = parametros[0]
    maximoPositivo = parametros[1]
    # Continúa una sucesión recurrente
    a1 = random.randrange(1, maximoPositivo)
    a2 = random.randrange(1, maximoPositivo)
    a3 = random.randrange(1, maximoPositivo)
    ACorrecta = (-1)**random.randrange(2)*random.randrange(round(maximoPositivo/2), maximoPositivo)
    BCorrecta = (-1)**random.randrange(2)*random.randrange(round(maximoPositivo/2), maximoPositivo)
    # Creamos el término general de la sucesión y de las distractoras
    sucesionCorrecta = [a1, a2, a3]
    sucesionDistractor1 = [a1, a2, a3]
    sucesionDistractor2 = [a1, a2, a3]
    sucesionDistractor3 = [a1, a2, a3]
    for n in range(0,4):
        sucesionCorrecta.append(ACorrecta*sucesionCorrecta[n] + BCorrecta*sucesionCorrecta[n+1])
        sucesionDistractor1.append(ACorrecta*sucesionCorrecta[n] + BCorrecta*sucesionCorrecta[n+2])
        sucesionDistractor2.append(ACorrecta*sucesionCorrecta[n] - BCorrecta*sucesionCorrecta[n+1] + 1)
        sucesionDistractor3.append(ACorrecta*sucesionCorrecta[n] - BCorrecta*sucesionCorrecta[n+1] - 1)
    if BCorrecta > 0:
        enunciado = r"En la sucesión recurrente con término general $a_{n}=" + str(ACorrecta) + r"\cdot{}a_{n-3}+" + str(BCorrecta) + r"\cdot{}a_{n-2}$ y $a_{1}=" + str(a1) + r"$," + r"$a_{2}=" + str(a2) + r"$," + r"$a_{3}=" + str(a3) + r"$, los términos $a_{4}, a_{5}, a_{6}$ y $a_{7}$ son:"
    else:
        enunciado = r"En la sucesión recurrente con término general $a_{n}=" + str(ACorrecta) + r"\cdot{}a_{n-3}" + str(BCorrecta) + r"\cdot{}a_{n-2}$ y $a_{1}=" + str(a1) + r"$," + r"$a_{2}=" + str(a2) + r"$," + r"$a_{3}=" + str(a3) + r"$, los términos $a_{4}, a_{5}, a_{6}$ y $a_{7}$ son:"
    respuestaSucesionCorrecta = r"("
    respuestaSucesionDistractor1 = r"("
    respuestaSucesionDistractor2 = r"("
    respuestaSucesionDistractor3 = r"("
    for nuji in range(4):
        respuestaSucesionCorrecta += str(sucesionCorrecta[3+nuji]) + r","
        respuestaSucesionDistractor1 += str(sucesionDistractor1[3+nuji]) + r","
        respuestaSucesionDistractor2 += str(sucesionDistractor2[3+nuji]) + r","
        respuestaSucesionDistractor3 += str(sucesionDistractor3[3+nuji]) + r","
    respuestaSucesionCorrecta = respuestaSucesionCorrecta[0:-1] + r")" # Para quitar la coma final
    respuestaSucesionDistractor1 = respuestaSucesionDistractor1[0:-1] + r")" # Para quitar la coma final
    respuestaSucesionDistractor2 = respuestaSucesionDistractor2[0:-1] + r")" # Para quitar la coma final
    respuestaSucesionDistractor3 = respuestaSucesionDistractor3[0:-1] + r")" # Para quitar la coma final
    return [enunciado,respuestaSucesionCorrecta,respuestaSucesionDistractor1,respuestaSucesionDistractor2,respuestaSucesionDistractor3]
    
def generaEjercicioTipo3(parametros):
    numeroOperaciones = parametros[0]
    maximoPositivo = parametros[1]
    # Término general de una progresión aritmética
    a1 = (-1)**random.randrange(2)*random.randrange(round(maximoPositivo/2), 2*maximoPositivo)
    d = (-1)**random.randrange(2)*random.randrange(round(maximoPositivo/2), 2*maximoPositivo)
    PA = [a1]
    for nujop in range(5*maximoPositivo):
        PA.append(PA[-1]+d)
    posicionTerminoA = random.randrange(1*maximoPositivo,3*maximoPositivo)
    posicionTerminoB = random.randrange(4*maximoPositivo,5*maximoPositivo)
    
    enunciado = r"De una progresión aritmética sabemos $a_{" + str(posicionTerminoA+1) + "}=" + str(PA[posicionTerminoA]) + r"$ y $a_{" + str(posicionTerminoB+1) + "}=" + str(PA[posicionTerminoB]) + r"$. ¿Cuál de estos es su término general?"
    if d>0:
        respuestaCorrecta = r"$a_{n}=" + str(a1) + r"+" + str(d)+ r"\cdot{}(n-1)$"
        respuestaDistractor1 = r"$a_{n}=" + str(a1+d) + r"+" + str(d+1)+ r"\cdot{}(n-1)$"
        respuestaDistractor2 = r"$a_{n}=" + str(a1-d) + r"+" + str(d-1)+ r"\cdot{}(n-1)$"
        respuestaDistractor3 = r"$a_{n}=" + str(a1-d-1) + r"+" + str(d+2)+ r"\cdot{}(n-1)$"
    else:
        respuestaCorrecta = r"$a_{n}=" + str(a1) + r"" + str(d)+ r"\cdot{}(n-1)$"
        respuestaDistractor1 = r"$a_{n}=" + str(a1+d) + r"" + str(d+1)+ r"\cdot{}(n-1)$"
        respuestaDistractor2 = r"$a_{n}=" + str(a1-d) + r"" + str(d-1)+ r"\cdot{}(n-1)$"
        respuestaDistractor3 = r"$a_{n}=" + str(a1-d-1) + r"" + str(d+2)+ r"\cdot{}(n-1)$"        
    return [enunciado,respuestaCorrecta,respuestaDistractor1,respuestaDistractor2,respuestaDistractor3]

def generaEjercicioTipo4(parametros):
    numeroOperaciones = parametros[0]
    maximoPositivo = parametros[1]
    # Término general de una progresión aritmética
    a1 = (-1)**random.randrange(2)*random.randrange(round(maximoPositivo/2), maximoPositivo)
    d = (-1)**random.randrange(2)*random.randrange(round(maximoPositivo/2), maximoPositivo)
    PA = [a1]
    for nujop in range(99):
        PA.append(PA[-1]+d)
    posicionTerminoA = random.randrange(2*maximoPositivo,3*maximoPositivo)
    posicionTerminoB = random.randrange(4*maximoPositivo,5*maximoPositivo)
    #print(PA[0])
    #print(PA[-1])
    enunciado = r"De una progresión aritmética sabemos $a_{" + str(posicionTerminoA+1) + "}=" + str(PA[posicionTerminoA]) + r"$ y $a_{" + str(posicionTerminoB+1) + "}=" + str(PA[posicionTerminoB]) + r"$. ¿Cuánto es la suma de sus 100 primeros términos?"
    respuestaCorrecta = r"$" + str(50*(PA[0]+PA[-1])) + "$"
    respuestaDistractor1 = r"$" + str(51*(PA[0]+PA[-1])) + "$"
    respuestaDistractor2 = r"$" + str(50*(PA[0]+PA[-1]+d)) + "$"
    respuestaDistractor3 = r"$" + str(50*(PA[0]+PA[-1]-d)) + "$"
    return [enunciado,respuestaCorrecta,respuestaDistractor1,respuestaDistractor2,respuestaDistractor3]

numeroEjerciciosDiferentes = 4
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
    fLaTeX.write(r"\begin{multi}{" + nombreCategoria + r"}" + "\n")    
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
