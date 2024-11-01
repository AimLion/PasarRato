# 
# IMPORTACIÓN MÉTODOS --
from funciones import *
from random import randint
from money import compra
from time import sleep
import keyboard as kb
import music as m

m.Init()
# 
# TEXTOS A IMPRIMIR --
def jefe():
    '''Método enfocado en la presentación del Jefe'''
    txt0 = "\nAlgo pasa . . ."
    txt1 = "\nEste nivel no debería existir . . ."
    txt2 = "\n-Sientes corrientes de viento rodeandote- . . ."
    txt3 = "\nLos enemigos no están . . ."
    txt4 = "\nA donde se han ido? . . ."
    txt5 = "\n-Una voz se escucha al fondo- . . ."
    txt6 = "\nTodos se han reunido contra ti . . ."
    txt7 = "\nEsta es la batalla final . . ."

    for x in range(0,8):
        match x:
            case 0: sleep(0.1);print(txt0)
            case 1: print(txt1)
            case 2: print(txt2)
            case 3: print(txt3); sleep(0.5)
            case 4: print(txt4)
            case 5: print(txt5)
            case 6: print(txt6)
            case 7: print(txt7)
        if (x != 7): sleep(2)
        else: sleep(1)

def status(vidaPJ,vidaE,Round,z):
    '''Muestra los Resultados al Final de cada Ronda parte 1'''
    if (vidaE <= 0) and (vidaPJ>0): print(F"\nGran combate!! Has sobrevivido ",z," turnos con ",vidaPJ," de vida")
    elif(vidaE<=0) and (vidaPJ<=0):
        print(f"\nA sido un gran combate, se declara un empate.")
        print(f"Llegaste hasta el nivel: ",Round)
    else:
        print(f"\nBuen intento, ha sobrevivido el enemigo con ",vidaE," de vida")
        print(f"Llegaste hasta el nivel: ",Round)

def resultados(registroPJ,totalPJ,ApromPJ,ApromE,totalE,registroE):
    '''Muestra los Resultados al Final de cada Ronda parte 2'''
    print(f"\nCantidad de daño propio: ",registroPJ.all_items()," Total → ",totalPJ)
    print(f"Cantidad de daño del enemigo: ",registroE.all_items()," Total → ",totalE)
    print(f"\nTu daño promedio: ",ApromPJ)
    print(f"Su daño promedio: ",ApromE)

def lectura(lectura):
    '''Método de lecuta de Sans'''
    m.Bye()
    txt=lectura
    t1=""
    for y in range(0,len(txt)):
        t1 = t1 + txt[y]
        m.Play()
        print(t1, end="\r")
        sleep(0.07)
        if (txt[y] == " "):
            m.Stop()
            sleep(0.5)

def attackJ(vidaPJ,totalE,ataqueE,registroE):
    '''Método de impresión y ataque del Jefe'''
    vidaPJ = vidaPJ - ataqueE
    totalE = totalE + ataqueE
    registroE.enqueue(ataqueE)
    print(f"Te a bajado {ataqueE} de vida")
    print(" ")
    return vidaPJ,totalE

def oneshot(registroE,totalE,money):
    '''Oneshot, simplemente'''
    if(totalE==0):
        print(f"\nHAS ONESHOTEADO AL ENEMIGO!! +$100")
        money = money + 100
        ApromE = 0;registroE.enqueue(0)
    else: ApromE = totalE / registroE.size()
    return ApromE,money

def level(Round):
    '''Imprime el Mapa del Juego'''
    lv = Queue()
    lv.enqueue("Ø     O--O |\n|  \   /   | |\n|   \ /    | |\n|    O     O");
    lv.enqueue("O     O--O |\n|  \   /   | |\n|   \ /    | |\n|    Ø     O");
    lv.enqueue("O     Ø--O |\n|  \   /   | |\n|   \ /    | |\n|    O     O")
    lv.enqueue("O     O--Ø |\n|  \   /   | |\n|   \ /    | |\n|    O     O");
    lv.enqueue("O     O--O |\n|  \   /   | |\n|   \ /    | |\n|    O     Ø")
    if Round>1:
        for x in range(1,(Round)): lv.enqueue(lv.dequeue())
    print("\nMapa de rondas")
    print("--------------")
    if Round==6: print("| O     O--O |\n|  \   /   | |\n|   \ /    | |\n|    O     O-|-Ø")
    else: print("|",lv.first(),"|")
    print("--------------")
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
                print(f'"Ataque Letal" del {personaje}!!')
                sleep(0.75)
                ataquePJ = habA(ataquePJ)
        case "Tanque":
            ataquePJ=attackTan(Round)
            if Round == 6 and z == 4 and vidaPJ>=3000:
                print(f'"Golpe Duo" del {personaje}!!\n')
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
                print(f'Tic . . .Tac . . . del {personaje}!!')
                sleep(0.75)
                m.ThemeTir(6)
                sleep(0.4)
                print(f"\nPrimer Disparo de {ataquePJ} !")
                sleep(1)
                attlist=habT(ataquePJ2,check,chk,upgrade,att4,attlist)
            else:
                ataquePJ2=attackTir(Round)
                if(check==1) and (chk==1):ataquePJ=ataquePJ+upgrade;ataquePJ2=ataquePJ2+upgrade
                print(f"Le has bajado {ataquePJ} y {ataquePJ2} de vida al enemigo")
                sleep(0.2)
                ataquePJ = ataquePJ + ataquePJ2
            att = 2
    if att != 2:
        if(check==1) and (chk==1):ataquePJ=ataquePJ+upgrade
    if att == 1: 
        print(f"Tu y el {duopj} le han bajado {ataquePJ} de vida al enemigo!!")
        att = 0
    elif att == 2: att = 0; ataquePJ = ataquePJ + attlist
    else: print(f"Le has bajado {ataquePJ} de vida al enemigo")
    vidaE = vidaE - ataquePJ
    totalPJ = totalPJ + ataquePJ
    registroPJ.enqueue(ataquePJ)
    return ataquePJ,vidaE,totalPJ

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

