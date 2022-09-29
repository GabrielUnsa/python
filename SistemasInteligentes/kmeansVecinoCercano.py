# Kmeans Vecinos Cercanos
# Sistemas Inteligentes

import math
import numpy as np
import collections
from random import uniform,random,randint

class puntos:

# Constructor de la clase
    def __init__ ( self, punto = None, clase = None ):
        self.punto = punto
        self.clase = clase

    def getPunto( self ):
        return self.punto

    def getClase ( self ):
        return self.clase

    def distancia (self, nuevo_punto):
        eucld = 0
        dis = nuevo_punto - self.punto
        for i in range( len ( dis ) ):
            eucld += ( dis[i] ** 2 )
        return math.sqrt( eucld )

# Creacion de Puntos
def creaPuntos( cantPuntos, cant ):
    lista = []
    for i in range( cantPuntos ):
        pnt = []
        for j in range( cant ):
            pnt.append(uniform(0,1))
        pnt = np.array(pnt)
        lista.append( puntos ( pnt, randint(1,6)) )
    return lista

def distance ( puntos, newpunto ):
    dst = []
    for pto in puntos:
        dst.append( ( pto.distancia( newpunto ), pto.getClase() ) )
    return dst

def creaNewPuntos( cantPuntos, cant ):
    lista = []
    for i in range( cantPuntos ):
        pnt = []
        for j in range( cant ):
            pnt.append(uniform(0,1))
        lista.append( np.array(pnt) )
    return lista

def muestra( Puntos ):
    for i in Puntos:
        print ( "El Punto: " + str( i.getPunto() ) + " pertenece a la clase: " + str( i.getClase() ) )
        
def main ():
    k = 7
    pts = creaPuntos( 10, 2 )
    muestra( pts )
    newPuntos = creaNewPuntos( 10 , 2 )
    print ( "Los nuevos puntos son: " )
    for i in newPuntos:
        print ("\t\t      " + str( i ) )
    for newPunto in newPuntos:
        vecino_cercano = distance( pts, newPunto )
        vecino_cercano = sorted( vecino_cercano, key = lambda distancia:distancia[0] )
        clases = []
        for i in range(k):
            clases.append( vecino_cercano[i][1])
        counter = collections.Counter(clases)
        pts.append( puntos ( newPunto, counter.most_common(1)[0][0] ) )
        print ( " El punto: " + str( newPunto ) + " se asigno a la clase: " + str( counter.most_common(1)[0][0] ) )

if __name__ == '__main__':
    main()
