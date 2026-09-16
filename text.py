# 
# IMPORTACIÓN MÉTODOS --
from translation import TxtPrint
from funciones import *
from random import randint
from money import compra
from time import sleep
import keyboard as kb
import music

music.Init()
# 
# TEXTOS A IMPRIMIR --
def jefe():
    '''Método enfocado en la presentación del Jefe'''
    secuencia_textos = [
        "jefe_txt0", "jefe_txt1", "jefe_txt2", "jefe_txt3",
        "jefe_txt4", "jefe_txt5", "jefe_txt6", "jefe_txt7"
    ]

    for x in range(0,8):
        if x == 0: sleep(0.1)
        print(TxtPrint(secuencia_textos[x]))
        if x == 3: sleep(0.5)
        if x != 7: sleep(2)

# TODO Corregir variables de 1 sola vocal a 2 vocales, para que se pueda traducir correctamente. Ejemplo: "vidaE" a "vidaEnemigo"
def status(vidaPJ,vidaE,Round,z,zona):
    '''Muestra los Resultados al Final de cada Ronda parte 1'''
    if (vidaE <= 0) and (vidaPJ>0): print(TxtPrint("victory_message", z=z, vidaPJ=vidaPJ))
    elif(vidaE<=0) and (vidaPJ<=0):
        print(TxtPrint("draw_message"))
        print(TxtPrint("round_zone_message", Round=Round, zona=zona))
    else:
        print(TxtPrint("defeat_message", vidaE=vidaE))
        print(TxtPrint("round_zone_message", Round=Round, zona=zona))

def resultados(registroPJ,totalPJ,ApromPJ,ApromE,totalE,registroE):
    '''Muestra los Resultados al Final de cada Ronda parte 2'''
    print(TxtPrint("player_dmg_message", registroPJ=registroPJ.all_items(), totalPJ=totalPJ))
    print(TxtPrint("enemy_dmg_message", registroE=registroE.all_items(), totalE=totalE))
    print(TxtPrint("player_avg_dmg_message", ApromPJ=ApromPJ))
    print(TxtPrint("enemy_avg_dmg_message", ApromE=ApromE))

def lectura(texto):
    '''Método de lectura de Sans'''
    music.Bye()
    for char in texto:
        music.Play()
        print(char, end="", flush=True)
        sleep(0.07)
        if char == " ":
            music.Stop()
            sleep(0.5)
        if char == "\n":
            music.Stop()
            sleep(0.7)
    print()

def attackJ(vidaPJ,totalE,ataqueE,registroE):
    '''Método de impresión y ataque del Jefe'''
    vidaPJ = vidaPJ - ataqueE
    totalE = totalE + ataqueE
    registroE.enqueue(ataqueE)
    print(TxtPrint("attacked_enemy_message", ataqueE=ataqueE))
    print(" ")
    return vidaPJ,totalE

def oneshot(registroE,totalE,money):
    '''Oneshot, simplemente'''
    if(totalE==0):
        print(TxtPrint("oneshot_message"))
        money = money + 100
        ApromE = 0;registroE.enqueue(0)
    else: ApromE = totalE / registroE.size()
    return ApromE,money

