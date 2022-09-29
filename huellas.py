import cv2
import numpy as np
import pylab
import matplotlib.pyplot as plt
from pathlib import Path
from kmeansVecinoCercano import *

# Calcula la frecuencia de los pixeces perteneciente a una imagen
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

# Dibuja un historgrama de un vector de tamaño n dado
def histograma ( vector ):
    plt.bar( np.arange( vector.shape[0] ) ,vector)
    plt.title("Histograma Huella")
    plt.xlabel("nBins")
    plt.ylabel("Frecuencia")  
    pylab.show()

# Obtiene todas las ruta de un directorio
def ls ( ruta = Path.cwd( ) ):
    return [arch.name for arch in Path(ruta).iterdir() if arch.is_file()]

#Funcion Principal
def main():
    ruta = 'DB3_B/'
    lista_huellas = sorted ( ls ( ruta ) )
    for huella in lista_huellas:
        imagen = cv2.imread ( ruta + huella , cv2.IMREAD_COLOR )
        print ( frecuencia ( imagen , 5 ) )
    #histograma ( frecuencia( imagen ) )
    #cv2.imshow('Title',imagen)
    #cv2.waitKey(0)

if __name__ == '__main__':
    main()
    