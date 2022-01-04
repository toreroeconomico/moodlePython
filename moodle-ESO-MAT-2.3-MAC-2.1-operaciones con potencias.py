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
nombreCategoria = "ESO-MAT-2.3-MAC-2.1-operaciones con potencias"
numeroOperaciones = 1 # No hace falta que cada solución tenga más de una posibilidad, como sucede en criptografía.
# Esto no es muy eficiente, pero tiene la ventaja de que podemos reutilizar el código creado
# para las fichas de criptografía, en el que sí es necesario que haya más de una posibilidad para cada solución.
maximoPositivo = int(input("Introduce el máximo positivo: "))
minimoNegativo = -maximoPositivo
exponenteSolucion = random.randrange(-13,14)
parametros = [exponenteSolucion, numeroOperaciones, maximoPositivo, minimoNegativo]
numeroEjercicios = int(input("Introduce el número de ejercicios de cada tipo: "))

#######################################################################################
# INICIO del código específico para esta ficha
#######################################################################################
def generaEjercicioTipo1(parametros):
    # (base^exp1·base^exp2)/(base^exp3·base^exp4) OK
    exponenteSolucion = parametros[0]
    numeroOperaciones = parametros[1]
    maximoPositivo = parametros[2]
    minimoNegativo = parametros[3]
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        base = random.randrange(round(maximoPositivo/2), maximoPositivo)
        exp1 = random.randrange(minimoNegativo, maximoPositivo)
        exp2 = random.randrange(minimoNegativo, maximoPositivo)
        exp3 = random.randrange(minimoNegativo, maximoPositivo)
        exp4 = random.randrange(minimoNegativo, maximoPositivo)
        if (exp1+exp2-exp3-exp4) == exponenteSolucion:
            textoOperacion = r"$\dfrac{" + str(base) + r"^{" + str(exp1) + r"}\cdot{}" + str(base) + r"^{" + str(exp2) + r"}" + r"}{" +  str(base) + r"^{" + str(exp3) + r"}\cdot{}" + str(base) + r"^{" + str(exp4) + r"}" + r"}$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    return listaOperacionesUnicas[random.randrange(0,numeroOperaciones)],str(base),str(exponenteSolucion)
    
def generaEjercicioTipo2(parametros):
    # base1 = factor1·factor2
    # base2 = factor3·factor4
    # (base1^exp1·factor3^exp1·factor4^exp1)/(factor1^exp2·base2^exp2·factor2^exp2) OK
    exponenteSolucion = parametros[0]
    numeroOperaciones = parametros[1]
    maximoPositivo = parametros[2]
    minimoNegativo = parametros[3]
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        factor1 = random.randrange(2,10)
        factor2 = random.randrange(2,10)
        factor3 = random.randrange(2,10)
        factor4 = random.randrange(2,10)
        base1 = factor1*factor2
        base2 = factor3*factor4
        exp1 = random.randrange(minimoNegativo, maximoPositivo)
        exp2 = random.randrange(minimoNegativo, maximoPositivo)
        if (exp1-exp2) == exponenteSolucion:
            textoOperacion = r"$\dfrac{" + str(base1) + r"^{" + str(exp1) + r"}\cdot{}" + str(factor3) + r"^{" + str(exp1) + r"}\cdot{}" + str(factor4) + r"^{" + str(exp1) + r"}" + r"}{" +  str(factor1) + r"^{" + str(exp2) + r"}\cdot{}" + str(base2) + r"^{" + str(exp2) + r"}\cdot{}" + str(factor2) + r"^{" + str(exp2) + r"}" + r"}$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    base = base1*factor3*factor4
    return listaOperacionesUnicas[random.randrange(0,numeroOperaciones)],str(base),str(exponenteSolucion)
    
def generaEjercicioTipo3(parametros):
    # (factor1^exp0)^exp1·factor1^exp2)/(factor1^exp3):factor1^exp4 OK
    exponenteSolucion = parametros[0]
    numeroOperaciones = parametros[1]
    maximoPositivo = parametros[2]
    minimoNegativo = parametros[3]
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        factor1 = random.randrange(2,10)
        exp0 = random.randrange(2,4)
        exp1 = random.randrange(minimoNegativo, maximoPositivo)
        exp2 = random.randrange(minimoNegativo, maximoPositivo)
        exp3 = random.randrange(minimoNegativo, maximoPositivo)
        exp4 = random.randrange(minimoNegativo, maximoPositivo)
        base1 = factor1**exp0        
        if (exp0*exp1+exp2-exp3-exp4) == exponenteSolucion:
            textoOperacion = r"$\dfrac{" + str(base1) + r"^{" + str(exp1) + r"}\cdot{}" + str(factor1) + r"^{" + str(exp2) + r"}}{" +  str(factor1) + r"^{" + str(exp3) + r"}}:" + str(factor1) + r"^{" + str(exp4) + r"}$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    base = factor1
    return listaOperacionesUnicas[random.randrange(0,numeroOperaciones)],str(base),str(exponenteSolucion)
    