def zonalv(zona):
    '''Define la zona de juego'''
    lv1 = ""; lv2 = ""; lv3 = ""; lv4 = ""; lv5 = ""; lv6 = ""; nombre = ""
    match zona:
        case 1:
            nombre = TxtPrint("zone1_name")
            lv1 = "Ø     O--O |\n|  \   /   | |\n|   \ /    | |\n|    O     O"
            lv2 = "O     O--O |\n|  \   /   | |\n|   \ /    | |\n|    Ø     O"
            lv3 = "O     Ø--O |\n|  \   /   | |\n|   \ /    | |\n|    O     O"
            lv4 = "O     O--Ø |\n|  \   /   | |\n|   \ /    | |\n|    O     O"
            lv5 = "O     O--O |\n|  \   /   | |\n|   \ /    | |\n|    O     Ø"
            lv6 = "| O     O--O |\n|  \   /   | |\n|   \ /    | |\n|    O     O-|-Ø"
            # MAPA ZONA 1
            # |O     O--O |
            # | \   /   | |
            # |  \ /    | |
            # |   O     O |
        case 2:
            nombre = TxtPrint("zone2_name")
            lv1 = "Ø--~     O |\n|     \   /| |\n|      \ / | |\n|       O  | |\n|     O----O"
            lv2 = "O--~     O |\n|     \   /| |\n|      \ / | |\n|       Ø  | |\n|     O----O"
            lv3 = "O--~     Ø |\n|     \   /| |\n|      \ / | |\n|       O  | |\n|     O----O"
            lv4 = "O--~     O |\n|     \   /| |\n|      \ / | |\n|       O  | |\n|     O----Ø"
            lv5 = "O--~     O |\n|     \   /| |\n|      \ / | |\n|       O  | |\n|     Ø----O"
            lv6 = "| O--~     O |\n|     \   /| |\n| Ø    \ / | |\n| |     O  | |\n| |~~-O----O |"
            # MAPA ZONA 2
            # |Ø--~     O |
            # |    \   /| |
            # |     \ / | |
            # |      O  | |
            # |    O----O | 
        case 3:
            nombre = TxtPrint("zone3_name")
            lv1 = "Ø-~~--~~-O |\n|         /  |\n| O-~--~-O   |\n|  \         |\n|   O       "
            lv2 = "O-~~--~~-Ø |\n|         /  |\n| O-~--~-O   |\n|  \         |\n|   O       "
            lv3 = "O-~~--~~-O |\n|         /  |\n| O-~--~-Ø   |\n|  \         |\n|   O       "
            lv4 = "O-~~--~~-O |\n|         /  |\n| Ø-~--~-O   |\n|  \         |\n|   O       "
            lv5 = "O-~~--~~-O |\n|         /  |\n| O-~--~-O   |\n|  \         |\n|   Ø       "
            lv6 = "| O-~~--~~-O |\n|      Ø  /  |\n| O-~--~-O   |\n|  \   |     |\n|   O--|     |"
            # MAPA ZONA 3
            # |Ø-~~--~~-O |
            # |        /  |
            # |O-~--~-O   |
            # | \         |
            # |  O        |
    return lv1,lv2,lv3,lv4,lv5,lv6,nombre

def level(Round,zona):
    '''Imprime el Mapa del Juego'''
    lv1 = ""; lv2 = ""; lv3 = ""; lv4 = ""; lv5 = ""; lv6 = ""; nombre = ""
    lv1,lv2,lv3,lv4,lv5,lv6,nombre = zonalv(zona)
    lv = Queue()
    lv.enqueue(lv1)
    lv.enqueue(lv2)
    lv.enqueue(lv3)
    lv.enqueue(lv4)
    lv.enqueue(lv5)
    if Round>1:
        for x in range(1,(Round)): lv.enqueue(lv.dequeue())
    print(TxtPrint("map_levels"))
    print("--------------")
    if Round==6: print(lv6)
    else: print("|",lv.first(),"|")
    print("--------------")
    print(TxtPrint("actual_zone", nombre=nombre))
    sleep(0.25)

#
# DECLARACIÓN DE VARIABLES --
def vidaEXround(Round):
    '''Retorna la vida del enemigo dependiendo de la ronda'''
    match Round:
        case 1: vidaE = 500
        case 2: vidaE = 1000
        case 3: vidaE = 1500
        case 4: vidaE = 2000
        case 5: vidaE = 2500
        case 6: vidaE = 5000
    return vidaE

def attack(valattack):
    '''Método de impresión y calculo del daño del Pj'''
    Round=valattack[0]; check=valattack[1]; chk=valattack[2]; z=valattack[3]
    upgrade=valattack[4]; personaje=valattack[5]; vidaE=valattack[6]; totalPJ=valattack[7]
    registroPJ=valattack[8]; vidaPJ=valattack[9]; att=0; ataquePJ2 = 0; att4 = Queue(); attlist = 0
    match personaje:
        case "Peleador":
            ataquePJ=attackP(Round)
        case "Asesino":
            ataquePJ=attackA(Round)
            if Round == 6 and z == 2:
                print(TxtPrint("special_abiliti_assassin", personaje=personaje))
                sleep(0.75)
                music.ThemeA(6)
                ataquePJ = habA(ataquePJ)
        case "Tanque":
            ataquePJ=attackTan(Round)
            if Round == 6 and z == 4 and vidaPJ>=3000:
                print(TxtPrint("special_abiliti_tank", personaje=personaje))
                sleep(0.7)
                duoattack = randint(1,3)
                match duoattack:
                    case 1:
                        ataquePJ = ataquePJ + attackP(6)
                        pj = "Peleador"
                    case 2:
                        ataquePJ = ataquePJ + attackA(6)
                        pj = "Asesino"
                    case 3:
                        ataquePJ = ataquePJ + attackTir(6)
                        pj = "Tirador"
                att = 1
                duopj = str(pj)
        case "Tirador":
            ataquePJ=attackTir(Round)
            if Round == 6 and z == 3:
                print(TxtPrint("special_abiliti_shooter", personaje=personaje))
                sleep(0.75)
                music.ThemeTir(6)
                sleep(0.4)
                print(TxtPrint("first_atk_shooter", ataquePJ=ataquePJ))
                sleep(1)
                attlist=habT(ataquePJ2,check,chk,upgrade,att4,attlist)
            else:
                ataquePJ2=attackTir(Round)
                if(check==1) and (chk==1):ataquePJ=ataquePJ+upgrade;ataquePJ2=ataquePJ2+upgrade
                print(TxtPrint("attacked_shooter_message", ataquePJ=ataquePJ, ataquePJ2=ataquePJ2))
                sleep(0.2)
                ataquePJ = ataquePJ + ataquePJ2
            att = 2
    if att != 2:
        if(check==1) and (chk==1):ataquePJ=ataquePJ+upgrade
    if att == 1: 
        print(TxtPrint("attacked_tank_message", ataquePJ=ataquePJ, duopj=duopj))
        att = 0
    elif att == 2: att = 0; ataquePJ = ataquePJ + attlist
    else: print(TxtPrint("attacked_message", ataquePJ=ataquePJ))
    vidaE = vidaE - ataquePJ
    totalPJ = totalPJ + ataquePJ
    registroPJ.enqueue(ataquePJ)
    return ataquePJ,vidaE,totalPJ

