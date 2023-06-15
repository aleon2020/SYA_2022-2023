import RPi.GPIO as GPIO
import time
import threading

OPTOINTERRUPTOR = 2
CONTADOR = 0
MUESCAS = 4
SEGUNDOS = 2

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(OPTOINTERRUPTOR,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def RPM(aux):
    print(aux*60/MUESCAS/SEGUNDOS,"revoluciones por minuto (RPM)")
    time.sleep(SEGUNDOS)

def tarea(nombre,OPTOINTERRUPTOR):
    global CONTADOR
    GPIO.add_event_detect(OPTOINTERRUPTOR,GPIO.FALLING,
        callback = callbackOPTOINTERRUPTOR,bouncetime = 100)
    while True:
        aux = CONTADOR
        CONTADOR = 0
        RPM(aux)

def callbackOPTOINTERRUPTOR(OPTOINTERRUPTOR):
    global CONTADOR
    CONTADOR = CONTADOR + 1
    
def callbackSalir(senial,cuadro):
    GPIO.cleanup()
    sys.exit(0)
    
hilo = threading.Thread(target=tarea, args=("Hilo",OPTOINTERRUPTOR,))
hilo.start()
hilo.join()
signal.signal(signal.SIGINT,callbackSalir)
signal.pause()