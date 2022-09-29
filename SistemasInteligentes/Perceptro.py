import numpy as np
import math as mt
import random as rn
import pandas as pd
import matplotlib.pyplot as mpl

x1 = np.array([0,1])
x2 = np.array([0,1])
x3 = -1
And = []
Or = []
Xor = []

def xor( a, b):
    return int(a != b)

def AndOrXor():
    for i in x1:
        for j in x2:
            And.append( i and j )
            Or.append( i or j )
            Xor.append( xor(i,j) )
    np.array(And)
    np.array(Or)
    np.array(Xor)

def creapesos( n ):
    w = []
    for i in range( n ):
        w.append( rn.random() )
    return np.array(w)
    
def ponderacion( w, x ):
    sum = 0
    for i in ( w * x ):
        sum += i
    return sum

def funcion( x ):
    if ( x < 0):
        return 0
    else:
        return 1


def mejoraPesos( w, x, y, z ):
    i = 0 
    while ( True ):
        oldw = w[i]
        delta = 0.001 * ( z - y ) * x[i]
        w[i] += delta
        if( mt.fabs( oldw - w[i]) < 0.01 ):
            i += 1
        if ( i >= len(x) ):
            break
    return w

def perceptron( x, z ):
    iteracion  = 0
    w = creapesos(3)
    y = funcion( ponderacion( w, x ) )
    i = 0
    while ( mt.fabs( z - y) > 0.001 ):
        w = mejoraPesos(w,x,y,z)
        y = funcion( ponderacion( w, x ) ) 
    return y

def resultadosPerceptron():
    k = 0
    resultados =  []
    for i in x1:
        for j in x2:
            x = [ i, j, x3 ]
            AndPerceptron = perceptron( x , And[ k ] )
            OrPerceptron = perceptron( x , Or[ k ] )
            XorPerceptron = perceptron( x , Xor[ k ] )
            fila = x
            fila.append( And[k] )
            fila.append( AndPerceptron )
            fila.append( Or[k] )
            fila.append( OrPerceptron )
            fila.append( Xor[k] )
            fila.append( XorPerceptron )
            resultados.append ( fila )
            k += 1
    return resultados

def main():
    AndOrXor()
    df = pd.DataFrame( resultadosPerceptron(), columns = ['x1','x2','x3','AND','PAND','OR','POR','XOR','PXOR'])
    print (df)

if __name__ == '__main__':
    main()
    
