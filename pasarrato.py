# 
# IMPORTACIÓN METODOS --
from time import sleep 
from random import randint
from translation import TxtPrint, Translate
from funciones import *
from valores import *
import menu_interactive as interac
import music
import text
import money as money

limpiar()
music.Init()
registroPJ = Queue()
registroE = Queue()

# 
# PANTALLA DE CARGA -- 
while True:
    music.Menu()
    music.Vup()
    print(TxtPrint("main_menu", cantm=cantm, personaje=personaje))

    option = leer_entero(TxtPrint("select_menu"))
    match option:
        case 1:
            sleep(1)
            NumDiscoMusic = randint(1,3)
            music.FondoMusicaPelea(NumDiscoMusic)
            while True:
                tecla = enter(TxtPrint("check_combat"))
                sleep(1)
                if tecla==b'N' or tecla==b'n' :
                    music.Stop(); upgrade=0; Round=1; check=0;
                    chk=0; limpiar(); roundm=0; break
                elif tecla==b'Y' or tecla==b'y':
                    limpiar()
                    print(TxtPrint("loading_combat"))
                    sleep(1)
                    if (newvidaPJ != 0):vidaPJ = newvidaPJ
                    else: vidaPJ = 2500
                    totalPJ = 0; totalE = 0; ApromPJ = 0; ApromE = 0; i = 0; z = 0;
                    if (check==1) and (chk==2): vidaPJ=vidaPJ+upgrade
                    for x in range(0,registroE.size()): registroE.dequeue()
                    for y in range(0,registroPJ.size()): registroPJ.dequeue()
                    vidaE=(text.vidaEXround(Round))
                    print(TxtPrint("ready_combat", Round=Round))
                    text.level(Round,zona)
                    if (Round == 6):
                        music.Stop(); sleep(1)
                        music.TemaBoss()
                        sleep(1); text.jefe()
                    print(TxtPrint("values_character", vidaPJ=vidaPJ, vidaE=vidaE))
                    sleep(1)
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
                            if (Round < 6): vidaPJ,totalE=(text.attackJ(vidaPJ,totalE,ataqueE,registroE))
                            elif (Round == 6) and (check==1) and (chk==3): 
                                while True:
                                    tecla = enter(TxtPrint("check_shield"))
                                    if tecla==b'N' or tecla==b'n' :
                                        vidaPJ,totalE=(text.attackJ(vidaPJ,totalE,ataqueE,registroE));break
                                    elif tecla==b'S' or tecla==b's':
                                        print(TxtPrint("blocked_damage", ataqueE=ataqueE)); chk=0;break
                                    else: print(TxtPrint("invalid_option"));sleep(1.5);limpiar()
                            else: vidaPJ,totalE=(text.attackJ(vidaPJ,totalE,ataqueE,registroE))
                            i = 0
                            sleep(1)
                        # 
                        # ATAQUE PROPIO ---
                        valattack=Round,check,chk,z,upgrade,personaje,vidaE,totalPJ,registroPJ,vidaPJ
                        ataquePJ,vidaE,totalPJ=(text.attack(valattack))
                        sleep(1)
                        print(TxtPrint("values_character", vidaPJ=vidaPJ, vidaE=vidaE))
                        # 
                        # CURACIÓN AMBOS ---
                        z = z + 1
                        if (z == 11):
                            vidaE = vidaE + curacion
                            while True:
                                print(TxtPrint("health_boss"))
                                tecla = enter(TxtPrint("health_option"))
                                if tecla==b'S' or tecla==b's' :
                                    curacion = randint(300,1500)
                                    print(TxtPrint("life_restored", curacion=curacion))
                                    break
                                elif tecla==b'N' or tecla==b'n': break
                                else: print(TxtPrint("invalid_option"));text.sleep(1);limpiar()
                        if (vidaE<=0) or (vidaPJ<=0): break
                        # 
                        # OPCIÓN RETIRO ---
                        while (vidaPJ<=200):
                            tecla = enter(TxtPrint("surrender_option"))
                            if tecla==b'N' or tecla==b'n' : break
                            elif tecla==b'S' or tecla==b's': gameover = 1; break
                            else: print(TxtPrint("invalid_option"));text.sleep(1.5);limpiar()
                        if gameover==1: break
                    # 
                    # DATOS FINALES Y RESULTADO ---
                    text.status(vidaPJ,vidaE,Round,z,zona)
                    ApromPJ = totalPJ / registroPJ.size()
                    ApromE,roundm = text.oneshot(registroE,totalE,roundm)
                    text.resultados(registroPJ,totalPJ,ApromPJ,ApromE,totalE,registroE)
                    if gameover==0: roundm = money.moneyxR(roundm,Round,vidaPJ)
                    if personaje=="Peleador": roundm = text.habP(vidaPJ,roundm,Round)
                    sleep(0.4)
                    if (vidaPJ <= 0) or (Round == 6):
                        music.Stop(); sleep(0.5)
                        if (vidaPJ <= 0) or (gameover == 1):
                            music.GameOver(); cantm=cantm+(roundm/2); print(TxtPrint("penalty_gameover", monedas=cantm))
                        if (Round == 6) and (vidaPJ > 0) and (gameover == 0):
                            print(TxtPrint("win_boss"))
                            cantm = cantm + roundm + 150; music.Win(); zona = zona + 1;
                        sleep(11); Round = 1; limpiar(); music.Stop();
                        gameover = 0; upgrade = 0; check = 0; roundm = 0
                        break
                    else: Round = Round + 1; continue
                else:print(TxtPrint("invalid_option")); text.sleep(1); limpiar()
        case 2:
            if ( check == 1 ):
                print(TxtPrint("validation_upgrade"))
                sleep(1.5); limpiar()
            else:
                limpiar()
                upgrade,chk,check,cantm=(text.Mejoras(cantm))
                sleep(1.5); limpiar()
        case 3:
            print(TxtPrint("loading_characters"))
            music.seleccion()
            personaje,newvidaPJ,cantm,vendido=interac.interactiveMenu("Peleador","Asesino","Tanque","Tirador","√",300,cantm,vendido)
            limpiar()
        case 4:
            Translate()
            sleep(1)
            limpiar()
        case 5:
            break
        case _:
            print(TxtPrint("invalid_option")); text.sleep(1); limpiar()

text.lectura(TxtPrint("logout"))
sleep(1.5)
limpiar()
