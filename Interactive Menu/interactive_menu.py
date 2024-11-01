from stack_and_queue import Queue as q
import MisFunciones_v2 as m
import keyboard as kb
import time as t

menu2 = q()
y = 0
x = 0
a = input("Valor a: ")
b = input("Valor b: ")
c = input("Valor c: ")
la = int((len(a)/2))
lb = int((len(b)/2))
lc = int((len(c)/2))
f1 = (" "*(la+3))
f2 = (" "*(lb+len(a)+10))
f3 = (" "*(lc+len(a)+len(b)+17))
menu2.enqueue(f"{f1} ↓")
menu2.enqueue(f"{f2} ↓")
menu2.enqueue(f"{f3} ↓")

def left2():
    menu2.enqueue(menu2.dequeue())

def right2():
    y = menu2.last()
    while (y!=menu2.first()):
        menu2.enqueue(menu2.dequeue())

def dinamicMenu(a,b,c):
    while True:
        print(menu2.first())
        print("",("-"*(len(a)+6)),("-"*(len(b)+6)),("-"*(len(c)+6)))
        print(" | ",a," | | ",b," | | ",c," | ")
        print("",("-"*(len(a)+6)),("-"*(len(b)+6)),("-"*(len(c)+6)))
        t.sleep(0.05)
        if kb.is_pressed("left"):
            x = 1
            right2()
        if kb.is_pressed("right"):
            x = 1
            left2()
        if kb.is_pressed("esc"):
            break
        if kb.is_pressed("enter"):
            if (menu2.first()==(f"{f1} ↓")):
                m.limpiar()
                print(f"Entraste al botón {a}")
                t.sleep(2)
            if (menu2.first()==(f"{f2} ↓")):
                m.limpiar()
                print(f"Entraste al botón {b}")
                t.sleep(2)
            if (menu2.first()==(f"{f3} ↓")):
                m.limpiar()
                print(f"Entraste al botón {c}")
                t.sleep(2)
        m.limpiar()

dinamicMenu(a,b,c)
# 
# VERSIÓN 1 - No recomendada
# menu1.enqueue(" A ")
# menu1.enqueue(" B ")
# menu1.enqueue(" C ")
# def left1():
#     menu1.enqueue(menu1.dequeue())
# def right1():
#     y = menu1.last()
#     while (y!=menu1.first()):
#         menu1.enqueue(menu1.dequeue())
# while True:
#     print("   ↓")
#     print(" -----  -----  -----")
#     print(menu1.all_items())
#     print(" -----  -----  -----")
#     t.sleep(0.1)
#     if kb.is_pressed("left"):
#         left1()
#     if kb.is_pressed("right"):
#         right1()
#     if kb.is_pressed("esc"):
#         break
#     if kb.is_pressed("enter"):
#         match menu1.first():
#             case " A ":
#                 os.system('cls')
#                 print("Entraste al botón A")
#                 t.sleep(2)
#             case " B ":
#                 os.system('cls')
#                 print("Entraste al botón B")
#                 t.sleep(2)
#             case " C ":
#                 os.system('cls')
#                 print("Entraste al botón C")
#                 t.sleep(2)
#     os.system('cls')
