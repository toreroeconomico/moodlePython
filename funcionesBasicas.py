#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 16:59:22 2021

@author: sergio
"""
import random
import math

#######################################################################################
def corrigeCaracteresEspeciales(cadena):
    # Moodle no acepta los acentos ni la ñ tal cual. Hay que escribirlos entre llaves.
    cadena = cadena.replace(r"á",r"\'{a}")
    cadena = cadena.replace(r"é",r"\'{e}")
    cadena = cadena.replace(r"í",r"\'{i}")
    cadena = cadena.replace(r"ó",r"\'{o}")
    cadena = cadena.replace(r"ú",r"\'{u}")
    cadena = cadena.replace(r"ñ",r"\~{n}")
    cadena = cadena.replace(r"¿",r"&iquest;")
    return cadena

#######################################################################################
def generaListaAleatoriaTiposEjercicio(numeroEjerciciosDiferentes,numeroEjercicios):
    listaAleatoriaTiposEjercicio = []
    for kupi in range(numeroEjercicios):
        listaAleatoriaTiposEjercicio += random.sample(range(1,numeroEjerciciosDiferentes+1), numeroEjerciciosDiferentes)
    return listaAleatoriaTiposEjercicio

#######################################################################################
def generaValoresDistintos(valorOriginal,numeroValoresDistintos,minimo,maximo):
    seguir = 1
    while seguir == 1:
        valoresDistintos = random.sample(range(minimo, maximo), numeroValoresDistintos)
        if valorOriginal not in valoresDistintos:
            return valoresDistintos
