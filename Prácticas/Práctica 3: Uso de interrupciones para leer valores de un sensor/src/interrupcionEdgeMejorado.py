# Ejercicio 2

# Rediseña el esquema de conexión, así como la implementación de los tres códigos facilitados para dar 
# soporte a dos botones que a su vez operan sobre dos LEDs de forma independiente. Así, al pulsar uno de los
# botones, se encenderá un led rojo (y se apagará al soltar dicho botón); y, al pulsar el otro botón, lo 
# mismo pero con el otro LED, que será verde.
# Recuerda que deberás ofrecer esa funcionalidad bajo las tres implementaciones que se han expuesto aquí.

# Apartado 2: interrupcionesEdgeMejorado.py

import RPi.GPIO as GPIO
import time, sys

rojoPin = 00
verdePin = 00

def encender(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    
def apagar(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    
def encenderRojo():
    encender(rojoPin)
    
def apagarRojo():
    apagar(rojoPin)
    
def encenderVerde():
    encender(verdePin)
    
def apagarVerde():
    apagar(verdePin)
    
pulsadorGPIO_rojo = 00
pulsadorGPIO_verde = 00


def main():

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pulsadorGPIO_rojo, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        GPIO.wait_for_edge(pulsadorGPIO_rojo, GPIO.FALLING)
        encenderRojo()
    else:
        apagarRojo()
        
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pulsadorGPIO_verde, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        GPIO.wait_for_edge(pulsadorGPIO_verde, GPIO.FALLING)
        encenderVerde()
    else:
        apagarVerde()
        
if __name__ == '__main__':
	main()
