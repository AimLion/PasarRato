# 
# IMPORTACIÓN METODOS --
from time import sleep 
from random import randint
from funciones import *
import menu_interactive as interac
import music as m
import text as t
import money as money

limpiar()
m.Init()

# 
# DECLARACIÓN VARIABLES --
registroPJ = Queue();       registroE = Queue()
vidaPJ = 2500; vidaE = 0;  totalPJ = 0;  totalE = 0; ataquePJ = 0; ataqueE = 0;  ApromE = 0;
ApromPJ = 0;   Round = 1;  upgrade = 0;  chk = 0;    music = 0;    gameover = 0; option = 0;
check = 0;     curacion = 1500;  i = 0;  z = 0;      cantm = 0;    newvidaPJ = 0; vendido = [0,0,0]
personaje = "Peleador"; NoOption="Esta opción no es válida"; teclastr=""

# 
# PANTALLA DE CARGA -- 
while True:
    m.Menu()
    m.Vup()
    print("Bienvenido al Sistema de Combate Automatizado")
    print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
    print("\nMenu de opciones")
    print("\n1) Iniciar Partida")
    print(f"2) Comprar Mejoras ( ${cantm} monedas )")
    print(f"3) Cambia de personaje ({personaje})")
    print("4) Salir")
    option = leer_entero("\nSeleccionar Opción: ")
    match option:
        case 2:
            if ( check == 1 ):
                print("\nYa tienes una mejora!")
                sleep(1.5); limpiar()
            else:
                limpiar()
                upgrade,chk,check,cantm=(t.Mejoras(cantm))
                sleep(1.5); limpiar()
        case 1:
            sleep(1)
            music = randint(1,3)
            m.FondoMusicaPelea(music)
            while True:
                tecla,teclastr = enter("\n¿Listo para el combate?(S/N) → ")
                print(teclastr)
                sleep(1)
                if tecla==b'N' or tecla==b'n' :
                    m.Stop(); upgrade=0; Round=1
                    check=0; chk=0; limpiar();break
                elif tecla==b'S' or tecla==b's':
                    limpiar()
                    print("Cargando combate . . .")
                    sleep(1)
                    if (newvidaPJ != 0):vidaPJ = newvidaPJ
                    else: vidaPJ = 2500
                    totalPJ = 0; totalE = 0; ApromPJ = 0; ApromE = 0;  i = 0;      z = 0
                    if (check==1) and (chk==2): vidaPJ=vidaPJ+upgrade
                    for x in range(0,registroE.size()): registroE.dequeue()
                    for y in range(0,registroPJ.size()): registroPJ.dequeue()
                    vidaE=(t.vidaEXround(Round))
                    print(f"\nInicia Combate!! RONDA ",Round)
                    t.level(Round)
                    if (Round == 6):
                        m.Stop(); sleep(1)
                        m.TemaBoss()
                        sleep(1); t.jefe()
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
                            ataqueE = randint(400,800)
                            if (Round < 6): vidaPJ,totalE=(t.attackJ(vidaPJ,totalE,ataqueE,registroE))
                            elif (Round == 6) and (check==1) and (chk==3): 
                                while True:
                                    tecla,teclastr=enter("Quieres bloquear este ataque?: (s/n)\n")
                                    if tecla==b'N' or tecla==b'n' :
                                        print(teclastr)
                                        vidaPJ,totalE=(t.attackJ(vidaPJ,totalE,ataqueE,registroE));break
                                    elif tecla==b'S' or tecla==b's':
                                        print(f"Has bloqueado {ataqueE} de daño!"); chk=0;break
                                    else: print(NoOption);sleep(1);limpiar()
                            else: vidaPJ,totalE=(t.attackJ(vidaPJ,totalE,ataqueE,registroE))
                            i = 0
                            sleep(1)
                        # 
                        # ATAQUE PROPIO ---
                        valattack=Round,check,chk,z,upgrade,personaje,vidaE,totalPJ,registroPJ,vidaPJ
                        ataquePJ,vidaE,totalPJ=(t.attack(valattack))
                        sleep(1)
                        print("\nTu vida: ",vidaPJ," Su vida: ",vidaE)
                        # 
                        # CURACIÓN AMBOS ---
                        z = z + 1
                        if (z == 11):
                            vidaE = vidaE + curacion
                            while True:
                                print("\n¡¡El enemigo a recuperado 1500 de vida!!")
                                tecla,teclastr = enter("\n¿Quieres curarte (S/N) → ")
                                print(teclastr)
                                if tecla==b'S' or tecla==b's' :
                                    curacion = randint(300,1500)
                                    print(f"\nTe has curado ",curacion," de vida!!")
                                    break
                                elif tecla==b'N' or tecla==b'n': break
                                else: print(NoOption);t.sleep(1);limpiar()
                        if (vidaE<=0) or (vidaPJ<=0): break
                        # 
                        # OPCIÓN RETIRO ---
                        while (vidaPJ<=200):
                            tecla,teclastr = enter("\n¿Quieres retirarte (S/N) → ")
                            print(teclastr)
                            if tecla==b'N' or tecla==b'n' : break
                            elif tecla==b'S' or tecla==b's': gameover = 1; break
                            else: print(NoOption);t.sleep(1);limpiar()
                        if gameover==1: break
                    # 
                    # DATOS FINALES Y RESULTADO ---
                    t.status(vidaPJ,vidaE,Round,z)
                    ApromPJ = totalPJ / registroPJ.size()
                    ApromE,cantm = t.oneshot(registroE,totalE,cantm)
                    t.resultados(registroPJ,totalPJ,ApromPJ,ApromE,totalE,registroE)
                    if gameover==0: cantm = money.moneyxR(cantm,Round,vidaPJ)
                    if personaje=="Peleador": cantm = t.habP(vidaPJ,cantm,Round)
                    sleep(0.4)
                    if (vidaPJ <= 0) or (Round == 6):
                        m.Stop(); sleep(0.5)
                        if (vidaPJ <= 0) or (gameover == 1):
                            m.GameOver(); cantm=cantm/2; print(f"\nPenalización de Gameover - Monedas / 2\nMonedas:{cantm}")
                        if (Round == 6) and (vidaPJ > 0) and (gameover == 0): 
                            print("Lograste derrotar al jefe!! ( + $250 monedas )")
                            cantm = cantm +  250; m.Win();
                        sleep(11); Round = 1; limpiar(); m.Stop();
                        gameover = 0; upgrade = 0; check = 0
                        break
                    else: Round = Round + 1; continue
                else:print(NoOption); t.sleep(1); limpiar()
        case 3:
            print("\nCargando personajes . . .")
            m.seleccion()
            personaje,newvidaPJ,cantm,vendido=interac.interactiveMenu("personaje","Peleador","Asesino","Tanque","Tirador","√",300,cantm,vendido)
            limpiar()
        case 4:
            break
        case _:
            print(NoOption); t.sleep(1); limpiar()

t.lectura("Vuelva Pronto!!")
sleep(1)
