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
nombreCategoria = "ESO-MAT-2.1-MAC-2.1-notacion cientifica grandes"
numeroOperaciones = 1 # No hace falta que cada solución tenga más de una posibilidad, como sucede en criptografía.
# Esto no es muy eficiente, pero tiene la ventaja de que podemos reutilizar el código creado
# para las fichas de criptografía, en el que sí es necesario que haya más de una posibilidad para cada solución.
maximoPositivo = int(input("Introduce el máximo positivo: "))
parametros = [numeroOperaciones, maximoPositivo]
numeroEjercicios = int(input("Introduce el número de ejercicios de cada tipo: "))

#######################################################################################
# INICIO del código específico para esta ficha
#######################################################################################

diccionarioOrdenesMagnitud = {'cientos': 2, 'miles': 3, 'decenas de miles': 4, 'cientos de miles': 5, 'millones': 6, 'decenas de millones': 7, 'cientos de millones': 8, 'miles de millones': 9, 'decenas de miles de millones': 10,  'cientos de miles de millones': 11, 'billones': 12, 'decenas de billones': 13, 'cientos de billones': 14, 'miles de billones': 15, 'decenas de miles de billones': 16, 'cientos de miles de billones': 17, 'trillones': 18}

def generaValoresDistintos(valorOriginal,numeroValoresDistintos,minimo,maximo):
    seguir = 1
    while seguir == 1:
        valoresDistintos = random.sample(range(minimo, maximo), numeroValoresDistintos)
        if valorOriginal not in valoresDistintos:
            return valoresDistintos

def generaEjercicioTipo1(parametros):
    # Lectura orden de magnitud
    numeroOperaciones = parametros[0]
    maximoPositivo = parametros[1]
    
    exponenteCorrecto = random.randrange(2,19)
    numeroValoresDistintos = 3
    distractores = generaValoresDistintos(exponenteCorrecto,numeroValoresDistintos,max(2,exponenteCorrecto-4),min(19,exponenteCorrecto+4))
    enunciado = r"El orden de magnitud de $" + str(random.randrange(100,1000)/100).replace('.',',') + r"\cdot{}" + r"10^{" + str(exponenteCorrecto) + r"}$ es:"
    dict_items=diccionarioOrdenesMagnitud.items()
    ordenMagnitudCorrecto = ""
    ordenMagnitudDistractor1 = ""
    ordenMagnitudDistractor2 = ""
    ordenMagnitudDistractor3 = ""
    for key,value in dict_items:
        if value == exponenteCorrecto:
            ordenMagnitudCorrecto = key
        elif value == distractores[0]:
            ordenMagnitudDistractor1 = key
        elif value == distractores[1]:
            ordenMagnitudDistractor2 = key
        elif value == distractores[2]:
            ordenMagnitudDistractor3 = key
    return [enunciado,ordenMagnitudCorrecto,ordenMagnitudDistractor1,ordenMagnitudDistractor2,ordenMagnitudDistractor3]
    
def generaEjercicioTipo2(parametros):
    # Corrección por mantisa demasiado pequeña
    numeroOperaciones = parametros[0]
    maximoPositivo = parametros[1]
    
    numeradorMantisaIncorrecta = random.randrange(1,999)
    ordenMagnitudIncorrecto = random.randrange(2,19)
    dict_items=diccionarioOrdenesMagnitud.items()
    if numeradorMantisaIncorrecta < 10:
        numeradorMantisaCorrecta = numeradorMantisaIncorrecta*10000
        ordenMagnitudCorrecto = ordenMagnitudIncorrecto-4
        ordenMagnitudDistractor1 = ordenMagnitudIncorrecto+4
        ordenMagnitudDistractor2 = ordenMagnitudIncorrecto-2
        ordenMagnitudDistractor3 = ordenMagnitudIncorrecto-3
    elif numeradorMantisaIncorrecta < 100:
        numeradorMantisaCorrecta = numeradorMantisaIncorrecta*1000
        ordenMagnitudCorrecto = ordenMagnitudIncorrecto-3
        ordenMagnitudDistractor1 = ordenMagnitudIncorrecto+3
        ordenMagnitudDistractor2 = ordenMagnitudIncorrecto-1
        ordenMagnitudDistractor3 = ordenMagnitudIncorrecto+2        
    elif numeradorMantisaIncorrecta < 1000:
        numeradorMantisaCorrecta = numeradorMantisaIncorrecta*100
        ordenMagnitudCorrecto = ordenMagnitudIncorrecto-2
        ordenMagnitudDistractor1 = ordenMagnitudIncorrecto+2
        ordenMagnitudDistractor2 = ordenMagnitudIncorrecto-1
        ordenMagnitudDistractor3 = ordenMagnitudIncorrecto+1        
    else:
        numeradorMantisaCorrecta = numeradorMantisaIncorrecta*10
        ordenMagnitudCorrecto = ordenMagnitudIncorrecto-1
        ordenMagnitudDistractor1 = ordenMagnitudIncorrecto+1
        ordenMagnitudDistractor2 = ordenMagnitudIncorrecto-2
        ordenMagnitudDistractor3 = ordenMagnitudIncorrecto+2        
    enunciado = r"El número $" + str(numeradorMantisaIncorrecta/10000).replace('.',',') + r"\cdot{}" + r"10^{" + str(ordenMagnitudIncorrecto) + r"}$ parece estar en notación científica, pero no lo está, porque la mantisa es demasiado pequeña. La mantisa correcta es " + str(numeradorMantisaCorrecta/10000).replace('.',',') + " y el exponente correcto será:"
    respuestaCorrecta = str(ordenMagnitudCorrecto)
    distractor1 = str(ordenMagnitudDistractor1)
    distractor2 = str(ordenMagnitudDistractor2)
    distractor3 = str(ordenMagnitudDistractor3)
    return [enunciado,respuestaCorrecta,distractor1,distractor2,distractor3]

