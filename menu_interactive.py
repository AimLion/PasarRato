from funciones import *
import keyboard as kb
import time as t
import text as txt
from money import compra

menu = Queue()

def description(pj,descrip):
    match pj:
        case 'Peleador':
            descrip = '\n- Este peleador a estado en infinidad de combates, la experiencia que a\n  obtenido más la fuerza lo vuelven el peleador más potente de toda la arena.\n\nDatos de Batalla:\n - Vida Maxima: 2500\n - Daño Promedio: 600 (+- 100)\n - Habilidad Especial: "Mi comisión!"\n   Si al final de cada ronda queda con más de 1000 de vida, obtendrá\n   +$50 de monedas y 150 si vence al jefe con la misma condición.'
            vidaPj=2500
        case 'Asesino':
            descrip = '\n- Este feroz asesino es sigiloso cual noche y puede eliminar a sus enemigos sin que \n lleguen a sentir su presencia. Un golpe certero y no se levantarán tus contrincantes\n\nDatos de Batalla:\n - Vida Maxima: 1500\n - Daño Promedio: 750 (+- 100)\n - Habilidad Especial: "Ataque Letal"\n   Después de 2 turnos contra el jefe, se esconde para lanzar un ataque con el daño triplicado.'
            vidaPj=1500
        case 'Tanque':
            descrip = '\n- Este robusto tanque es como ningún otro, si bien no puede aplicar mucho daño,lo fuerte en el es \n  su aguante y espiritu por resistir. Llevalo a la arena y solo te harán cosquillas tus enemigos\n\nDatos de Batalla:\n - Vida Maxima: 4500\n - Daño Promedio: 300 (+- 100)\n - Habilidad Especial: "Golpe Duo"\n   Después de 4 turnos contra el jefe, llama a un compañero al azar para atacar juntos.'
            vidaPj=4500
        case 'Tirador':
            descrip = '\n- Sin duda alguna, no hay nadie como este tirador. Sea en lluvia o tormenta, nunca dejaría ir a \n  sus enemigos con vida. Puedes llevarlo a la arena y cada tiro será una victoria a la lista.\n\nDatos de Batalla:\n - Vida Maxima: 2000\n - Daño Promedio: 400 (+- 100) x Disparo\n - Habilidad Especial: "Tic tac"\n   Ataca dos veces por turno, y en el turno 4 contra el jefe, ataca cuatro veces seguidas.'
            vidaPj=2000
    return descrip,vidaPj

def selection(pj,confirm,selec):
    descrip=""
    descrip,vidaPJ=description(pj,descrip)
    while True:
        print(f"Personaje - {pj}")
        print("\nInformación General:\n",descrip)
        print("\nOpciones:")
        selec=leer_entero("1) Seleccionar\n2) Regresar\n\nSelecciona: ")
        match selec:
            case 1:
                confirm = pj
                print(f"\nElegiste al {pj}")
                txt.temaS(pj)
                break
            case 2:
                confirm = ""
                t.sleep(0.5)
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

def dinamicMenu(a,b,c,d,title,f1,f2,f3,f4,confirm,money,pr1,pr2,pr3,pr4,v2,v3,v4):
    '''Menu de Elección de Personaje'''
    op1=space(a,pr1); txt2=f"${pr2}"; txt3=f"${pr3}"; txt4=f"${pr4}"; 
    op2=verifV(b,v2,txt2,pr1); op3=verifV(c,v3,txt3,pr1); op4=verifV(d,v4,txt4,pr1); check=0;
    while True:
        print(f"Menu de Selección de {title}\n#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
        print(f"\nEscoje tu {title}")
        print(menu.first())
        print("",("-"*(len(a)+6)),("-"*(len(b)+6)),("-"*(len(c)+6)),("-"*(len(d)+6)))
        print(" | ",a," | | ",b," | | ",c," | | ",d," | ")
        print(" | ",op1," | | ",op2," | | ",op3," | | ",op4," | ")
        print("",("-"*(len(a)+6)),("-"*(len(b)+6)),("-"*(len(c)+6)),("-"*(len(d)+6)))
        print(f"\nMonedas Disponibles: {money}")
        print("\n-) Pulsa enter para elegir/comprar\n-) Pulsa tab para regresar al menú")
        tecla = enter("")
        if kb.is_pressed("left"):
            right()
            t.sleep(0.02)
        elif kb.is_pressed("right"):
            left()
            t.sleep(0.02)
        elif kb.is_pressed("tab"):
            confirm = "Peleador";vidaPJ=0
            break
        elif tecla[0] == b'\r':
            if (menu.first()==(f"{f1} ↓")):
                print(f"\nCargando {title} . . .")
                t.sleep(1); limpiar()
                confirm,vidaPJ = selection(a,confirm,0)
            elif (menu.first()==(f"{f2} ↓")):
                if v2==1:
                    print(f"\nCargando {title} . . .")
                    t.sleep(1); limpiar()
                    confirm,vidaPJ = selection(b,confirm,0)
                else:
                    money,check = compra(money,pr2,check)
                    match check:
                        case 0: t.sleep(1)
                        case 1: v2 = 1; op2 = space(b,pr1)
            elif (menu.first()==(f"{f3} ↓")):
                if v3==1:
                    print(f"\nCargando {title} . . .")
                    t.sleep(1); limpiar()
                    confirm,vidaPJ = selection(c,confirm,0)
                else:
                    money,check = compra(money,pr3,check);
                    match check:
                        case 0: t.sleep(1)
                        case 1: v3 = 1; op3 = space(c,pr1)
            elif (menu.first()==(f"{f4} ↓")):
                if v4==1:
                    print(f"\nCargando {title} . . .")
                    t.sleep(1); limpiar()
                    confirm,vidaPJ = selection(d,confirm,0)
                else:
                    money,check = compra(money,pr4,check);
                    match check:
                        case 0: t.sleep(1)
                        case 1: v4 = 1; op4 = space(d,pr1)
        if confirm != "": break
        else: limpiar()
    return confirm,vidaPJ,money,v2,v3,v4

def interactiveMenu(title,op1,op2,op3,op4,pr1,precio,money,ventas):
    '''Declaración de todas las variables necesarias para el menu de personajes'''
    vidaPj = 0;   t.sleep(1);   confirm = ""; limpiar()
    a = str(op1); b = str(op2); c = str(op3); d = str(op4)
    la = int((len(a)/2)); lb = int((len(b)/2))
    lc = int((len(c)/2)); ld = int((len(d)/2))
    f1 = (" "*(la+3)); f2 = (" "*(lb+len(a)+10))
    f3 = (" "*(lc+len(a)+len(b)+17)); f4 = (" "*(ld+len(a)+len(b)+len(c)+24))
    menu.enqueue(f"{f1} ↓"); menu.enqueue(f"{f2} ↓")
    menu.enqueue(f"{f3} ↓"); menu.enqueue(f"{f4} ↓")
    v2=ventas[0]; v3=ventas[1]; v4=ventas[2]

    confirm,vidaPj,money,v2,v3,v4=dinamicMenu(a,b,c,d,title,f1,f2,f3,f4,confirm,money,pr1,precio,precio,precio,v2,v3,v4)
    ventas = v2,v3,v4
    return confirm,vidaPj,money,ventas
