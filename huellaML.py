# -*- coding: utf-8 -*-
"""
Created on Mon May  6 12:18:04 2019

@author: ismael
"""

import cv2
import numpy as np

winSize = (64,64)
blockSize = (16,16)
blockStride = (8,8)
cellSize = (8,8)
nbins = 25
derivAperture = 1
winSigma = 4.
histogramNormType = 0
L2HysThreshold = 2.0000000000000001e-01
gammaCorrection = 0
nlevels = 64
hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins,derivAperture,winSigma,histogramNormType,L2HysThreshold,gammaCorrection,nlevels)


X_train, y_train = list(), list()
X_test, y_test   = list(), list()
for l in range(1,11):
    for i in range(1,9):
        if ( l != 10):
            ruta = '/home/gabriel/Documentos/huellas/DB3_B/10' + str(l) + '_' + str(i) + '.tif'
        else:
            ruta = '/home/gabriel/Documentos/huellas/DB3_B/1' + str(l) + '_' + str(i) + '.tif'
        img = cv2.imread(ruta, cv2.IMREAD_COLOR)
#        img = cv2.resize(img,(128,128))
        descriptor = hog.compute(img).ravel()
        if(i < 7):
            X_train.append(descriptor)
            y_train.append(l)
        else:
            X_test.append(descriptor)
            y_test.append(l)

X_train = np.array(X_train, dtype = np.float32)
y_train = np.array(y_train, dtype = np.int32)

X_test = np.array(X_test, dtype = np.float32)
y_test = np.array(y_test, dtype = np.int32)

SVM = cv2.ml.SVM_create()
SVM.setType(cv2.ml.SVM_C_SVC)
#SVM.setKernel(cv2.ml.SVM_LINEAR) #Lineal

#SVM.setC(0.0005)
#SVM.setC(10)
#SVM.setDegree(4)

SVM.setDegree(3)
SVM.setKernel(cv2.ml.SVM_POLY) #Polinomial

'''
SVM.setC(1)
SVM.setGamma(100)
SVM.setKernel(cv2.ml.SVM_RBF) #Circunferencia
'''
'''
SVM.setC(1)
SVM.setGamma(100)
SVM.setKernel(cv2.ml.SVM_CHI2) #Chicuadrada
'''
SVM.setTermCriteria((cv2.TERM_CRITERIA_COUNT, 100, 1.e-06))
SVM.train(X_train, cv2.ml.ROW_SAMPLE, y_train)

res, y_predict = SVM.predict(X_test)

matriz = []
for i in range( 10 ):
	matriz.append( [0] * 10 )
i = 0
j = 0
for y in y_predict:
	matriz[i][int(y)-1] += 1
	j += 1
	if ( j == 2):
		j = 0
		i += 1
view = np.array(matriz)
print ( view )
print ("Presicion: " + str ( float(np.trace(view) / 20 ) ))
