# 
# IMPORTACIÓN METODOS --
from time import sleep 
from random import randint
from stack_and_queue import Queue
from MisFunciones_v2 import leer_tecla
import music as m
import text as t
import os

os.system('cls')
m.Init()

# 
# DECLARACIÓN VARIABLES --
registroPJ = Queue()
registroE = Queue()
vidaPJ = 2500
vidaE = 0
curacion = 1500
totalPJ = 0
totalE = 0
ataquePJ = 0
ataqueE = 0
ApromE = 0
ApromPJ = 0
Round = 1
music = 0
gameover = 0
i = 0
z = 0

# 
# PANTALLA DE CARGA -- 
while True:
    print("Bienvenido al Sistema de Combate Automatizado --")
    tecla = leer_tecla("\n¿Desea iniciar una nueva partida (S/N) → ")
    print(tecla)
    sleep(1)
    music = randint(1,2)
    if tecla.upper() == 'N' or tecla.upper() == 'n' :
        break
    else:
        m.FondoMusica(music)
        while True:
            tecla = leer_tecla("\n¿Listo para el combate?(S/N) → ")
            print(tecla)
            sleep(1)
            os.system("CLS")
            if tecla.upper() == 'N' or tecla.upper() == 'n' :
                gameover = 1
                m.Stop()
                break
            else:
                print("\nCargando combate . . .")
                sleep(1)
                vidaPJ = 2500
                totalPJ = 0
                totalE = 0
                ApromPJ = 0
                ApromE = 0
                i = 0
                z = 0
                for x in range(1,registroE.size()):
                    registroE.dequeue()
                for y in range(1,registroPJ.size()):
                    registroPJ.dequeue()
                match(Round):
                    case 1:
                        vidaE = 500
                    case 2:
                        vidaE = 1000
                    case 3:
                        vidaE = 1500
                    case 4:
                        vidaE = 2000
                    case 5:
                        vidaE = 2500
                    case 6:
                        vidaE = 5000
                print(f"\nInicia Combate!! RONDA ",Round)
                if (Round == 6):
                    m.Stop()
                    sleep(1)
                    m.TemaBoss()
                    sleep(1)
                    t.jefe()
                print("\nTu vida: ",vidaPJ," Su vida: ",vidaE)
                # 
                # COMBATE ---
                while (vidaPJ > 0) and (vidaE > 0):
                    i = i + 1
                    sleep(1.5)
                    os.system("CLS")
                    # 
                    # ATAQUE ENEMIGO ---
                    if i == 2:
                        ataqueE = randint(300,650)
                        vidaPJ = vidaPJ - ataqueE
                        print(F"\nTe a bajado ", ataqueE, " de vida")
                        i = 0
                        totalE = totalE + ataqueE
                        registroE.enqueue(ataqueE)
                        sleep(1)
                    # 
                    # ATAQUE PROPIO ---
                    match(Round):
                        case 1:
                            ataquePJ = randint(50,300)
                        case 2:
                            ataquePJ = randint(100,400)
                        case 3:
                            ataquePJ = randint(100,500)
                        case 4:
                            ataquePJ = randint(200,600)
                        case 5:
                            ataquePJ = randint(200,700)
                        case 6:
                            ataquePJ = randint(300,800)
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
                        print("\n¡¡El enemigo a recuperado 1500 de vida!!")
                        vidaE = vidaE + curacion
                        tecla = leer_tecla("\n¿Quieres curarte (S/N) → ")
                        print(tecla)
                        if tecla.upper() == 'S' or tecla.upper() == 's' :
                            curacion = randint(300,1500)
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
                            gameover = 1
                            break
                # 
                # DATOS FINALES Y RESULTADO ---
                if (vidaE <= 0) and (vidaPJ>0):
                    print(F"\nGran combate!! Has sobrevivido ",z," turnos con ",vidaPJ," de vida")
                elif(vidaE<=0) and (vidaPJ<=0):
                    print(f"\nA sido un gran combate, se declara un empate.")
                    print(f"Llegaste hasta el nivel: ",Round)
                else:
                    print(f"\nBuen intento, ha sobrevivido el enemigo con ",vidaE," de vida")
                    print(f"Llegaste hasta el nivel: ",Round)
                
                ApromE = totalE / registroE.size()
                ApromPJ = totalPJ / registroPJ.size()
                
                t.resultados(registroPJ,totalPJ,ApromPJ,ApromE,totalE,registroE)
                if (vidaPJ <= 0) or (Round == 6):
                    m.Stop()
                    sleep(0.5)
                    if (vidaPJ <= 0) or (gameover == 1): m.GameOver()
                    if (Round == 6) and (vidaPJ > 0) and (gameover == 0): m.Win()
                    sleep(11)
                    Round = 1
                    os.system('cls')
                    m.Stop()
                    gameover = 0
                    break
                else:
                    Round = Round + 1
                    continue

t.despedida("Vuelva Pronto!!")
sleep(2)