def generaEjercicioTipo4(parametros):
    # (factor1^3^exp1^exp2)/(factor1^2^exp2^exp3)·factor1^exp1 OK
    exponenteSolucion = parametros[0]
    numeroOperaciones = parametros[1]
    maximoPositivo = parametros[2]
    minimoNegativo = parametros[3]    
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        factor1 = random.randrange(2,10)
        exp1 = random.randrange(minimoNegativo, maximoPositivo)
        exp2 = random.randrange(minimoNegativo, maximoPositivo)
        exp3 = random.randrange(minimoNegativo, maximoPositivo)
        exp4 = random.randrange(minimoNegativo, maximoPositivo)        
        if (3*exp1*exp2-2*exp2*exp3+exp4) == exponenteSolucion:
            textoOperacion = r"$\dfrac{(" + str(factor1**3) + r"^{" + str(exp1) + r"})^{" + str(exp2) + r"}}{(" + str(factor1**2) + r"^{" + str(exp2) + r"})^{" + str(exp3) + "}}\cdot{}" + str(factor1) + r"^{" + str(exp4) + r"}$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    base = factor1
    return listaOperacionesUnicas[random.randrange(0,numeroOperaciones)],str(base),str(exponenteSolucion)
    
def generaEjercicioTipo5(parametros):
    # ((factor1^2)^exp1·(factor1^3)^exp2)/((factor1^2)^exp3·factor1^exp4) OK
    exponenteSolucion = parametros[0]
    numeroOperaciones = parametros[1]
    maximoPositivo = parametros[2]
    minimoNegativo = parametros[3]    
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        factor1 = random.randrange(2,10)
        exp1 = random.randrange(minimoNegativo, maximoPositivo)
        exp2 = random.randrange(minimoNegativo, maximoPositivo)
        exp3 = random.randrange(minimoNegativo, maximoPositivo)
        exp4 = random.randrange(minimoNegativo, maximoPositivo)        
        if (2*exp1+3*exp2-2*exp3-exp4) == exponenteSolucion:
            textoOperacion = r"$\dfrac{" + str(factor1**2) + r"^{" + str(exp1) + r"}\cdot{}" + str(factor1**3) + r"^{" + str(exp2) + r"}}{" + str(factor1**2) + r"^{" + str(exp3) + r"}\cdot{}" + str(factor1) + r"^{" + str(exp4) + r"}}$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    base = factor1
    return listaOperacionesUnicas[random.randrange(0,numeroOperaciones)],str(base),str(exponenteSolucion)

def generaEjercicioTipo6(parametros):
    # (factor1/factor2)^exp1·(factor1^3/factor2)^exp2)·(factor2/factor1^2)^-exp3
    exponenteSolucion = parametros[0]
    numeroOperaciones = parametros[1]
    maximoPositivo = parametros[2]
    minimoNegativo = parametros[3]    
    contador = 0
    listaOperaciones = []
    while contador < numeroOperaciones:
        factor1 = random.randrange(2,10)
        #factor2 = random.randrange(2,10)
        posibilidadesFactor2 = [2*factor1-1,2*factor1+1,2*factor1+3] # Primos con factor1
        factor2 = posibilidadesFactor2[random.randrange(0,len(posibilidadesFactor2))]
        exp1 = random.randrange(minimoNegativo, maximoPositivo)
        exp2 = random.randrange(minimoNegativo, maximoPositivo)
        exp3 = random.randrange(2, maximoPositivo)
        if (exp1+3*exp2+2*exp3) == (2*exp1+2*exp2+exp3) and (exp1+3*exp2+2*exp3) == exponenteSolucion:
            textoOperacion = r"$\Big(\dfrac{" + str(factor1) + r"}{" + str(factor2**2) + r"}\Big)^{" + str(exp1) + r"}\cdot{}\Big(\dfrac{" + str(factor1**3) + r"}{" + str(factor2**2) + r"}\Big)^{" + str(exp2) + r"}\cdot{}" + r"\Big(\dfrac{" + str(factor2) + r"}{" + str(factor1**2) + r"}\Big)^{" + str(-exp3) + r"}$"
            listaOperaciones.append(textoOperacion)
            listaOperacionesUnicas = np.unique(listaOperaciones)
            contador = len(listaOperacionesUnicas)
    base = factor1/factor2
    return listaOperacionesUnicas[random.randrange(0,numeroOperaciones)],str(base),str(exponenteSolucion)

numeroEjerciciosDiferentes = 6
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
    fLaTeX.write(r"\begin{cloze}{" + nombreCategoria  + r"}" + "\n")
    fLaTeX.write(funcionesBasicas.corrigeCaracteresEspeciales(r"Reduce la siguiente expresión a una única potencia e indica su base y su exponente:") + "\n")
    fLaTeX.write(r"" + "\n")    
    fLaTeX.write(r"" + funcionesBasicas.corrigeCaracteresEspeciales(cadenas[0]) + "\n")
    fLaTeX.write(r"" + "\n")
    fLaTeX.write(r"    \begin{numerical}" + "\n")
    fLaTeX.write(r"        Base: \item[tolerance={0}] " + funcionesBasicas.corrigeCaracteresEspeciales(cadenas[1]) + "\n")
    fLaTeX.write(r"    \end{numerical}"+"\n")    
    fLaTeX.write(r"    \begin{numerical}" + "\n")    
    fLaTeX.write(r"        Exponente: \item[tolerance={0}] " + funcionesBasicas.corrigeCaracteresEspeciales(cadenas[2]) + "\n")
    fLaTeX.write(r"    \end{numerical}"+"\n")
    fLaTeX.write(r"\end{cloze}" + "\n")
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
