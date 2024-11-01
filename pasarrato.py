# 
# IMPORTACIÓN METODOS --
from time import sleep 
from random import randint
from stack_and_queue import Queue
from MisFunciones_v2 import *
import music as m
import text as t

limpiar()
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
option = 0
check = 0
upgrade = 0
chk = 0
i = 0
z = 0

# 
# PANTALLA DE CARGA -- 
while True:
    m.Menu()
    print("Bienvenido al Sistema de Combate Automatizado")
    print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
    print("\nMenu de opciones")
    print("\n1) Iniciar Partida")
    print("2) Comprar Mejoras")
    print("3) Salir")
    option = leer_entero("\nSeleccionar Opción: ")
    match option:
        case 2:
            if ( check == 1 ):
                print("\nYa tienes una mejora!")
                sleep(1.5)
                limpiar()
            else:
                limpiar()
                upgrade,chk,check=(t.Mejoras())
                sleep(1.5)
                limpiar()
        case 1:
            sleep(1)
            music = randint(1,3)
            m.FondoMusicaPelea(music)
            while True:
                tecla = leer_tecla("\n¿Listo para el combate?(S/N) → ")
                print(tecla)
                sleep(1)
                limpiar()
                if tecla.upper() == 'N' or tecla.upper() == 'n' :
                    m.Stop()
                    upgrade=0
                    Round=1
                    check=0
                    chk=0
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
                    if (check==1) and (chk==2): vidaPJ=vidaPJ+upgrade
                    for x in range(0,registroE.size()):
                        registroE.dequeue()
                    for y in range(0,registroPJ.size()):
                        registroPJ.dequeue()
                    vidaE=(t.vidaEXround(Round))
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
                        limpiar()
                        # 
                        # ATAQUE ENEMIGO ---
                        if i == 2:
                            ataqueE = randint(300,700)
                            if (Round < 6):
                                vidaPJ,totalE=(t.attackJ(vidaPJ,totalE,ataqueE,registroE))
                            elif (Round == 6) and (check==1) and (chk==3): 
                                tecla=leer_tecla("Quieres bloquear este ataque?: (s/n)")
                                if tecla.upper() == 'N' or tecla.upper() == 'n' :
                                    vidaPJ,totalE=(t.attackJ(vidaPJ,totalE,ataqueE,registroE))
                                else:
                                    print(f"\nHas bloqueado {ataqueE} de daño!")
                                    chk=0
                            else:
                                vidaPJ,totalE=(t.attackJ(vidaPJ,totalE,ataqueE,registroE))
                            i = 0
                            sleep(1)
                        # 
                        # ATAQUE PROPIO ---
                        ataquePJ,vidaE,totalPJ=(t.attack(Round,check,chk,upgrade,vidaE,totalPJ,registroPJ))
                        sleep(1)
                        print("\nTu vida: ",vidaPJ," Su vida: ",vidaE)
                        # 
                        # CURACIÓN AMBOS ---
                        z = z + 1
                        if (z == 9):
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
                        if (z >= 11):
                            tecla = leer_tecla("\n¿Quieres retirarte (S/N) → ")
                            print(tecla)
                            if tecla.upper() == 'N' or tecla.upper() == 'n' :
                                continue
                            else:
                                gameover = 1
                                break
                    # 
                    # DATOS FINALES Y RESULTADO ---
                    t.status(vidaPJ,vidaE,Round,z)
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
                        limpiar()
                        m.Stop()
                        gameover = 0
                        upgrade = 0
                        check = 0
                        break
                    else:
                        Round = Round + 1
                        continue
        case 3:
            break

t.lectura("Vuelva Pronto!!")
sleep(2)
