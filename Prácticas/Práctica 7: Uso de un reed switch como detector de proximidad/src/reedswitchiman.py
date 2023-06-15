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

INTERRUPTOR = 17
LED_DE_AVISO = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(INTERRUPTOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False)

def main():
    while True:
        if GPIO.input(INTERRUPTOR):
            print("El circuito está cerrado")
            apagar(LED_DE_AVISO)
        else:
            print("El circuito ha sido abierto")
            encender(LED_DE_AVISO)
        time.sleep(0.1)

main()