import RPi.GPIO as GPIO
import time
import sys, tty, termios, time, pigpio

miServo = pigpio.pi()

def leerOrden(): 
  fd = sys.stdin.fileno()
  old_settings = termios.tcgetattr(fd)

  try:
    tty.setraw(sys.stdin.fileno())
    ch = sys.stdin.read(1)

  finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# Rango de valores para la velocidad del servo en este sentido: [1280 a 1480]
def adelante (velocidad):
  miServo.set_servo_pulsewidth(servoPin, velocidad)

# Rango de valores para la velocidad del servo en el otro sentido: [1520 a 1720]
def atras (velocidad):
  miServo.set_servo_pulsewidth(servoPin, velocidad)

def parar ():
  miServo.set_servo_pulsewidth(servoPin, 1500)
  time.sleep(1)
  miServo.set_servo_pulsewidth(servoPin, 0)
  miServo.stop()
  
print("Bienvenido a la interfaz de usuario")
print("Aquí podrás elegir en qué sentido quieres que gire tu servo (adelante => horario, atrás => antihorario)")
sentido = input("¿En qué dirección/sentido quieres que gire tu servo (derecha/izquierda)?: ")

def encender(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

def apagar(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

PIN_TRIGGER = 23
PIN_ECHO = 18
LED_VERDE = 25
LED_ROJO = 7
servoPin = 14

def main():
    while True:
        # Sentido horario: 1440  1280
        # Sentido antihorario: 1720  1560
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
        if sentido == "derecha":
            if (distancia >= 65):
                encender(LED_VERDE)
                apagar(LED_ROJO)
                adelante(1280)
            if (distancia > 45 and distancia < 65):
                apagar(LED_VERDE)
                apagar(LED_ROJO)
                adelante(1400)
            if (distancia > 25 and distancia < 45):
                apagar(LED_VERDE)
                encender(LED_ROJO)
                parar()
            if (distancia <= 25):
                apagar(LED_VERDE)
                encender(LED_ROJO)
                adelante(1400)
            if (distancia <= 5):
                apagar(LED_VERDE)
                encender(LED_ROJO)
                adelante(1280)
        if sentido == "izquierda":
            if (distancia >= 65):
                encender(LED_VERDE)
                apagar(LED_ROJO)
                atras(1680)
            if (distancia > 45 and distancia < 65):
                apagar(LED_VERDE)
                apagar(LED_ROJO)
                atras(1560)
            if (distancia > 25 and distancia < 45):
                apagar(LED_VERDE)
                encender(LED_ROJO)
                parar()
            if (distancia <= 25):
                apagar(LED_VERDE)
                encender(LED_ROJO)
                atras(1560)
            if (distancia <= 5):
                apagar(LED_VERDE)
                encender(LED_ROJO)
                atras(1680)
main()