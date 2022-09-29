#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 13:19:29 2019

@author: gabriel
"""
# Importaciones
import math
import gc
from random import uniform,random

# Creamos el nodo que contendra la informacion de los puntos ingresados
class node:

    # Constructor del nodo donde estara el punto manejado como vector
    def __init__ ( self, data = None, next = None ):
        self.data = data
        self.next = next

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
    def add_at_end ( self, data ):
        if not ( self.head ):
            self.head = node ( data = data )
            return
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = node ( data = data )

    # Elimina un punto especifico
    def delete_node ( self, key ):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
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
            node = node.next

# Centroide

class nodeCentroid:

    # Constructor estructura donde esta los puntos centroides y sus puntos
    def __init__ ( self, centroid = None, next = None, first = None, oldcenotrid = None ):
        self.oldcentroid = None
        self.centroid = centroid
        self.next = next
        self.first = first

    def getCentroid( self ):
        return self.centroid

    def getNext( self ):
        return self.next

    def getFirst( self ):
        return self.first

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
    def add_point ( self, point, place ):
        tmp = self.headCentroid
        for i in range( place ):
            tmp = tmp.next
        if not ( tmp.first ):
            tmp.first = linked_list()
            tmp.first.add_at_end( point )
            return
        tmp.first.add_at_end( point )

    # Muestra la lista de centroides
    def print_list( self ):
        node = self.headCentroid
        while node != None:
            print ( " Centroide: " + str( node.centroid ) )
            list_point = node.first
            if not ( list_point ):
                print ( " No tiene puntos asignados este centroide " )
            else:
                print ( " Los puntos asignados son: " )
                list_point.print_list()
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

def generate_centroids ( quantity, quantitypoints ):
    centroids = linked_Centroid()
    for i in range ( quantity ):
        puntCentroides = []
        for j in range ( quantitypoints ):
            puntCentroides.append( uniform(0,1) )
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
                    centroids.add_point( point, dest )
                    ptmp = ptmp.get_next()
                    tmp.first.delete_node( point )
                else:
                    ptmp = ptmp.get_next()
        pert += 1
        tmp = tmp.next

def main():
    centroids = generate_centroids( 3 , 2 )
    for i in range ( 1000 ):
        point = generate_point( 2 )
        centroids.add_point( point, centroids.min_distance( point ) )
    while True:
        centroids.refinament_centroids()
        refinament_points( centroids )
        if ( centroids.error(0.00000001) ):
            break
    gc.collect()
    centroids.print_list()

if __name__ == '__main__':
    main()
