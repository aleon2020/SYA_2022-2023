import RPi.GPIO as GPIO
import time
import threading

MEDIDOR_BOTON = 4
MEDIDOR_PRESENCIA = 23
LED_CORTESÍA = 26

def encender(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    
def apagar(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    
def tareaPresencia(hilo):
    SEGUNDOS = 0
    if GPIO.wait_for_edge(MEDIDOR_BOTON,GPIO.FALLING):
        while SEGUNDOS < 30:
            if GPIO.input(MEDIDOR_PRESENCIA):
                encender(LED_CORTESÍA)
            else:
                apagar(LED_CORTESÍA)
            time.sleep(1)
            SEGUNDOS = SEGUNDOS + 1
            
def tareaPresion(hilo):
    while True:
        while (GPIO.input(MEDIDOR_BOTON)):
            hiloPresencia = threading.Thread(target=tareaPresencia,args=("hiloPresencia",))
            hiloPresencia.start()
            hiloPresencia.join()
            time.sleep(1)
            
GPIO.setmode(GPIO.BCM)
GPIO.setup(MEDIDOR_BOTON,GPIO.IN)
GPIO.setup(MEDIDOR_PRESENCIA,GPIO.IN)
GPIO.setwarnings(False)

def main():
    hiloPresion = threading.Thread(target=tareaPresion,args=("hiloPresion",))
    hiloPresion.start()
    hiloPresion.join()
if __name__ == "__main__":
    main()