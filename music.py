# 
# IMPORTACIÓN MÉTODOS --
from pygame.locals import *
from pygame import mixer

# 
# CONTROLES --
def Play():
    mixer.music.play()

def Stop():
    mixer.music.stop()

def Init():
    mixer.init()

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
    mixer.music.play()

def GameOver():
    mixer.music.load('.\music\over.wav')
    mixer.music.play()

def TemaBoss():
    mixer.music.load('.\music\jefe.wav')
    mixer.music.play()

def Win():
    mixer.music.load('.\music\win.wav')
    mixer.music.play()

def Bye():
    mixer.music.load('.\music\hablarC.wav')

def Menu():
    mixer.music.load('.\music\galaxylife.wav')
    mixer.music.play()

def mejoras():
    mixer.music.load('.\music\mercado.wav')
    mixer.music.play()
