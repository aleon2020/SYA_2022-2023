# Ejercicio 2

# Rediseña el esquema de conexión, así como la implementación de los tres códigos facilitados para dar 
# soporte a dos botones que a su vez operan sobre dos LEDs de forma independiente. Así, al pulsar uno de los
# botones, se encenderá un led rojo (y se apagará al soltar dicho botón); y, al pulsar el otro botón, lo 
# mismo pero con el otro LED, que será verde.
# Recuerda que deberás ofrecer esa funcionalidad bajo las tres implementaciones que se han expuesto aquí.

# Apartado 3: interrupcionEventMejorado.py

import signal
import sys
import RPi.GPIO as GPIO

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

def callbackSalir (senial, cuadro):
    GPIO.cleanup ()
    sys.exit(0)

def callbackBotonRojoPulsado ():
    encenderRojo()

def callbackBotonVerdePulsado ():
    encenderVerde()

def main():

    pulsadorGPIO_rojo = 00
    pulsadorGPIO_verde = 00

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pulsadorGPIO_rojo, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(pulsadorGPIO_rojo, GPIO.FALLING, 
      callback=callbackBotonRojoPulsado, bouncetime=500)
    
    signal.signal(signal.SIGINT, callbackSalir)
    signal.pause()

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pulsadorGPIO_verde, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(pulsadorGPIO_verde, GPIO.FALLING, 
      callback=callbackBotonVerdePulsado, bouncetime=500)
    
    signal.signal(signal.SIGINT, callbackSalir)
    signal.pause()

if __name__ == '__main__':
    main()