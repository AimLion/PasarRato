from time import sleep
import music as m

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

def despedida(despedida):
    print("\n")
    m.Bye()
    txt=despedida
    t1=""
    for y in range(0,len(txt)):
        t1 = t1 + txt[y]
        m.Play()
        print(t1, end="\r")
        sleep(0.07)
        if (txt[y] == " "):
            sleep(0.7)
            m.Stop()

def resultados(registroPJ,totalPJ,ApromPJ,ApromE,totalE,registroE):
    print(f"\nCantidad de daño propio: ",registroPJ.all_items()," Total → ",totalPJ)
    print(f"Cantidad de daño del enemigo: ",registroE.all_items()," Total → ",totalE)
    print(f"\nTu daño promedio: ",ApromPJ)
    print(f"Su daño promedio: ",ApromE)
