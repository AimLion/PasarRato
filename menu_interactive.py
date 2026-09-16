from translation import TxtPrint
from funciones import *
import keyboard as kb
from time import sleep
import text as txt
from money import compra

menu = Queue()

def description(pj,descrip):
    match pj:
        case 'Peleador':
            descrip = TxtPrint("description_fighter")
            vidaPj=2500
        case 'Asesino':
            descrip = TxtPrint("description_assassin")
            vidaPj=1500
        case 'Tanque':
            descrip = TxtPrint("description_tank")
            vidaPj=4500
        case 'Tirador':
            descrip = TxtPrint("description_shooter")
            vidaPj=2000
    return descrip,vidaPj

def selection(pj,confirm,selec):
    descrip=""
    descrip,vidaPJ=description(pj,descrip)
    while True:
        selec=leer_entero(TxtPrint("character_info", namePj=pj, descrip=descrip))
        match selec:
            case 1:
                confirm = pj
                print(TxtPrint("character_selected", namePj=pj))
                txt.temaS(pj)
                break
            case 2:
                confirm = ""
                sleep(0.5)
                break
            case _:
                limpiar()
    return confirm,vidaPJ

def left():
    menu.enqueue(menu.dequeue())

def right():
    y = menu.last()
    while (y!=menu.first()):
        menu.enqueue(menu.dequeue())

def space(letra,verify):
    '''Determina los espacios para los guiones de compra y venta'''
    space=" "*int((len(letra)-len(verify))/2)
    space2 = " "*int((len(letra)-len(verify))%2)
    if space2 == 0: space2 = space
    else: space2 = space2 + space
    op=f"{space2}{verify}{space}"
    return op

def verifV(texto,v,txt,pr1):
    '''Verifica si se ingresa el icono de vendido o el precio'''
    match v:
        case 0: v=space(texto,txt)
        case 1: v=space(texto,pr1)
    return v

def dinamicMenu(a,b,c,d,f1,f2,f3,f4,confirm,money,pr1,pr2,pr3,pr4,v2,v3,v4):
    '''Menu de Elección de Personaje'''
    op1=space(a,pr1); txt2=f"${pr2}"; txt3=f"${pr3}"; txt4=f"${pr4}"; 
    op2=verifV(b,v2,txt2,pr1); op3=verifV(c,v3,txt3,pr1); op4=verifV(d,v4,txt4,pr1); check=0;
    while True:
        print(TxtPrint("menu_characters"))
        print(menu.first())
        print("",("-"*(len(a)+6)),("-"*(len(b)+6)),("-"*(len(c)+6)),("-"*(len(d)+6)))
        print(" | ",a," | | ",b," | | ",c," | | ",d," | ")
        print(" | ",op1," | | ",op2," | | ",op3," | | ",op4," | ")
        print("",("-"*(len(a)+6)),("-"*(len(b)+6)),("-"*(len(c)+6)),("-"*(len(d)+6)))
        print(TxtPrint("coins_available", money=money))
        print(TxtPrint("instructions_menu"))
        tecla = enter("")
        if kb.is_pressed("left"):
            right()
            sleep(0.1)
        elif kb.is_pressed("right"):
            left()
            sleep(0.1)
        elif kb.is_pressed("tab"):
            confirm = "Peleador";vidaPJ=0
            break
        elif tecla == b'\r':
            if (menu.first()==(f"{f1} ↓")):
                print(TxtPrint("loading_character"))
                sleep(1); limpiar()
                confirm,vidaPJ = selection(a,confirm,0)
            elif (menu.first()==(f"{f2} ↓")):
                if v2==1:
                    print(TxtPrint("loading_character"))
                    sleep(1); limpiar()
                    confirm,vidaPJ = selection(b,confirm,0)
                else:
                    money,check = compra(money,pr2,check)
                    match check:
                        case 0: sleep(1)
                        case 1: v2 = 1; op2 = space(b,pr1)
            elif (menu.first()==(f"{f3} ↓")):
                if v3==1:
                    print(TxtPrint("loading_character"))
                    sleep(1); limpiar()
                    confirm,vidaPJ = selection(c,confirm,0)
                else:
                    money,check = compra(money,pr3,check);
                    match check:
                        case 0: sleep(1)
                        case 1: v3 = 1; op3 = space(c,pr1)
            elif (menu.first()==(f"{f4} ↓")):
                if v4==1:
                    print(TxtPrint("loading_character"))
                    sleep(1); limpiar()
                    confirm,vidaPJ = selection(d,confirm,0)
                else:
                    money,check = compra(money,pr4,check);
                    match check:
                        case 0: sleep(1)
                        case 1: v4 = 1; op4 = space(d,pr1)
        if confirm != "": break
        else: limpiar()
    return confirm,vidaPJ,money,v2,v3,v4

def interactiveMenu(op1,op2,op3,op4,pr1,precio,money,ventas):
    '''Declaración de todas las variables necesarias para el menu de personajes'''
    vidaPj = 0;   sleep(1);   confirm = ""; limpiar()
    a = str(op1); b = str(op2); c = str(op3); d = str(op4)
    la = int((len(a)/2)); lb = int((len(b)/2))
    lc = int((len(c)/2)); ld = int((len(d)/2))
    f1 = (" "*(la+3)); f2 = (" "*(lb+len(a)+10))
    f3 = (" "*(lc+len(a)+len(b)+17)); f4 = (" "*(ld+len(a)+len(b)+len(c)+24))
    menu.enqueue(f"{f1} ↓"); menu.enqueue(f"{f2} ↓")
    menu.enqueue(f"{f3} ↓"); menu.enqueue(f"{f4} ↓")
    v2=ventas[0]; v3=ventas[1]; v4=ventas[2]

    confirm,vidaPj,money,v2,v3,v4=dinamicMenu(a,b,c,d,f1,f2,f3,f4,confirm,money,pr1,precio,precio,precio,v2,v3,v4)
    ventas = v2,v3,v4
    return confirm,vidaPj,money,ventas
