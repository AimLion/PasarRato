# 
# IMPORTACIÓN MÉTODOS --
from time import sleep
from random import randint
from MisFunciones_v2 import *
import music as m
import keyboard as kb
from stack_and_queue import Queue

# 
# TEXTOS A IMPRIMIR --
def jefe():
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
            case 0:
                print(txt0)
            case 1:
                print(txt1)
            case 2:
                print(txt2)
            case 3:
                print(txt3)
                sleep(0.5)
            case 4:
                print(txt4)
            case 5:
                print(txt5)
            case 6:
                print(txt6)
            case 7:
                print(txt7)
        if (x != 7):
            sleep(2)
        else:
            sleep(1)

def status(vidaPJ,vidaE,Round,z):
    if (vidaE <= 0) and (vidaPJ>0):
        print(F"\nGran combate!! Has sobrevivido ",z," turnos con ",vidaPJ," de vida")
    elif(vidaE<=0) and (vidaPJ<=0):
        print(f"\nA sido un gran combate, se declara un empate.")
        print(f"Llegaste hasta el nivel: ",Round)
    else:
        print(f"\nBuen intento, ha sobrevivido el enemigo con ",vidaE," de vida")
        print(f"Llegaste hasta el nivel: ",Round)

def resultados(registroPJ,totalPJ,ApromPJ,ApromE,totalE,registroE):
    print(f"\nCantidad de daño propio: ",registroPJ.all_items()," Total → ",totalPJ)
    print(f"Cantidad de daño del enemigo: ",registroE.all_items()," Total → ",totalE)
    print(f"\nTu daño promedio: ",ApromPJ)
    print(f"Su daño promedio: ",ApromE)

def lectura(lectura):
    # print("\n")
    m.Bye()
    txt=lectura
    t1=""
    for y in range(0,len(txt)):
        t1 = t1 + txt[y]
        m.Play()
        print(t1, end="\r")
        sleep(0.06)
        if (txt[y] == " "):
            sleep(0.7)
            m.Stop()

def attackJ(vidaPJ,totalE,ataqueE,registroE):
    vidaPJ = vidaPJ - ataqueE
    totalE = totalE + ataqueE
    registroE.enqueue(ataqueE)
    print(F"\nTe a bajado {ataqueE} de vida")
    return vidaPJ,totalE

# 
# DECLARACIÓN DE VARIABLES --
def vidaEXround(Round):
    match Round:
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
    return vidaE

def attack(Round,check,chk,upgrade,vidaE,totalPJ,registroPJ):
    match Round:
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
    if(check==1) and (chk==1):ataquePJ=ataquePJ+upgrade
    vidaE = vidaE - ataquePJ
    print(f"\nLe has bajado ", ataquePJ, " de vida")
    totalPJ = totalPJ + ataquePJ
    registroPJ.enqueue(ataquePJ)
    return ataquePJ,vidaE,totalPJ

# 
# MÉTODO MEJORAS --
def Mejoras():
    m.mejoras()
    print("Menu de Mejoras")
    print("-#-#-#-#-#-#-#-")
    print("\n1) Aumentar Ataque +150")
    print("2) Aumentar Vida +250")
    print("3) Bloquear un Ataque del Jefe")
    print("4) Probar la Catafixia")
    print("5) Regresar al Menu")
    option = leer_entero("\nSeleccione su mejora: ")
    match option:
        case 1:
            print("\nSe a aumentado tu ataque +150")
            upgrade = 150
            chk = 1
            check = 1
        case 2:
            print("\nSe a aumentado tu vida +250")
            upgrade = 250
            chk = 2
            check = 1
        case 3:
            print("\nAhora puedes bloquear 1 ataque del Jefe")
            upgrade = 0
            chk = 3
            check = 1
        case 4:
            print("\nCargando Catafixia . . .")
            sleep(1)
            upgrade,chk=(catafixia())
            if (upgrade == 0) and (chk == 0):
                check = 0
            else:
                check = 1
        case 5:
            print("\nRegresando al menu . . .")
            upgrade = 0
            chk = 0
            check = 0
    return upgrade,chk,check

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
        case 2:
            print(f"\nHas ganado {caja2}")
            upgrade=0
            chk=0
        case 3:
            if (caja3=="Mejor suerte para la próxima!"):
                print(f"\nLastima, {caja3}") 
                upgrade=0
                chk=0
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
