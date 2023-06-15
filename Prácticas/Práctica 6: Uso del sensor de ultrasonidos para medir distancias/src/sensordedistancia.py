# Así, haz uso de tres LEDs que indiquen el acercamiento del objeto según tu criterio:
# 1. Luz verde. Inicialmente, será el LED que estará encendido, indicando que existe una distancia de
# seguridad razonable al objeto.
# 2. Luz amarilla. Si el objeto entra en un tramo intermedio de distancia, que consideremos prudencial,
# aunque no crítica.
# 3. Luz roja. Si el objeto entra en una zona peligrosa de distancia; esto es, está excesivamente cerca.
# Es muy interesante hacer pruebas experimentales para, por ejemplo, establecer el rango del sensor; e.g.
# distancia mínima/máxima de detención de objetos.

import RPi.GPIO as GPIO
import time

def encender(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

def apagar(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

PIN_TRIGGER = 4 
PIN_ECHO = 17
LED_VERDE = 21
LED_AMARILLO = 20
LED_ROJO = 16

def main():
    while True:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(PIN_ECHO, GPIO.IN)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)
        time.sleep(1)
        GPIO.output(PIN_TRIGGER, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)
        while GPIO.input(PIN_ECHO)==0:
            inicioPulso = time.time()
        while GPIO.input(PIN_ECHO)==1:
            finPulso = time.time()
        duracionPulso = finPulso - inicioPulso
        distancia = round(duracionPulso * 17150, 2)
        print("Distancia: ", distancia, " cm")
        if (distancia >= 35):
            encender(LED_VERDE)
            apagar(LED_AMARILLO)
            apagar(LED_ROJO)
        if (distancia > 15 and distancia < 35):
            apagar(LED_VERDE)
            encender(LED_AMARILLO)
            apagar(LED_ROJO)
        if (distancia <= 15):
            apagar(LED_VERDE)
            apagar(LED_AMARILLO)
            encender(LED_ROJO)
      
main()
