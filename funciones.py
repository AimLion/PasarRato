from msvcrt import getch
import os
import winsound

# ------------- Funciones -------------
def pitidoError():
    winsound.Beep(880,125)
    winsound.Beep(700,125)


def leer_entero(_msj):
    while True:
        try:
            return int(input(_msj))
        except:
            break


def leer_eleccion(_msj):
    while True:
        if _msj==2:
            _msj = 0
        else:
            try:
                return int(input(_msj))
            except:
                break


def leer_float(_msj):
    while True:
        try:
            return float(input(_msj))
        except:
            pitidoError()
            print("Error! Debe dar un número entero. Intente de nuevo.\n")


def leer_tecla(_msj):
    print(_msj, end="", flush=True)     # El flush=True es para que imprima la línea de una vez.
    tecla = getch()
    # print(ord(tecla))     # Para saber el código de la tecla pulsada
    if tecla == b'\x1b':    # ESC
        return "Escape"
    else:
        return tecla.decode("ANSI")

def enter(_msj):
    print(_msj, end="", flush=True)
    tecla = getch()
    # print(ord(tecla))
    # if tecla == b'\x1b':    # ESC
    #     return "Escape"
    # else:
    return tecla,tecla.decode("ANSI")

def limpiar():
    if os.name == 'nt':
        os.system("CLS")        # Windows
    else:
        os.system("Clear")      # Linux


def pausa_final():
    print("Presione una tecla para Terminar.")
    getch()     # msvcrt.getch()


def pausa(_msj=""):
    print(_msj, end="", flush=True)
    return getch()

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