def generaEjercicioTipo3(parametros):
    # Corrección por mantisa demasiado grande
    numeroOperaciones = parametros[0]
    maximoPositivo = parametros[1]
    
    numeradorMantisaIncorrecta = random.randrange(11,9999)
    ordenMagnitudIncorrecto = random.randrange(2,19)
    dict_items=diccionarioOrdenesMagnitud.items()
    if numeradorMantisaIncorrecta < 100:
        numeradorMantisaCorrecta = numeradorMantisaIncorrecta/10
        ordenMagnitudCorrecto = ordenMagnitudIncorrecto+1
        ordenMagnitudDistractor1 = ordenMagnitudIncorrecto+2
        ordenMagnitudDistractor2 = ordenMagnitudIncorrecto-1
        ordenMagnitudDistractor3 = ordenMagnitudIncorrecto-2
    elif numeradorMantisaIncorrecta < 1000:
        numeradorMantisaCorrecta = numeradorMantisaIncorrecta/100
        ordenMagnitudCorrecto = ordenMagnitudIncorrecto+2
        ordenMagnitudDistractor1 = ordenMagnitudIncorrecto-1
        ordenMagnitudDistractor2 = ordenMagnitudIncorrecto-2
        ordenMagnitudDistractor3 = ordenMagnitudIncorrecto+1        
    elif numeradorMantisaIncorrecta < 10000:
        numeradorMantisaCorrecta = numeradorMantisaIncorrecta/1000
        ordenMagnitudCorrecto = ordenMagnitudIncorrecto+3
        ordenMagnitudDistractor1 = ordenMagnitudIncorrecto-1
        ordenMagnitudDistractor2 = ordenMagnitudIncorrecto-2
        ordenMagnitudDistractor3 = ordenMagnitudIncorrecto-3        
    enunciado = r"El número $" + str(numeradorMantisaIncorrecta).replace('.',',') + r"\cdot{}" + r"10^{" + str(ordenMagnitudIncorrecto) + r"}$ parece estar en notación científica, pero no lo está, porque la mantisa es demasiado grande. La mantisa correcta es " + str(numeradorMantisaCorrecta).replace('.',',') + " y el exponente correcto será:"
    respuestaCorrecta = str(ordenMagnitudCorrecto)
    distractor1 = str(ordenMagnitudDistractor1)
    distractor2 = str(ordenMagnitudDistractor2)
    distractor3 = str(ordenMagnitudDistractor3)
    return [enunciado,respuestaCorrecta,distractor1,distractor2,distractor3]    

numeroEjerciciosDiferentes = 3
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
    fLaTeX.write(r"    \item " + funcionesBasicas.corrigeCaracteresEspeciales(cadenas[3]) + "\n")
    fLaTeX.write(r"    \item " + funcionesBasicas.corrigeCaracteresEspeciales(cadenas[4]) + "\n")
    fLaTeX.write(r"\end{multi}"+"\n")
fLaTeX.write(r"\end{quiz}"+"\n")
fLaTeX.write(r"\end{document}"+"\n")
fLaTeX.close()
subprocess.run(["pdflatex","--interaction=batchmode","-output-directory=archivosXML", rutaArchivoLaTeX])
#######################################################################################
# FIN del código común para todas las fichas
#######################################################################################
