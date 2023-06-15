# Ejercicio 1. Uso de colores

# a) En primer lugar, modifica convenientemente el programa para que 
# pueda gestionar el encendido y apagado de los tres colores primarios.

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
    
def encenderRojo():
    encender(rojoPin)
    apagar(azulPin)
    apagar(verdePin)
    
def apagarRojo():
    apagar(rojoPin)

def encenderAzul():
    encender(azulPin)
    apagar(rojoPin)
    apagar(verdePin)
    
def apagarAzul():
    apagar(azulPin)

def encenderVerde():
    encender(verdePin)
    apagar(azulPin)
    apagar(rojoPin)
    
def apagarVerde():
    apagar(verdePin)

def main():    
    while True:
        encenderRojo()
        time.sleep(1)
        apagarRojo()
        time.sleep(1)
        encenderAzul()
        time.sleep(1)
        apagarAzul()
        time.sleep(1)
        encenderVerde()
        time.sleep(1)
        apagarVerde()
        time.sleep(1)
    return

if __name__ == '__main__':
    main()


