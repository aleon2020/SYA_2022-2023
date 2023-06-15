# Ejercicio 2. Interfaz de usuario
# Partiendo de la funcionalidad implementada para el Ejercicio 1, añade nueva
# funcionalidad para que el programa pida por teclado al usuario las órdenes de
# qué quiere hacer. Por ejemplo:
# encender rojo
# apagar rojo
# encender blanco
# encender verde
# salir

import time, sys
import RPi.GPIO as GPIO

rojoPin = 36
azulPin = 38
verdePin = 40

input("Hola! Bienvenido al menú de usuario de la práctica 2")
input("En este apartado serás tú quién pueda elegir qué color encender y apagar")
input("Los colores a elegir son los siguientes:")
input("rojo verde azul magenta cyan amarillo blanco")
input("Y a estos colores se le pueden aplicar las siguientes acciones:")
input("encender apagar salir")
input("Por lo tanto, solo se detectará la siguiente entrada:")
input("accion(encender,apagar,salir) espacio color(rojo,verde,azul,...)")
input("Ejemplo para encender el color rojo: encender rojo")

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
    apagar(rojoPin)
    apagar(azulPin)
    
def apagarVerde():
    apagar(verdePin)

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
        accion = input("Introduce un color y una acción a realizar: ")
        if accion == "encender rojo":
            encenderRojo()
        elif accion == "apagar rojo":
            apagarRojo()        
        elif accion == "encender azul":
            encenderAzul()
        elif accion == "apagar azul":
            apagarAzul()
        elif accion == "encender verde":
            encenderVerde()
        elif accion == "apagar verde":
            apagarVerde()
        elif accion == "encender magenta":
            encenderMagenta()
        elif accion == "apagar magenta":
            apagarMagenta()
        elif accion == "encender amarillo":
            encenderAmarillo()
        elif accion == "apagar amarillo":
            apagarAmarillo()
        elif accion == "encender cyan":
            encenderCyan()
        elif accion == "apagar cyan":
            apagarCyan()
        elif accion == "encender blanco":
            encenderBlanco()
        elif accion == "apagar blanco":
            apagarBlanco()
        elif accion == "salir":
            print("El programa ha terminado")
            break
        else:
            print("No se ha introducido la orden correctamente")

if __name__ == '__main__':
    main()