def temaS(personaje):
    '''Voz de cada personaje al escojer'''
    match personaje:
        case "Peleador":
            vos = randint(1,5)
            m.ThemeP(vos)
            if vos == 5:sleep(3.5)
            else:sleep(5.5)
        case "Asesino":
            vos = randint(1,5)
            m.ThemeA(vos)
            sleep(4.5)
        case "Tanque":
            vos = randint(1,5)
            m.ThemeTan(vos)
            sleep(3.6)
        case "Tirador":
            vos = randint(1,5)
            m.ThemeTir(vos)
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
    return ataquePJ

def habT(ataquePJ2,check,chk,upgrade,att4,attlist):
    for y in range(1,4):
        ataquePJ2 = attackTir(6)
        if(check==1) and (chk==1):ataquePJ2=ataquePJ2+upgrade
        att4.enqueue(ataquePJ2)
        match y:
            case 1:
                print(f"Segundo Disparo de {att4.first()} !!")
                attlist = attlist + att4.first()
                att4.dequeue()
                sleep(1)
            case 2:
                print(f"Tercer Disparo de {att4.first()} !!!")
                attlist = attlist + att4.first()
                att4.dequeue()
                sleep(1)
            case 3:
                print(f"Cuarto Disparo de {att4.first()} !!!")
                attlist = attlist + att4.first()
                att4.dequeue()
                sleep(1)
        sleep(0.4)
    return attlist

def habP(vidaPJ,money,Round):
    if vidaPJ>=1000:
        money = money + 50
        print('Has ganado +$50 por "Mi comisión!"')
    elif Round == 6 and vidaPJ>=1000:
        money = money + 150
        print('Has ganado +$150 por "Mi comisión!"')
    return money

# 
# MÉTODO MEJORAS --
def Mejoras(money):
    '''Este método es de las mejoras, que incluye la Catafixia y las opciones de esta'''
    m.mejoras()
    upgrade = 0
    chk = 0
    check = 0
    print("Menu de Mejoras")
    print("-#-#-#-#-#-#-#-")
    print(f"\nMonedas: ${money}")
    print("\nOpciones:")
    print("1) Aumentar Ataque +150 - Precio $250")
    print("2) Aumentar Vida +250 - Precio $150")
    print("3) Bloquear un Ataque del Jefe - Precio $500")
    print("4) Probar la Catafixia")
    print("5) Regresar al Menu")
    option = leer_entero("\nSeleccione su mejora: ")
    match option:
        case 1:
            money,check=compra(money,250,check)
            if check==1: print("\nSe a aumentado tu ataque +150"); upgrade = 150; chk = 1
        case 2:
            money,check=compra(money,150,check)
            if check==1: print("\nSe a aumentado tu vida +250"); upgrade = 250; chk = 2
        case 3:
            money,check=compra(money,500,check)
            if check==1: print("\nAhora puedes bloquear 1 ataque del Jefe"); chk = 3
        case 4:
            print("\nCargando Catafixia . . .")
            sleep(1)
            upgrade,chk=(catafixia())
            if chk == -1: check = 0
            else: check = 1
        case 5:
            print("\nRegresando al menu . . .")
        case _:
            print("Opción no válida")
            limpiar()
    return upgrade,chk,check,money

def catafixia():
    upgrade = 0
    chk = 0
    limpiar()
    lectura("Bienvenido a la Catafixia!")
    print("\n")
    sleep(0.7)
    lectura("Pulsa espacio para sacar tu ficha")
    while True:
        limpiar()
        print("Bienvenido a la Catafixia!")
        print("\nPulsa espacio para sacar tu ficha")
        caja = [1,2,3]
        y=randint(0,2)
        sleep(0.05)
        if kb.is_pressed("space"):
            print(f"\nTomaste la ficha número: {caja[y]}")
            caja = caja[y]
            break
    caja1,caja2,caja3=(opciones())
    sleep(1)
    print(f"\n¿Qué has ganado? . . .")
    sleep(1)
    match caja:
        case 1:
            print(f"\nHas ganado {caja1}")
            if(caja1=="Una espada de fuego!! (+500 ataque)"):
                upgrade=500
                chk=1
            elif(caja1=="Una poción bonificadora (+500 hp)"):
                upgrade=500
                chk=2
            elif(caja1=="Un escudo"):
                upgrade=0
                chk=3
        case 2: print(f"\nHas ganado {caja2}")
        case 3:
            if (caja3=="Mejor suerte para la próxima!"):
                print(f"\nLastima, {caja3}")
                chk=-1
            else:
                print(f"\nHas ganado {caja3}")
                if(caja3=="Una poción venenosa (-500 hp)"):
                    upgrade=-500
                    chk=2
                elif(caja3=="Una poción debilitante (-250 ataque)"):
                    upgrade=-500
                    chk=1
    sleep(1)
    print("\n¿Que había en las demás cajas?")
    sleep(1)
    print(f"\nEn caja 1 hay: {caja1}")
    sleep(0.5)
    print(f"En caja 2 hay: {caja2}")
    sleep(0.5)
    print(f"En caja 3 hay: {caja3}")
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
