#Kmeans Sistemas Inteligentes

import math
import numpy as np
from random import uniform,random

# Clase puntos
# Esta clase contiene los puntos cordenadas de ingresados y su correspondiente centroide

class puntos:

# Constructor de la clase
    def __init__ ( self, punto = None, centroide = None ):
        self.punto = punto
        self.centroide = centroide

# Clasifica a que centroide pertenece el punto
    def clasificador( self, centroides ):
        disMin = 10000000  # Distancia Minima
        self.centroide = centroides[0]
        for cntroide in centroides:
            eucld = 0 # Valor de la suma Euclidiana (x-y)^2
            for i in range( len (cntroide) ):
                eucld += ( ( self.punto[i] - cntroide[i] ) ** 2 )
            disEucld = math.sqrt( eucld ) # Valor de la raiz de la suma Euclidiana ( contiene el valor de la norma Euclidiana)
            if disEucld < disMin:
                disMin = disEucld
                self.centroide = cntroide # Asigno el Centroide mas Cercano

# Muestra Punto con su Centroides
    def Muestra( self ):
        print ("Punto: " + str( self.punto ) )
        print ("Centroide: " + str( self.centroide ) )

# Devuelve el punto
    def getPunto( self ):
        return self.punto

# Devuelve el centroide
    def getCentroide( self ):
        return self.centroide

# Guarda el punto ingresado
    def setPunto( self, punto ):
        self.punto = punto

# Guarda el centroide ingresado
    def setCentroide( self, centroide ):
        self.centroide = centroide

# Compara el centroide del punto con el centroido dado, si estos son iguales
# entonces devuelve true.
def comparar_elementos( cenPunto, centroide ):
    return cenPunto == centroide

# Refinamiento de los centroides
def refinamiento ( pts , centroides ):
    newCentroide = [] # Nuevo centroide
    newCentroides = [] # Lista de los nuevos centroides
    for cntroide in centroides:
        cant = 0 # Contador de Cantidad de Puntos que pertenece a un centroide
        newCentroide = [0] * len(cntroide) # Inicia el nuevo centroide en 0
        for punto in pts:
            if ( comparar_elementos ( punto.getCentroide(), cntroide ) ):
                cant += 1
                for i in range( len(cntroide) ):
                    newCentroide[i] += punto.getPunto()[i] # Suma de todos los puntos perteneciente al centroide
        if (cant != 0) :
            for i in range( len(cntroide) ):
                newCentroide[i] /= cant # Promedio de los puntos perteneciente al centroide
            newCentroides.append(newCentroide)
        else:
            newCentroides.append(cntroide)
    return newCentroides

# Crea n cantidad de centroides
def creaCentroides( cantCentoides, cantPuntCentroide ):
    centroides = []
    for i in range( cantCentoides ):
        puntCentroides = []
        for j in range( cantPuntCentroide ):
            puntCentroides.append(uniform(0,1))
        centroides.append(puntCentroides)
    return centroides

# Creacion de Puntos
def creaPuntos( cantPuntos, cant ):
    lista = []
    for i in range( cantPuntos ):
        pnt = []
        for j in range( cant ):
            pnt.append(uniform(0,1))
        lista.append( puntos ( pnt ) )
    return lista

# Asigna el centroide mas cercano a cada punto
def clasificaPuntos( puntos , centroides ):
    for punto in puntos:
        punto.clasificador( centroides )

# Verifica que todos los centroides esten menor al error
def cantCentroideMenorEroor( centroides, newCentroides, Error, longitud):
    flag = 0
    for i in range(len(centroides)):
        count = 0
        for j in range(longitud):
            if ( Error > abs( newCentroides[i][j] - centroides[i][j] ) ):
                count += 1
        if ( count == longitud ):
            flag += 1
    return ( flag == len(centroides) )

# Muestra los centroides y los puntos con el centroide correspondiente
def muestra( puntos , centroides):
    for c in centroides:
        print ("Centroide: " + str( c ) )
    for p in puntos:
        p.Muestra()

def main():
    Error = 0.00000001
    centroides = creaCentroides( 4, 3 )
    pts = creaPuntos( 4000,  3)
    clasificaPuntos( pts, centroides )
    newCentroides = refinamiento (pts , centroides )
    while not cantCentroideMenorEroor( centroides, newCentroides , Error, 3):
        clasificaPuntos( pts, newCentroides )
        centroides = newCentroides
        newCentroides = refinamiento (pts , centroides )
    muestra( pts , centroides )

if __name__ == '__main__':
    main()
