
# chair: Introduccion a Sistemas Inteligentes


import numpy as np
import math

#Datos
X = []
y = []
for line in np.genfromtxt( "data.txt", delimiter=',' ):
    X.append( line[:4] )
    y.append( line[4:5] )
X = np.array( X, dtype= float )
y = np.array( y, dtype=float ) 

#Normalizacion de los datos
''' X = X / np.amax( X, axis = 0 )
y = y / 100 '''

class Neural_Network( object ):
    def __init__( self ):
        self.inputSize = 4
        self.hiddenSize = 12
        self.outputSize = 1
        self.W1 = np.random.randn( self.inputSize, self.hiddenSize )
        self.W2 = np.random.randn( self.hiddenSize, self.outputSize )

    def sigmoid( self, s ):
        return 1 / ( 1 + np.exp( -s ) )

    def forward( self, X ):
        self.z = np.dot( X, self.W1 )
        self.z2 = self.sigmoid( self.z )
        self.z3 = np.dot( self.z2, self.W2 )
        o = self.sigmoid( self.z3 )
        return o
    
    def sigmoidPrime( self, s ):
        return s * ( 1 - s )
    
    def backward( self, X, y, o ):
        self.o_error = y - o
        self.o_delta = self.o_error * self.sigmoidPrime( o )
        self.z2_error = self.o_delta.dot( self.W2.T )
        self.z2_delta = self.z2_error * self.sigmoidPrime( self.z2 )
        self.W1 += X.T.dot( self.z2_delta )
        self.W2 += self.z2.T.dot( self.o_delta )
    
    def train( self, X, y ):
        o = self.forward( X )
        self.backward( X, y, o )
    
def main():
    NN = Neural_Network()
    for _ in range(1000000):
        NN.train( X, y )
    print( "Salida: " + str( y ) )
    print( "Prediccion: " + str( NN.forward( X ) ) )
    print( "Perdida: " + str( np.mean( np.square( y - NN.forward( X ) ) ) ) )

if __name__ == '__main__':
    main()
    