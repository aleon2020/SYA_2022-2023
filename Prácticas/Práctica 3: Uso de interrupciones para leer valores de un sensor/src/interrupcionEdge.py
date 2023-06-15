#!/usr/bin/env python3

import RPi.GPIO as GPIO

pulsadorGPIO = 16

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pulsadorGPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        GPIO.wait_for_edge(pulsadorGPIO, GPIO.RISING)
        print("El boton se ha pulsado")

