# 
# IMPORTACIÓN METODOS --
from time import sleep 
from random import randint
from msvcrt import getch
from stack_and_queue import Queue
import os

os.system("CLS")

# 
# DECLARACIÓN VARIABLES --
registroPJ = Queue()
registroE = Queue()
vidaE = 5000
vidaPJ = 2500
curacion = 1000
totalPJ = 0
totalE = 0
ataquePJ = 0
ataqueE = 0
ApromE = 0
ApromPJ = 0
i = 0
z = 0

# 
# LECTOR TECLA --
def leer_tecla(_msj):
    print(_msj, end="", flush=True)
    tecla = getch()
    if tecla == b'\x1b':
        return "Escape"
    else:
        return tecla.decode("ANSI")
# 
# PANTALLA DE CARGA --
print("Bienvenido al Sistema de Combate Automatizado --")
while True:
    tecla = leer_tecla("\n¿Desea iniciar un nuevo combate (S/N) → ")
    print(tecla)
    if tecla.upper() == 'N' or tecla.upper() == 'n' :
        break
    else:
        print("\nCargando combate . . .")
        vidaPJ = 2500
        vidaE = 5000
        totalPJ = 0
        totalE = 0
        ApromPJ = 0
        ApromE = 0
        z = 0
        for x in range(1,registroE.size()):
            registroE.dequeue()
        for y in range(1,registroPJ.size()):
            registroPJ.dequeue()
    # 
    # COMBATE ---
    while (vidaPJ > 0) and (vidaE > 0):
        i = i + 1
        sleep(2)
        os.system("CLS")
        # 
        # ATAQUE ENEMIGO ---
        if i == 2:
            ataqueE = randint(150,800)
            vidaPJ = vidaPJ - ataqueE
            print(F"\nTe a bajado ", ataqueE, " de vida")
            i = 0
            totalE = totalE + ataqueE
            registroE.enqueue(ataqueE)
            sleep(1)
        # 
        # ATAQUE PROPIO ---
        ataquePJ = randint(350,800)
        vidaE = vidaE - ataquePJ
        print(f"\nLe has bajado ", ataquePJ, " de vida")
        sleep(1)
        print("\nTu vida: ",vidaPJ," Su vida: ",vidaE)
        totalPJ = totalPJ + ataquePJ
        registroPJ.enqueue(ataquePJ)
        # 
        # CURACIÓN AMBOS ---
        z = z + 1
        if (z == 7):
            print("\n¡¡El enemigo se a curado 1000 de vida!!")
            vidaE = vidaE + curacion
            tecla = leer_tecla("\n¿Quieres curarte (S/N) → ")
            print(tecla)
            if tecla.upper() == 'S' or tecla.upper() == 's' :
                curacion = randint(100,1500)
                print(f"\nTe has curado ",curacion," de vida!!")
            else:
                continue
        if (vidaE<=0) or (vidaPJ<=0):
            break
        # 
        # OPCIÓN RETIRO ---
        if (z >= 10):
            tecla = leer_tecla("\n¿Quieres retirarte (S/N) → ")
            print(tecla)
            if tecla.upper() == 'N' or tecla.upper() == 'n' :
                continue
            else:
                break
    # 
    # DATOS FINALES Y RESULTADO ---
    if (vidaE <= 0) and (vidaPJ>0):
        print(F"\nGran combate!! Has sobrevivido ",z," turnos con ",vidaPJ," de vida")
    elif(vidaE<=0) and (vidaPJ<=0):
        print(f"\nA sido un gran combate, se declara un empate.")
    else:
        print(f"\nBuen intento, ha sobrevivido el enemigo con ",vidaE," de vida")
    ApromE = totalE / registroE.size()
    ApromPJ = totalPJ / registroPJ.size()

    print(f"\nCantidad de daño propio: ",registroPJ.all_items()," Total → ",totalPJ)
    print(f"Cantidad de daño del enemigo: ",registroE.all_items()," Total → ",totalE)
    print(f"\nTu daño promedio: ",ApromPJ)
    print(f"Su daño promedio: ",ApromE)

print("\nVuelva Pronto!!")
sleep(1.5)
