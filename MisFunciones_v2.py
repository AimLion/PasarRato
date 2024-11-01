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
            pitidoError()
            print("Error! Debe dar un número entero. Intente de nuevo.\n")


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