# 
# VARIABLES DE ATAQUE DE CADA PERSONAJE --
def attackP(Round):
    match Round:
        case 1: ataquePJ = randint(50,300)
        case 2: ataquePJ = randint(100,400)
        case 3: ataquePJ = randint(100,500)
        case 4: ataquePJ = randint(200,600)
        case 5: ataquePJ = randint(200,700)
        case 6: ataquePJ = randint(300,800)
    return ataquePJ

def attackA(Round):
    match Round:
        case 1: ataquePJ = randint(100,500)
        case 2: ataquePJ = randint(300,600)
        case 3: ataquePJ = randint(300,700)
        case 4: ataquePJ = randint(400,800)
        case 5: ataquePJ = randint(400,900)
        case 6: ataquePJ = randint(500,1000)
    return ataquePJ

def attackTan(Round):
    match Round:
        case 1: ataquePJ = randint(50,100)
        case 2: ataquePJ = randint(60,200)
        case 3: ataquePJ = randint(60,300)
        case 4: ataquePJ = randint(80,400)
        case 5: ataquePJ = randint(80,500)
        case 6: ataquePJ = randint(100,600)
    return ataquePJ

def attackTir(Round):
    match Round:
        case 1: ataquePJ = randint(44,104)
        case 2: ataquePJ = randint(104,204)
        case 3: ataquePJ = randint(144,244)
        case 4: ataquePJ = randint(204,304)
        case 5: ataquePJ = randint(244,344)
        case 6: ataquePJ = randint(304,404)
    return ataquePJ

# 
# VOZ PRESENTACIÓN DE CADA PERSONAJE --
def temaS(personaje):
    '''Voz de cada personaje al escojer'''
    match personaje:
        case "Peleador":
            vos = randint(1,5)
            music.ThemeP(vos)
            if vos == 5:sleep(3.5)
            else:sleep(5.5)
        case "Asesino":
            vos = randint(1,5)
            music.ThemeA(vos)
            sleep(4.5)
        case "Tanque":
            vos = randint(1,5)
            music.ThemeTan(vos)
            sleep(3.6)
        case "Tirador":
            vos = randint(1,5)
            music.ThemeTir(vos)
            sleep(3.6)

# 
# HÁBILIDADES ESPECIALES --
def habA(ataquePJ):
    txt1="\nChimei ~ ¥";txt2="      Tekina ~ ¤";txt3="            Kōgeki ~ §";
    for x in range(0,4):
        match x:
            case 0:print(txt1)
            case 1:print(txt2)
            case 2:print(txt3)
            case 3:print("")
        if x!=3: sleep(0.75)
    ataquePJ = ataquePJ * 3
    sleep(1)
    return ataquePJ

