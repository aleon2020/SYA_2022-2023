# Ejercicio 2

# Rediseña el esquema de conexión, así como la implementación de los tres códigos facilitados para dar 
# soporte a dos botones que a su vez operan sobre dos LEDs de forma independiente. Así, al pulsar uno de los
# botones, se encenderá un led rojo (y se apagará al soltar dicho botón); y, al pulsar el otro botón, lo 
# mismo pero con el otro LED, que será verde.
# Recuerda que deberás ofrecer esa funcionalidad bajo las tres implementaciones que se han expuesto aquí.

# Apartado 2: interrupcionesEdgeMejorado.py

import threading
import time
import RPi.GPIO as GPIO

pulsadorGPIOverde = 21
verdePin = 20

class Hilo(threading.Thread):
    def __init__(self,pulsador,led):
        threading.Thread.__init__(self)
        self.pulsador = pulsador
        self.led = led
        
    def run(self):
        tarea(self.pulsador,self.led)

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
    while True:
        if GPIO.wait_for_edge(pulsador,GPIO.FALLING,timeout=500):
            print("El botón verde se ha pulsado")
            encender(led)
        else:
            apagar(led)
        
def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pulsadorGPIOverde,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    ledverde = Hilo(pulsadorGPIOverde,verdePin)
    ledverde.start()
    ledverde.join()
    
main()
GPIO.cleanup()