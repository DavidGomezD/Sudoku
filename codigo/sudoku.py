# -*- coding: utf-8 -*-
import random

#Variables del sudoku
fila_1 = []
fila_2 = []
fila_3 = []
fila_4 = []
fila_5 = []
fila_6 = []
fila_7 = []
fila_8 = []
fila_9 = []

col_1 = []
col_2 = []

contador = 1
aleatorio = 0
buscador = False

#Funciones 

#Se usa en if_buscador_f
def buscador_f(num, arreglo):
    for elemento in arreglo:
        if elemento == num:
            return True
        
#El numero no se repite en la columna y cuadrante
def if_buscador_f(num, arreglo):
    global buscador
    if buscador_f(num, arreglo) == True:
        buscador = True 

#El numero no se repite en las filas
def if_buscador_fila(fil):
    global aleatorio, contador, buscador 
    if aleatorio == fil[contador-1]:
        buscador = True

#Ingresa datos a la fila y aumenta el contador
def ingresa(buscador, fila, aleatorio):
    global contador
    if buscador == False:
        fila.append(aleatorio)
        contador += 1

#Inicia las variables para el ciclo
def inicia_var():
    global aleatorio, buscador
    aleatorio = random.randint(1, 9)
    buscador = False 
    
def inicia_var_while():
    global ciclos, contador
    ciclos = 1
    contador = 1

def fun_fila_1():
    return fila_1

def fun_fila_2():
    return fila_2

def fun_fila_3():
    return fila_3

def fun_fila_4():
    return fila_4

def fun_fila_5():
    return fila_5

def fun_fila_6():
    return fila_6

def fun_fila_7():
    return fila_7

def fun_fila_8():
    return fila_8

def fun_fila_9():
    return fila_9

#Llena la fila 1 del sudoku
inicia_var_while()
while contador <= 9:
    inicia_var()
    if_buscador_f(aleatorio, fila_1)
    ingresa(buscador, fila_1, aleatorio)

print("fila 1:", fila_1)

#Llena la fila 2 del sudoku
col_1 = [fila_1[0], fila_1[1], fila_1[2]]
inicia_var_while()
while contador <= 9:
    inicia_var()
    #Cambia las columnas
    if contador == 4:
        col_1 = [fila_1[3], fila_1[4], fila_1[5]]
    if contador == 7:
        col_1 = [fila_1[6], fila_1[7], fila_1[8]]
        
    if_buscador_f(aleatorio, fila_2)
    if_buscador_f(aleatorio, col_1)
    ingresa(buscador, fila_2, aleatorio)
    #Reinicio :D jajaja evita el ciclo infinito
    if ciclos == 65:
        contador = 1
        ciclos = 1
        col_1 = [fila_1[0], fila_1[1], fila_1[2]]
        fila_2 = []
    #Aumenta los ciclos
    ciclos += 1

print("fila 2:", fila_2)

#Llena la fila 3 del sudoku
col_1 = [fila_1[0], fila_1[1], fila_1[2]]
col_2 = [fila_2[0], fila_2[1], fila_2[2]]
inicia_var_while()
while contador <= 9:
    inicia_var()
    #Cambia las columnas
    if contador == 4:
        col_1 = [fila_1[3], fila_1[4], fila_1[5]]
        col_2 = [fila_2[3], fila_2[4], fila_2[5]]
    if contador == 7:
        col_1 = [fila_1[6], fila_1[7], fila_1[8]]
        col_2 = [fila_2[6], fila_2[7], fila_2[8]]
    
    if_buscador_f(aleatorio, fila_3)
    if_buscador_f(aleatorio, col_1)
    if_buscador_f(aleatorio, col_2)
    
    ingresa(buscador, fila_3, aleatorio)
        
    #Reinicio :D jajaja evita el ciclo infinito
    if ciclos == 65:
        contador = 1
        ciclos = 1
        col_1 = [fila_1[0], fila_1[1], fila_1[2]]
        col_2 = [fila_2[0], fila_2[1], fila_2[2]]
        fila_3 = []    
    #Aumenta los ciclos
    ciclos += 1

print("fila 3:", fila_3)

#Llena la fila 4 del sudoku
inicia_var_while()
while contador <= 9:
    inicia_var()
    
    #El numero no se repite en las filas anteriores
    if_buscador_fila(fila_1)
    if_buscador_fila(fila_2)
    if_buscador_fila(fila_3)
    
    if_buscador_f(aleatorio, fila_4)
    ingresa(buscador, fila_4, aleatorio)
    
    #Reinicio :D jajaja evita el ciclo infinito
    if ciclos == 65:
        contador = 1
        ciclos = 1
        fila_4 = []    
    #Aumenta los ciclos
    ciclos += 1
    
print("fila 4:", fila_4)

#Llena la fila 5 del sudoku
col_1 = [fila_4[0], fila_4[1], fila_4[2]]
inicia_var_while()
while contador <= 9:
    inicia_var()
    #Cambia las columnas
    if contador == 4:
        col_1 = [fila_4[3], fila_4[4], fila_4[5]]
    if contador == 7:
        col_1 = [fila_4[6], fila_4[7], fila_4[8]]
        
    #El numero no se repite en las filas anteriores
    if_buscador_fila(fila_1)
    if_buscador_fila(fila_2)
    if_buscador_fila(fila_3)
    if_buscador_fila(fila_4)
        
    if_buscador_f(aleatorio, fila_5)
    if_buscador_f(aleatorio, col_1)
    ingresa(buscador, fila_5, aleatorio)
    #Reinicio :D jajaja evita el ciclo infinito
    if ciclos == 65:
        contador = 1
        ciclos = 1
        col_1 = [fila_4[0], fila_4[1], fila_4[2]]
        fila_5 = []
    #Aumenta los ciclos
    ciclos += 1

