# 
# IMPORTACIÓN MÉTODOS --
import pygame.mixer as mixer

# 
# CONTROLES --
def Play():
    mixer.music.play()

def Stop():
    mixer.music.stop()

def Init():
    mixer.init()

def Vup():
    mixer.music.set_volume(1)

# 
# VOCES --
def Bye():
    mixer.music.load('.\music\hablarC.wav')
    mixer.music.set_volume(0.3)

def ThemeP(vos):
    match vos:
        case 1:
            mixer.music.load('.\music\sett\F1.wav')
        case 2:
            mixer.music.load('.\music\sett\F2.wav')
        case 3:
            mixer.music.load('.\music\sett\F3.wav')
        case 4:
            mixer.music.load('.\music\sett\F4.wav')
        case 5:
            mixer.music.load('.\music\sett\F5.wav')
    mixer.music.play()

def ThemeA(vos):
    match vos:
        case 1:
            mixer.music.load('.\music\zed\F1.wav')
        case 2:
            mixer.music.load('.\music\zed\F2.wav')
        case 3:
            mixer.music.load('.\music\zed\F3.wav')
        case 4:
            mixer.music.load('.\music\zed\F4.wav')
        case 5:
            mixer.music.load('.\music\zed\F5.wav')
        case 6:
            sound = mixer.Sound('.\music\zed\FR.wav')
            sound.play()
            sound.set_volume(0.5)
    if(vos!=6):
        mixer.music.play()
        mixer.music.set_volume(0.3)
    else:
        vos = vos

def ThemeTan(vos):
    match vos:
        case 1:
            mixer.music.load('.\music\Braum\F1.wav')
        case 2:
            mixer.music.load('.\music\Braum\F2.wav')
        case 3:
            mixer.music.load('.\music\Braum\F3.wav')
        case 4:
            mixer.music.load('.\music\Braum\F4.wav')
        case 5:
            mixer.music.load('.\music\Braum\F5.wav')
    mixer.music.play()
    mixer.music.set_volume(0.3)

def ThemeTir(vos):
    match vos:
        case 1:
            mixer.music.load('.\music\Jhin\F1.wav')
        case 2:
            mixer.music.load('.\music\Jhin\F2.wav')
        case 3:
            mixer.music.load('.\music\Jhin\F3.wav')
        case 4:
            mixer.music.load('.\music\Jhin\F4.wav')
        case 5:
            mixer.music.load('.\music\Jhin\F5.wav')
        case 6:
            sound = mixer.Sound('.\music\Jhin\FR2.wav')
            sound.play()
            sound.set_volume(0.5)
        case 7:
            mixer.music.load('.\music\Jhin\FR.wav')
    if(vos!=6):
        mixer.music.play()
        mixer.music.set_volume(0.2)
    else:
        vos = vos

# 
# TEMAS MUSICALES --
def FondoMusicaPelea(disco):
    match disco:
        case 1:
            mixer.music.load('.\music\papyrus.wav')
        case 2:
            mixer.music.load('.\music\determination.wav')
        case 3:
            mixer.music.load('.\music\Rutas.wav')
    mixer.music.play(-1)
    if disco==2: mixer.music.set_volume(0.1)
    else: mixer.music.set_volume(0.2)

def GameOver():
    mixer.music.load('.\music\over.wav')
    mixer.music.play()

def TemaBoss():
    mixer.music.load('.\music\jefe.wav')
    mixer.music.play()

def Win():
    mixer.music.load('.\music\win.wav')
    mixer.music.play()

def Menu():
    mixer.music.load('.\music\galaxylife.wav')
    mixer.music.play()

def mejoras():
    mixer.music.load('.\music\mercado.wav')
    mixer.music.play()

def seleccion():
    mixer.music.load('.\music\seleccion.wav')
    mixer.music.play()
    mixer.music.set_volume(0.5)
