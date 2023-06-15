import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
MEDIDOR = 24
GPIO.setup(MEDIDOR,GPIO.IN)

def detectarpresencia():
    valor = GPIO.input(MEDIDOR)
    if valor == 0:
        print("LOW")
    else:
        print("HIGH")

def main():
    print("Detectando cualquier tipo de presencia...")
    while True:
        detectarpresencia()
        time.sleep(0.25)
        
if __name__ == '__main__':
    main()