print("fila 5:", fila_5)

#Llena la fila 6 del sudoku
col_1 = [fila_4[0], fila_4[1], fila_4[2]]
col_2 = [fila_5[0], fila_5[1], fila_5[2]]
inicia_var_while()
while contador <= 9:
    inicia_var()
    #Cambia las columnas
    if contador == 4:
        col_1 = [fila_4[3], fila_4[4], fila_4[5]]
        col_2 = [fila_5[3], fila_5[4], fila_5[5]]
    if contador == 7:
        col_1 = [fila_4[6], fila_4[7], fila_4[8]]
        col_2 = [fila_5[6], fila_5[7], fila_5[8]]
        
    #El numero no se repite en las filas anteriores
    if_buscador_fila(fila_1)
    if_buscador_fila(fila_2)
    if_buscador_fila(fila_3)
    if_buscador_fila(fila_4)
    if_buscador_fila(fila_5)
    
    if_buscador_f(aleatorio, fila_6)
    if_buscador_f(aleatorio, col_1)
    if_buscador_f(aleatorio, col_2)
    
    ingresa(buscador, fila_6, aleatorio)
        
    #Reinicio :D jajaja evita el ciclo infinito
    if ciclos == 65:
        contador = 1
        ciclos = 1
        col_1 = [fila_4[0], fila_4[1], fila_4[2]]
        col_2 = [fila_5[0], fila_5[1], fila_5[2]]
        fila_6 = []    
    #Aumenta los ciclos
    ciclos += 1

print("fila 6:", fila_6)

#Llena la fila 7 del sudoku
inicia_var_while()
while contador <= 9:
    inicia_var()
    
    #El numero no se repite en las filas anteriores
    if_buscador_fila(fila_1)
    if_buscador_fila(fila_2)
    if_buscador_fila(fila_3)
    if_buscador_fila(fila_4)
    if_buscador_fila(fila_5)
    if_buscador_fila(fila_6)
    
    if_buscador_f(aleatorio, fila_7)
    ingresa(buscador, fila_7, aleatorio)
    
    #Reinicio :D jajaja evita el ciclo infinito
    if ciclos == 65:
        contador = 1
        ciclos = 1
        fila_7 = []    
    #Aumenta los ciclos
    ciclos += 1
    
print("fila 7:", fila_7)

#Llena la fila 5 del sudoku
col_1 = [fila_7[0], fila_7[1], fila_7[2]]
inicia_var_while()
while contador <= 9:
    inicia_var()
    #Cambia las columnas
    if contador == 4:
        col_1 = [fila_7[3], fila_7[4], fila_7[5]]
    if contador == 7:
        col_1 = [fila_7[6], fila_7[7], fila_7[8]]
        
    #El numero no se repite en las filas anteriores
    if_buscador_fila(fila_1)
    if_buscador_fila(fila_2)
    if_buscador_fila(fila_3)
    if_buscador_fila(fila_4)
    if_buscador_fila(fila_5)
    if_buscador_fila(fila_6)
    if_buscador_fila(fila_7)
        
    if_buscador_f(aleatorio, fila_8)
    if_buscador_f(aleatorio, col_1)
    ingresa(buscador, fila_8, aleatorio)
    #Reinicio :D jajaja evita el ciclo infinito
    if ciclos == 65:
        contador = 1
        ciclos = 1
        col_1 = [fila_7[0], fila_7[1], fila_7[2]]
        fila_8 = []
    #Aumenta los ciclos
    ciclos += 1

print("fila 8:", fila_8)

#Llena la fila 6 del sudoku
col_1 = [fila_7[0], fila_7[1], fila_7[2]]
col_2 = [fila_8[0], fila_8[1], fila_8[2]]
inicia_var_while()
while contador <= 9:
    inicia_var()
    #Cambia las columnas
    if contador == 4:
        col_1 = [fila_7[3], fila_7[4], fila_7[5]]
        col_2 = [fila_8[3], fila_8[4], fila_8[5]]
    if contador == 7:
        col_1 = [fila_7[6], fila_7[7], fila_7[8]]
        col_2 = [fila_8[6], fila_8[7], fila_8[8]]
        
    #El numero no se repite en las filas anteriores
    if_buscador_fila(fila_1)
    if_buscador_fila(fila_2)
    if_buscador_fila(fila_3)
    if_buscador_fila(fila_4)
    if_buscador_fila(fila_5)
    if_buscador_fila(fila_6)
    if_buscador_fila(fila_7)
    if_buscador_fila(fila_8)
    
    if_buscador_f(aleatorio, fila_9)
    if_buscador_f(aleatorio, col_1)
    if_buscador_f(aleatorio, col_2)
    
    ingresa(buscador, fila_9, aleatorio)
        
    #Reinicio :D jajaja evita el ciclo infinito
    if ciclos == 65:
        contador = 1
        ciclos = 1
        col_1 = [fila_7[0], fila_7[1], fila_7[2]]
        col_2 = [fila_8[0], fila_8[1], fila_8[2]]
        fila_9 = []    
    #Aumenta los ciclos
    ciclos += 1

print("fila 9:", fila_9)