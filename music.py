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
def FondoMusica(disco):
    match disco:
        # case 1:
        #     mixer.music.load()
        case 1:
            mixer.music.load('D:\maxim\Documents\Cosas en general\PASAR RATO\V2\papyrus.wav')
        case 2:
            mixer.music.load('D:\maxim\Documents\Cosas en general\PASAR RATO\V2\determination.wav')
    mixer.music.play()

def GameOver():
    mixer.music.load('D:\maxim\Documents\Cosas en general\PASAR RATO\V2\over.wav')
    mixer.music.play()

def TemaBoss():
    mixer.music.load('D:\maxim\Documents\Cosas en general\PASAR RATO\V2\jefe.wav')
    mixer.music.play()

def Win():
    mixer.music.load('D:\maxim\Documents\Cosas en general\PASAR RATO\V2\win.wav')
    mixer.music.play()

def Bye():
    mixer.music.load('D:\maxim\Documents\Cosas en general\PASAR RATO\V2\hablarC.wav')
    # mixer.music.play()
