# Ejercicio 1. Uso de colores

# b) En segundo lugar, añade la funcionalidad necesaria para gestionar el
# encendido y apagado de, al menos, otros cinco colores, p. ej.: magenta,
# amarillo, cyan, blanco, etc.

import time, sys
import RPi.GPIO as GPIO

rojoPin = 36
azulPin = 38
verdePin = 40

def encender(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    
def apagar(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    
def encenderMagenta():
    encender(rojoPin)
    encender(azulPin)
    apagar(verdePin)
    
def apagarMagenta():
    apagar(rojoPin)
    apagar(azulPin)

def encenderAmarillo():
    encender(rojoPin)
    encender(verdePin)
    apagar(azulPin)
    
def apagarAmarillo():
    apagar(rojoPin)
    apagar(verdePin)

def encenderCyan():
    encender(verdePin)
    encender(azulPin)
    apagar(rojoPin)
    
def apagarCyan():
    apagar(verdePin)
    apagar(azulPin)

def encenderBlanco():
    encender(rojoPin)
    encender(azulPin)
    encender(verdePin)
    
def apagarBlanco():
    apagar(rojoPin)
    apagar(azulPin)
    apagar(verdePin)

def main():
    while True:
        encenderMagenta()
        time.sleep(1)
        apagarMagenta()
        time.sleep(1)
        encenderAmarillo()
        time.sleep(1)
        apagarAmarillo()
        time.sleep(1)
        encenderCyan()
        time.sleep(1)
        apagarCyan()
        time.sleep(1)
        encenderBlanco()
        time.sleep(1)
        apagarBlanco()
        time.sleep(1)
    return

if __name__ == '__main__':
    main()
