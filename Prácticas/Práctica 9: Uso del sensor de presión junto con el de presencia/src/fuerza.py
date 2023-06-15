import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
MEDIDOR = 4
GPIO.setup(MEDIDOR,GPIO.IN)

def sensarfuerza():
    valor = GPIO.input(MEDIDOR)
    if valor == 0:
        print("LOW")
    else:
        print("HIGH")

def main():
    print("Detectando cualquier tipo de fuerza...")
    while True:
        sensarfuerza()
        time.sleep(0.25)
        
if __name__ == '__main__':
    main()