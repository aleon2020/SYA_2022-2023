# Ejercicio 2

# Rediseña el esquema de conexión, así como la implementación de los tres códigos facilitados para dar 
# soporte a dos botones que a su vez operan sobre dos LEDs de forma independiente. Así, al pulsar uno de los
# botones, se encenderá un led rojo (y se apagará al soltar dicho botón); y, al pulsar el otro botón, lo 
# mismo pero con el otro LED, que será verde.
# Recuerda que deberás ofrecer esa funcionalidad bajo las tres implementaciones que se han expuesto aquí.

# Apartado 1: sinInterrupcionesMejorado.py

import threading
import time
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
    
def tarea(pulsador,led):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pulsador, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while True:
        pulsado = False
        if not GPIO.input(pulsador):
            if not pulsado:
                print("El boton se ha pulsado")
                encender(led)
                pulsado = True
        else:
            apagar(led)
            pulsado = True
        time.sleep(0.1)
        
def ledrojo():
    tarea(pulsadorGPIOrojo,rojoPin)
    
def ledverde():
    tarea(pulsadorGPIOverde,verdePin)
    
hilo1 = threading.Thread(target=ledrojo)
hilo1.start()

hilo2 = threading.Thread(target=ledverde)
hilo2.start()

hilo1.join()
hilo2.join()