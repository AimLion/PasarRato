# Archivo: stack_and_queue.py
# 
# Autor: Prof. José Padilla Duarte
# Email: jopadu@gmail.com
# Fecha de última modificación: 04-noviembre-2021
# 
# Objetivo: Proveer de clases para el manejo estricto de Pilas y Colas.
#
# Fuentes consultadas:
# http://www.juanjoconti.com/posts/2010/07/22/pilas-y-cola-en-python/

class Stack:
    ''' Clase para implementar una Pila de comportamiento estricto que solo permite operaciones de push y pop
    '''
    def __init__(self):
        self.__items = []

    def size(self):
        return len(self.__items)

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if len(self.__items) < 1:
            return None
        return self.__items.pop()     # Saca el último elemento de la pila (el del tope).

    def peek(self):
        ''' Muestra el valor del tope de la pila sin extraerlo. '''
        if len(self.__items) < 1:
            return None
        return self.__items[-1]

    def all_items(self):
        return self.__items

    def clear(self):
        self.__items.clear()
    
    def replace(self,old_value,new_value):
        for x in range(self.size()):
            if self.__items[x] == old_value:
                self.__items[x] = new_value

class Queue:
    ''' Clase para implementar una Cola de comportamiento estricto que solo permite operaciones de enqueue y dequeue
    '''
    def __init__(self):
        self.__items = []

    def size(self):
        return len(self.__items)

    def enqueue(self, item):
        ''' Encolar: Meter un elemento a la cola. '''
        self.__items.append(item)

    def dequeue(self):
        ''' Desencolar: Sacar un elemento de la cola.'''
        if len(self.__items) < 1:
            return None
        return self.__items.pop(0)    # Saca el primer elemento de la cola

    def first(self):
        ''' Devuelve el valor del elemento de inicio de la cola sin extraerlo. '''
        if len(self.__items) < 1:
            return None
        return self.__items[0]

    def last(self):
        ''' Devuelve el valor del elemento final de la cola sin extraerlo. '''
        if len(self.__items) < 1:
            return None
        return self.__items[-1]
        
    def all_items(self):
        return self.__items

    def clear(self):
        self.__items.clear()

    def suma(self):
        return sum(self.__items())
