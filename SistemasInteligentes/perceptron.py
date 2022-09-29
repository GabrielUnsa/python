import numpy as np
import math
import random

def XOR( i, j ):
    return ( int ( i != j ) )
    
def creaMatrizDatos( ):
    matriz = []
    for xi in [ 0, 1 ]:
        for xj in [ 0, 1]:
            matriz.append( [ xi, xj, -1, xi and xj, xi or xj, XOR( xi, xj ) ] )
    return np.array( matriz )

def creaPesos( n ):
    w = []
    for i in range( n ):
        w.append( random.random() )
    return np.array( w )

def modificaPesos( x, w, y, z ):
    i = 0
    while True:
        oldw = w[i]
        delta = 0.001 * ( z - y ) * x[i]
        w[i] += delta
        if ( math.fabs( oldw - w[i] ) < 0.01 ):
            i += 1
        if ( i >= len(x) ):
            break
    return w

def funcionPredictora( x, w ):
    return ( 1 if ( np.sum( x * w ) > 0 ) else 0 )

def perceptron( matrizDatos ):
    w = creaPesos( 3 )
    for punto in matrizDatos:
        x = punto[:3]
        y = funcionPredictora( x, w )
        z = punto[3:4]
        while ( math.fabs( y - z ) > 0.01 ):
            w = modificaPesos( x, w, y, z)
            y = funcionPredictora( x, w )
    return w

def main():
    matrizDatos = creaMatrizDatos()
    w = perceptron( matrizDatos )
    for datos in matrizDatos:
        x = datos[:3]
        print( funcionPredictora( x, w ) )
    Xor = [ 
            [ 1, 0, -1, 0], 
            [ 1, 1, -1, 1],
            [ 1, 1, -1, 1],
            [ 1, 0, -1, 0]
        ]
    w = perceptron( np.array( Xor ) )
    for datos in Xor:
        x = datos[:3]
        print( funcionPredictora( x, w ) )

if __name__ == '__main__':
    main()
    