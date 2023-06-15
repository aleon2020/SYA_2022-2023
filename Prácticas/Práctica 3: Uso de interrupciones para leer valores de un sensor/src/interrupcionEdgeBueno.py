# Ejercicio 1

# Mejora la implementación del código facilitado en interrupcionEdge.py para que no ocurran los problemas
# descritos del mismo. Al fichero resultante denomínalo interrupcionEdgeBueno.py

#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

pulsadorGPIO = 16

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pulsadorGPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        GPIO.wait_for_edge(pulsadorGPIO, GPIO.RISING)
        print("El boton se ha pulsado")
        time.sleep(0.1)

# La solución a este ejercicio es muy sencilla: Al ejecutar el programa me he percatado de que se
# muestra más de una vez el mensaje de pulsado cuando realmente solo he pulsado el botón una vez.
# Para ello, lo único que he modificado del programa original es que a la última línea del programa,
# dentro del bucle infinito, le he añadido un sistema antirebote (mencionado así en el enunciado de esta
# práctica), que consiste en un time.sleep(0.1), ya que cuanto menor es la frecuencia, mayor será el
# alivio para el procesador, y por tanto, evitaremos saturarlo.
