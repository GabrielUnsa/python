#Kmeans Vecino mas cercano
#Sistemas Inteligentes
import collections
import math
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pylab
import pandas as pd
from pathlib import Path
from random import randint, random, uniform

class punto:
    #Contructor de la clase punto
    def __init__( self, punto = None, persona = None ):
        self.punto = punto
        self.persona = persona
    
    def setPunto( punto ):
        self.punto = punto

    def getPunto( self ):
        return self.punto

    def setPersona( persona ):
        self.persona = persona
    
    def getPersona( self ):
        return self.persona
    
    # calcula de distancia euclideana entre un punto pasado por parametro y el punto perteneciente a la clase
    def distancia( self, punto ):
        distancia = 0
        calculo = punto - self.punto
        for i in range ( len( calculo ) ):
            distancia += ( calculo[i] ** 2 )
        return math.sqrt( distancia )

class knn:
    # Contructor de la clase knn contiene una lista de la clase punto
    def __init__( self, puntos = None):
        self.puntos = puntos
    
    def setPuntos( puntos ):
        self.puntos = puntos
    
    def getPuntos( self ):
        return self.puntos
    
    # Clasifica el punto segun el metodo de kmean vecino mas cercano
    def clasificador( self, nuevo_punto, corte ):
        vector_distancia_clase =[]
        for punto in self.puntos:
            vector_distancia_clase.append( ( punto.distancia( nuevo_punto ), punto.getPersona() ) )
        vector_distancia_clase = sorted( vector_distancia_clase, key = lambda distancia:distancia[0] )
        persona = []
        for i in range( corte ):
            persona.append( vector_distancia_clase[i][1] )
        return collections.Counter(persona).most_common(1)[0][0]
    
    def muestra(self):
        for pto in self.puntos:
            print(pto.getPunto())
            print(pto.getPersona())
    
    # Guarda en un txt con formato csv los elementos perteneciente a la clase
    def guardar( self, nombre ):
        f = open( nombre , 'w')
        for punto in self.puntos:
            for elemento in punto.getPunto():
                f.write(str(elemento)+',')
            f.write(str(punto.getPersona())+'\n')
        f.close()

#Calcula de frecuencia de una imagen
def frecuencia( imagen, nBins = 265 ):
    frecuencia = np.array( [0] * nBins )
    for fila in imagen:
        for pixel in fila:
            for rgb in pixel:
                if ( nBins != 265 ):
                    i = 0
                    rango = int ( 265 / nBins )
                    clase = i * rango
                    while ( True ):
                        if ( rgb > (i * rango)  and rgb <= ( (i+1) * rango) ):
                            frecuencia[i] += 1
                            break
                        i += 1
                        clase = i * rango
                else:
                    frecuencia[rgb] += 1
    return frecuencia

# Crea vector con los nombre de los archivos en una ruta dada
def ls ( ruta = Path.cwd( ) ):
    return [arch.name for arch in Path(ruta).iterdir() if arch.is_file()] 

# Crea un array de la clase punto que contiene: la frecuencia de la imagen y a quien pertenece la frecuencia
def huellas( ruta, nBins ):
    lista_huellas = sorted ( ls ( ruta ) )
    puntos = []
    for huella in lista_huellas:
        imagen = cv2.imread ( ruta + huella , cv2.IMREAD_COLOR )
        puntos.append( punto( frecuencia ( imagen , nBins ), huella[2:3] ) )
    return puntos

# Dibuja el histograma del vector dado
def histograma ( vector ):
    plt.bar( np.arange( vector.shape[0] ) ,vector)
    plt.title("Histograma Huella")
    plt.xlabel("nBins")
    plt.ylabel("Frecuencia")  
    pylab.show()

# def prueba( ruta, nBins ):
#     lista_huella = ls( ruta ) 
#     nuevo_punto = []
#     for huella in lista_huella:
#         imagen = cv2.imread ( ruta + huella , cv2.IMREAD_COLOR )
#         nuevo_punto.append( frecuencia( imagen, nBins ) )
#     return nuevo_punto

# Convierte el array resultante en una lista de la clase punto
def convertidor( datos ):
    dato = []
    for vector in datos:
        dato.append( punto( vector[ :len( vector ) - 1 ], int ( vector[len( vector ) - 1 : len( vector ) ] ) ) )
    return dato

def main():
    # Primero procece las frecuencia de las huellas y lo guarde en un txt con formato csv para ahorrar tiempo
    # basedatos = knn ( huellas( 'db/', 5 ) )
    # basedatos.guardar('db.txt')
    # Creo MatrizConfusion
    matrizconfusion = []
    for i in range( 10 ):
        matrizconfusion.append( [0] * 10 )
    basedatos = knn( convertidor( np.genfromtxt("db.txt",delimiter=',') ) )
    test = convertidor( np.genfromtxt("test.txt",delimiter=',') )
    #Cargo la matriz confusion
    for punto in test:
        matrizconfusion[punto.getPersona()-1][basedatos.clasificador(punto.getPunto(),4)-1] += 1
    #Muestro la matriz confunsion
    print("Matriz Confunsion: ")
    for fila in matrizconfusion:
        print(fila)
    # Muestro el calculo de la presicion
    print ("Presicion: " + str( float ( np.trace(np.array(matrizconfusion)) ) / 20 ))

if __name__ == '__main__':
    main()
