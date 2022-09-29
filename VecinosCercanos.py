#knn vecinos cercanos 

import cv2
import numpy as np
from pathlib import Path
import math
import collections

def distancia( punto1, punto2 ):
    dis = 0
    for i in range( len( punto1 ) ):
        dis += ( ( punto1[i] - punto2[i] ) ** 2 )
        #print(i )
    return math.sqrt( dis )
#Calculo de frecuencia de una imagen
def frecuencia( imagen, nBins =  256 ):
    freq =  [0] *nBins 
    f =  [0] * 256 
    imagen = imagen.ravel()
    dim = len (imagen)
    for fila in range ( dim ):
        val = imagen[fila]
        f[val]+= 1
    if ( nBins != 256 ):
        rango = int( 256 / nBins )
        for i in range ( 0, nBins ):
            freq[i] = sum( f[ ( i*rango ) : ( (i+1)*rango )] )
        if ( rango * nBins< 256):
            freq[ (nBins-1) ] += sum ( f[ ((nBins)*rango) : 256] )
        return freq
    else: return f

# Crea vector con los nombre de los archivos en una ruta dada
def ls ( ruta = Path.cwd( ) ):
    return [arch.name for arch in Path(ruta).iterdir() if arch.is_file()]

def huellas( ruta, nBins ):
    lista_huellas = sorted ( ls ( ruta ) )
    puntos = []
    for huella in lista_huellas:
        #imagen = cv2.imread ( ruta + huella , cv2.IMREAD_GRAYSCALE)
        imagen = cv2.imread ( ruta + huella , cv2.IMREAD_COLOR)
        #img = segmentar_imagen(imagen) #define en 4 las imagenes
        #img = segmentar_imagen( imagen )
        #freq = []
        #for seg in img:
         #   freq.extend( frecuencia( seg, nBins ) )
        #print (freq)
        freq = frecuencia( imagen, nBins )
        freq.append( int( huella[2:3] ) ) #se agrega la persona
        puntos.append(  freq )
    return puntos

def segmentar_imagen( imagen ):
    izq_sup = imagen[0:239,0:224]
    der_sup = imagen[0:239,224:448]
    izq_inf = imagen[239:478,0:224]
    der_inf = imagen[239:478,224:448]
    return [izq_sup,der_sup,izq_inf,izq_sup]

#En esta version la imagen se divide en 4
def huellasDividida( ruta, nBins ):
    lista_huellas = sorted ( ls ( ruta ) )
    puntos = []
    for huella in lista_huellas:
        #imagen = cv2.imread ( ruta + huella , cv2.IMREAD_GRAYSCALE)
        imagen = cv2.imread ( ruta + huella , cv2.IMREAD_COLOR)
        img = segmentar_imagen(imagen) #define en 4 las imagenes
        freq = []
        for seg in img:
            freq.extend( frecuencia( seg, nBins ) )
        #print (freq)
        freq.append( int( huella[2:3] ) ) #se agrega la persona
        puntos.append(  freq )
    return puntos

#permite guardar los puntos en formato txt
def guardar( puntos , nombre ):
    f = open( nombre , 'w')
    for punto in puntos:
        for i in range( len( punto ) -1 ):
            f.write(str( punto[i] )+',') 
        f.write(str( punto[len(punto)-1] )+'\n')
    f.close()

#retorna un array de los puntos
def abrir ( nombre ):
    dataset = np.genfromtxt( nombre, delimiter="," )
    puntos = []
    for vector in dataset:
        p = []
        for punto in vector:
            p.append( punto )
        puntos.append( p )
    return puntos

def clasifica( dataset, nuevo_punto , k ):
    distancias = []
    for punto in dataset:
        u = len( punto ) - 1
        distancias.append( ( distancia( punto[0:u], nuevo_punto[0:u] ) , punto[u] ) )
    distancias = sorted ( distancias, key = lambda distancia:distancia[0] )
    persona = []
    for i in range ( k ):
        persona.append( distancias[i][1] )
    return collections.Counter( persona ).most_common(1)[0][0]

def main():
##    nom = "doc62.txt"
##    ruta = 'trainning\\'
##    dataset = huellasDividida( ruta, 62 )
##    guardar( dataset, nom )
##    nom = "doc62t.txt"
##    ruta = 'test - copia\\'

##    guardar( test, nom )
##    dataset = abrir ( "doc62.txt" )
##    test = abrir ( "doc62t.txt" )

    res = []
    for nBins in range( 200 ,201 ):
        ruta = 'trainning\\'
        dataset = huellasDividida( ruta, nBins )
        ruta = 'test - copia\\'
        test = huellasDividida( ruta, nBins ) #ruta + nBins
        #Creando matriz de confusion
        confusion = []
        for i in range( 10 ):
            confusion.append( [0] * 10 )
        for punto in test:
            k = 3
            alg = int ( clasifica( dataset, punto, 3 ) )
            real = int (punto[len(punto) - 1] )
            confusion[alg][real] += 1 #alf fila real columna
        for fila in confusion:
            print(fila)
    #print ("Presicion: " + str( float ( np.trace(np.array(matrizconfusion)) ) / 20 ))
        precision =  float ( np.trace(np.array(confusion) ) ) / 20 
        print ("Precision: " + str( precision) )
        res.append( (nBins, confusion, precision  ) )

    guardar( res, "pruebas2.txt")
    print (res )
    
##    print( np.array( dataset, dtype = np.int32 ) )

if __name__ == '__main__':
    main()
##    ruta = "101_7.tif"
##    imagen = cv2.imread ( ruta, cv2.IMREAD_COLOR)
##    seg = segmentar_imagen(imagen)
##    suma = 0
##    for i in seg:
##        freq = frecuencia( i )
##        suma += sum( freq )
##    print( "Seg freq "+ str( suma ) )
##    frecue = frecuencia ( imagen )
##    print (sum(frecue))
    
