import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BCM)
MEDIDOR = 17
GPIO.setup(MEDIDOR,GPIO.IN)

def sensarhumedad():
    valor = GPIO.input(MEDIDOR)
    if valor == 0:
        print("Húmedo")
        guardarregistrodecambios("1")
    else:
        print("Seco")
        guardarregistrodecambios("0")
        
def crearregistrodecambios():
    nombredearchivo = "registrodecambiosdehumedad.csv"
    csv = open(nombredearchivo,'w')
    csv.write("Timestamp,Humedad\n")
    csv.close
    
def guardarregistrodecambios(valor):
    nombredearchivo = "registrodecambiosdehumedad.csv"
    humedad = valor
    fecha = str(datetime.datetime.now())
    dato = fecha + "," + humedad + "\n"
    csv = open(nombredearchivo,'a')
    csv.write(dato)
    csv.close

def main():
    print("Sensando humedad")
    crearregistrodecambios()
    while True:
        sensarhumedad()
        time.sleep(1)
        
if __name__ == '__main__':
    main()