def habT(ataquePJ2,check,chk,upgrade,att4,attlist):
    for y in range(1,4):
        ataquePJ2 = attackTir(6)
        if(check==1) and (chk==1):ataquePJ2=ataquePJ2+upgrade
        att4.enqueue(ataquePJ2)
        match y: 
            case 1:
                print(TxtPrint("Second_atk_shooter", numAtaque=att4.first()))
                # attlist = attlist + att4.first()
                # att4.dequeue()
                # sleep(1)
            case 2:
                print(TxtPrint("Third_atk_shooter", numAtaque=att4.first()))
                # attlist = attlist + att4.first()
                # att4.dequeue()
                # sleep(1)
            case 3:
                print(TxtPrint("fourth_atk_shooter", numAtaque=att4.first()))
                # attlist = attlist + att4.first()
                # att4.dequeue()
                # sleep(1)
        attlist = attlist + att4.first()
        att4.dequeue()
        sleep(1.4)
    return attlist

def habP(vidaPJ,money,Round):
    comision = 50
    if vidaPJ>=1000:
        if Round == 6: comision = comision * 3
        money = money + comision
        print(TxtPrint("special_abiliti_fighter", comision=comision))
    return money

# 
# MÉTODO MEJORAS --
def Mejoras(money):
    '''Este método es de las mejoras, que incluye la Catafixia y las opciones de esta'''
    music.mejoras()
    upgrade = 0
    chk = 0
    check = 0
    print(TxtPrint("menu_upgrade", money=money))
    option = leer_entero(TxtPrint("select_menu"))
    match option:
        case 1:
            money,check=compra(money,250,check)
            if check==1: print(TxtPrint("upgrade1_success")); upgrade = 150; chk = 1
        case 2:
            money,check=compra(money,150,check)
            if check==1: print(TxtPrint("upgrade2_success")); upgrade = 250; chk = 2
        case 3:
            money,check=compra(money,500,check)
            if check==1: print(TxtPrint("upgrade3_success")); chk = 3
        case 4:
            print(TxtPrint("loading_catafixia"))
            sleep(1)
            upgrade,chk=(catafixia())
            if chk == -1: check = 0
            else: check = 1
        case 5:
            print(TxtPrint("return_menu"))
        case _:
            print(TxtPrint("invalid_option")); sleep(1); limpiar()
    return upgrade,chk,check,money

def catafixia():
    upgrade = 0
    chk = 0
    caja = [1,2,3]
    y=randint(0,2)
    limpiar()
    lectura(TxtPrint("welcome_catafixia"))
    sleep(0.7)
    lectura(TxtPrint("activate_catafixia"))
    while True:
        limpiar()
        print(TxtPrint("welcome_catafixia"))
        print(TxtPrint("activate_catafixia"))
        sleep(0.1)
        if kb.is_pressed("space"):
            caja = caja[y]
            print(TxtPrint("selected_box", caja=caja))
            break
    caja1,caja2,caja3=(opciones())
    sleep(1)
    print(TxtPrint("show_box"))
    sleep(1)
    match caja:
        case 1:
            print(TxtPrint("buff_message", caja=caja1))
            if(caja1=="Una espada de fuego!! (+500 ataque)"):
                upgrade=500
                chk=1
            elif(caja1=="Una poción bonificadora (+500 hp)"):
                upgrade=500
                chk=2
            elif(caja1=="Un escudo"):
                upgrade=0
                chk=3
        case 2: print(TxtPrint("buff_message", caja=caja2))
        case 3:
            if (caja3=="Mejor suerte para la próxima!"):
                print(TxtPrint("nerf_message", caja=caja3))
                chk=-1
            else:
                print(TxtPrint("buff_message", caja=caja3))
                if(caja3=="Una poción venenosa (-500 hp)"):
                    upgrade=-500
                    chk=2
                elif(caja3=="Una poción debilitante (-250 ataque)"):
                    upgrade=-500
                    chk=1
    sleep(1)
    print(TxtPrint("show_other_boxes"))
    sleep(1)
    print(TxtPrint("content_boxes", caja=1, contenido=caja1))
    sleep(0.5)
    print(TxtPrint("content_boxes", caja=2, contenido=caja2))
    sleep(0.5)
    print(TxtPrint("content_boxes", caja=3, contenido=caja3))
    sleep(2)
    return upgrade,chk

def opciones():
    op1=["Una espada de fuego!! (+500 ataque)","Una poción bonificadora (+500 hp)","Un escudo"]
    op2=["Una ¿cubeta?","Una ¿manguera?","Una ¿Dona?"]
    op3=["Mejor suerte para la próxima!","Una poción venenosa (-500 hp)","Una poción debilitante (-250 ataque)"]
    cajas=Queue()
    for x in range(0,3):
        y = randint(0,2)
        cajas.enqueue(y)
    caja1=op1[cajas.dequeue()]
    caja2=op2[cajas.dequeue()]
    caja3=op3[cajas.dequeue()]
    return caja1,caja2,caja3
