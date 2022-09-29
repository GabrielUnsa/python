#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 13:19:29 2019

@author: gabriel-lidia
@chair: sistemas inteligentes
@college: universidad nacional de Salta

"""
# Importaciones
import math
import gc
from random import uniform,random, randint
import numpy as np
import collections

# Creamos el nodo que contendra la informacion de los puntos ingresados
class node:

    # Constructor del nodo donde estara el punto manejado como vector
    def __init__ ( self, data = None, next = None, type = None ):
        self.data = data
        self.next = next
        self.type = type

    def get_type( self ):
        return self.type

    def set_type( self, type ):
        self.type = type

    # Retorna el punto
    def get_data ( self ):
        return self.data

    # Retorna el siguiente nodo
    def get_next ( self ):
        return self.next

    # Carga el punto pasado por parametro
    def set_data ( self, data ):
        self.data = data

    # Carga el siguiente nodo
    def set_next ( self, next ):
        self.next = next

# Lista Enlazada de Puntos
class linked_list:

    # Constructor de la lista.
    def __init__ ( self ):
        self.head = None

    # Añade frontalmente un punto
    def add_at_front ( self, data ):
        self.head = node( data = data, next = self.head )

    # Retorna True o False dependiendo del estado de la cabeza del nodo
    def is_empty ( self ):
        return self.head == None

    # Añade un punto al final de la lista
    def add_at_end ( self, data, type ):
        if not ( self.head ):
            self.head = node ( data = data, type = type )
            return
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = node ( data = data, type = type )

    # Elimina un punto especifico
    def delete_node ( self, key ):
        curr = self.head
        prev = None
        fg = True
        i = 0
        for i in range ( len ( key ) ):
            if ( curr.data[i] == key[i] ):
                i += 1
        if ( i == len ( key ) ):
            fg = False
        while curr and fg:
            prev = curr
            curr = curr.next
            i = 0
            for i in range ( len ( key ) ):
                if ( curr.data[i] == key[i] ):
                    i += 1
            if ( i == len ( key ) ):
                fg = False
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    # Devuelve el ultimo nodo
    def get_last_node ( self ):
        temp = self.head
        while( temp.next is not None ):
            temp = temp.next
        return temp.data

    # Devuelve el promedio de la suma de todos los puntos
    def avg_points ( self ):
        tmp = self.head
        sum_point = [0] * len ( tmp.data )
        cant = 0
        while tmp != None:
            for i in range( len ( tmp.data ) ):
                sum_point[i] += tmp.data[i]
            tmp = tmp.next
            cant += 1
        for i in range( len (sum_point) ):
            sum_point[i] /= cant
        return sum_point

    # Retorna la cabeza de la lista
    def getHead( self ):
        return self.head

    # Muestra la lista enlazada
    def print_list ( self ):
        node = self.head
        while node != None:
            print (node.data)
            print (node.type)
            node = node.next
    
    #Devuelve la cantidad de puntos que en la lista
    def counter_point( self ):
        count = 0
        node = self.head
        while node != None:
            count += 1
            node = node.next
        return count

# Centroide

class nodeCentroid:

    # Constructor estructura donde esta los puntos centroides y sus puntos
    def __init__ ( self, centroid = None, next = None, first = None, oldcenotrid = None ):
        self.oldcentroid = None
        self.centroid = centroid
        self.next = next
        self.first = first
        self.typeCentroid = None

    def getCentroid( self ):
        return self.centroid

    def getNext( self ):
        return self.next

    def getFirst( self ):
        return self.first

    def getType( self ):
        return self.typeCentroid

    def setType( self, typeCentroid ):
        self.typeCentroid = typeCentroid

# Lista de Centroides
class linked_Centroid:

    # Constructor de la lista de centroides
    def __init__ ( self ):
        self.headCentroid = None

    # Retorna la cabeza de la lista
    def getHead( self ):
        return self.headCentroid

    # Retorna True o False dependiendo si la lista de centroides esta vacia
    def is_empty_centroid ( self ):
        return self.headCentroid == None

    # Devuelve si el primer centroide tiene puntos asignados
    def is_empty_first ( self ):
        return self.first == None

    # Añade un centroide al final de la lista
    def add_end_centroid ( self, data ):
        if not ( self.headCentroid ):
            self.headCentroid = nodeCentroid ( centroid = data )
            return
        tmp = self.headCentroid
        while tmp.next:
            tmp = tmp.next
        tmp.next = nodeCentroid ( centroid = data )

    # Devuelve el ultimo centroide
    def get_last_node_Centroid ( self ):
        temp = self.headCentroid
        while( temp.next is not None ):
            temp = temp.next
        return temp.centroid

    # Añade un punto al centroide asignado
    def add_point ( self, point, place, type ):
        tmp = self.headCentroid
        for i in range( place ):
            tmp = tmp.next
        if not ( tmp.first ):
            tmp.first = linked_list()
            tmp.first.add_at_end( point, type )
            return
        tmp.first.add_at_end( point, type )

    # Muestra la lista de centroides
    def print_list( self, show = True ):
        node = self.headCentroid
        while node != None:
            print ( " Centroide: " + str( node.centroid ) + " Clase: " + str( node.typeCentroid ) )
            list_point = node.first
            if not ( list_point ):
                print ( " No tiene puntos asignados este centroide " )
            elif( show ) :
                print ( " Los puntos asignados son: " )
                list_point.print_list()
            elif( not ( show ) ):
                print ( "Cantidad de Puntos asignados: " + str ( list_point.counter_point() ) )
            node = node.next
            print ("*********************************************")

    # Encuentra el centroide con minimo de distancia
    def min_distance ( self, point ):
        Min = 100000
        place = 0
        tmp = self.headCentroid
        while tmp != None:
            eucld = 0
            for i in range( len ( point ) ):
                eucld += ( ( point[i] - tmp.centroid[i] ) ** 2 )
            eucld = math.sqrt( eucld )
            if ( Min > eucld ):
                Min = eucld
                find = place
            tmp = tmp.next
            place += 1
        return find

    # Refina el valor de los centroides
    def refinament_centroids ( self ):
        tmp = self.headCentroid
        while tmp != None:
            if ( tmp.first ):
                tmp.oldcentroid = tmp.centroid
                tmp.centroid = tmp.first.avg_points()
            tmp = tmp.next

    # Cumple con el error
    def error ( self, error ):
        tmp = self.headCentroid
        keep = True
        lgt = tmp.centroid
        while ( tmp != None ) and keep:
            i = 0
            while ( i < len( lgt ) ) and keep:
                if ( error < abs( tmp.centroid[i] - tmp.oldcentroid[i] ) ):
                    keep = False
                i += 1
            tmp = tmp.next
        return keep

    def centroid_point_one( self ):
        tmp = self.headCentroid
        flag = True
        while tmp != None and flag :
            if ( tmp.first == None ) :
                flag = False
            tmp = tmp.next
        return flag

    def classification( self ):
        node = self.headCentroid
        while node != None:
            type = []
            list_point = node.first.getHead()
            while list_point != None:
                type.append( int( list_point.get_type() ) )
                list_point = list_point.get_next()
            counter = collections.Counter(type)
            node.typeCentroid = ( counter.most_common()[0][0] )
            node = node.next

    def get_classcentroids( self, post ):
        tmp = self.headCentroid
        for i in range( post ):
            tmp = tmp.next
        return tmp.typeCentroid

def generate_centroids ( quantity, dimension ):
    centroids = linked_Centroid()
    for i in range ( quantity ):
        puntCentroides = []
        for j in range ( dimension ):
            puntCentroides.append( uniform(0,10) )
        centroids.add_end_centroid( puntCentroides )
    return centroids

def generate_point ( quantitypoints ):
    points = []
    for j in range ( quantitypoints ):
        points.append( uniform(0,1) )
    return points

# Reaccina los nuevos puntos a su centroides correspondiente
def refinament_points( centroids ):
    tmp = centroids.getHead()
    pert = 0
    while tmp != None:
        if ( tmp.first ):
            ptmp = tmp.first.getHead()
            while ptmp != None:
                point = ptmp.get_data()
                dest = centroids.min_distance( point )
                if ( dest != pert ):
                    centroids.add_point( point, dest, ptmp.get_type() )
                    ptmp = ptmp.get_next()
                    tmp.first.delete_node( point )
                else:
                    ptmp = ptmp.get_next()
        pert += 1
        tmp = tmp.next

def generate_numbers(begin, end):
    vector = []
    while ( len(vector) < 10 ):
        num = randint(begin, end)
        if not ( num in vector ):
            vector.append( num )
    return sorted( vector )


def point_from_file( path, centroids ):
    r1 = generate_numbers(0,50)
    r2 = generate_numbers(50,100)
    r3 = generate_numbers(100,150)
    Training = linked_list ()
    Test = linked_list()
    dataset = np.loadtxt( path, delimiter=',')
    for i in range ( 150 ):
        if i in r1 or i in r2 or i in r3 :
            Test.add_at_end( dataset[i][:len(dataset[i])-1], dataset[i][len(dataset[i])-1:len(dataset[i])] )
        else:
            point = dataset[i][:len(dataset[i])-1]
            centroids.add_point( point, centroids.min_distance( point ), dataset[i][len(dataset[i])-1:len(dataset[i])] )
            Training.add_at_end( dataset[i][:len(dataset[i])-1], dataset[i][len(dataset[i])-1:len(dataset[i])] )
    return Training, Test

def precision ( centroids, points ):
    conf = []
    for i in range( 3 ):
        conf.append( [0] * 3 )
    ttmp = points.getHead()
    while ttmp != None:
	    typePoint = ttmp.get_type()
	    typeCent = centroids.get_classcentroids( centroids.min_distance( ttmp.get_data()) )
	    conf[int(typePoint)][int(typeCent)] += 1
	    ttmp = ttmp.get_next()
    return conf

def main():
    centroids = generate_centroids( 3 , 4 )
    Training, Test = point_from_file('data.txt', centroids)
    while not centroids.centroid_point_one():
        centroids = generate_centroids( 3 , 4 )
        tmp = Training.getHead()
        while tmp != None:
            centroids.add_point( tmp.get_data(), centroids.min_distance( tmp.get_data() ), tmp.get_type() )
            tmp = tmp.get_next()
    while True:
        centroids.refinament_centroids()
        refinament_points( centroids )
        if ( centroids.error( 0.001 ) ):
            break
    centroids.classification()
    view = np.array( precision( centroids, Test) )
    print ( view )
    precisionMatrix = float ( np.trace(view) ) / 30
    print("Presición: " + str ( precisionMatrix ))
    centroids.print_list( False )

if __name__ == '__main__':
    main()
