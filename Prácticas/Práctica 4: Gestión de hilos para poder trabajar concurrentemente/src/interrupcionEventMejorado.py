# Ejercicio 2

# Rediseña el esquema de conexión, así como la implementación de los tres códigos facilitados para dar 
# soporte a dos botones que a su vez operan sobre dos LEDs de forma independiente. Así, al pulsar uno de los
# botones, se encenderá un led rojo (y se apagará al soltar dicho botón); y, al pulsar el otro botón, lo 
# mismo pero con el otro LED, que será verde.
# Recuerda que deberás ofrecer esa funcionalidad bajo las tres implementaciones que se han expuesto aquí.

# Apartado 3: interrupcionEventMejorado.py

#!/usr/bin/env python3

import threading
import signal
import sys
import RPi.GPIO as GPIO

pulsadorGPIOrojo = 7
rojoPin = 16
pulsadorGPIOverde = 21
verdePin = 20

def encender(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    
def apagar(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    
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

def callbackBotonRojoPulsado (canal):
    if (canal == pulsadorGPIOrojo):
        encenderRojo()
        print("Se ha pulsado el botón rojo")
        GPIO.remove_event_detect(pulsadorGPIOrojo)
        GPIO.add_event_detect(pulsadorGPIOrojo,GPIO.RISING,
            callback=callbackBotonRojoNoPulsado, bouncetime = 500)

def callbackBotonVerdePulsado (canal):
    if (canal == pulsadorGPIOverde):
        encenderVerde()
        print("Se ha pulsado el botón verde")
        GPIO.remove_event_detect(pulsadorGPIOverde)
        GPIO.add_event_detect(pulsadorGPIOverde,GPIO.RISING,
            callback=callbackBotonVerdeNoPulsado, bouncetime = 500)

def callbackBotonRojoNoPulsado (canal):
    if (canal == pulsadorGPIOrojo):
        apagarRojo()
        print("Se ha dejado de pulsar el botón rojo")
        GPIO.remove_event_detect(pulsadorGPIOrojo)
        tarea(pulsadorGPIOrojo)

def callbackBotonVerdeNoPulsado (canal):
    if (canal == pulsadorGPIOverde):
        apagarVerde()
        print("Se ha dejado de pulsar el botón verde")
        GPIO.remove_event_detect(pulsadorGPIOverde)
        tarea(pulsadorGPIOverde)

def tarea(pulsador):
        pulsadorGPIOrojo = 7
        rojoPin = 16
        pulsadorGPIOverde = 21
        verdePin = 20
        GPIO.setmode(GPIO.BCM)
        if (pulsador == pulsadorGPIOrojo):
            GPIO.setup(pulsador, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(pulsador, GPIO.FALLING, 
            callback = callbackBotonRojoPulsado, bouncetime=500)
        if (pulsador == pulsadorGPIOverde):
            GPIO.setup(pulsador, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(pulsador, GPIO.FALLING, 
            callback = callbackBotonVerdePulsado, bouncetime=500)            
        
def ledrojo():
    tarea(pulsadorGPIOrojo)
    
def ledverde():
    tarea(pulsadorGPIOverde)
    
hilo1 = threading.Thread(target=ledrojo)
hilo1.start()

hilo2 = threading.Thread(target=ledverde)
hilo2.start()

hilo1.join()
hilo2.join()