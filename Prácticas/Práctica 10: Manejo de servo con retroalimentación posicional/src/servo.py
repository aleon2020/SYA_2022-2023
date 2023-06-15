# Practica 10. Sensores y actuadores. URJC. Julio Vega
# Codigo de ejemplo de manejo del Servo Feedback 360 de Parallax

#!/usr/bin/env python3

import sys, tty, termios, time, pigpio

servoPin = 2 # numeracion en modo BCM (que es el usado por defecto por pigpio)

miServo = pigpio.pi() # instancia de la clase pi de la libreria pigpio
                      # Usaremos el demonio pigpiod para comandar al motor por teclado
                      # Por ello, IMPORTANTE, hay que lanzar el demonio: sudo pigpiod

def leerOrden(): # para leer orden por teclado a comandar al motor
  fd = sys.stdin.fileno()
  old_settings = termios.tcgetattr(fd)

  try:
    tty.setraw(sys.stdin.fileno())
    ch = sys.stdin.read(1)

  finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

'''
  Según especificaciones de la compañía fabricante de estos servos, Parallax,
  la modulación PWM de estos servos tiene los siguientes rangos:
  - Girar en un sentido: [1280...1480]
  - Parar: 1500
  - Girar en el otro: [1520...1720]

  Mientras más cerca al valor 1500, más despacio; cuanto más alejado, más rápido.
'''
def adelante (): # girar en un sentido a velocidad máxima
  miServo.set_servo_pulsewidth(servoPin, 1720)

def atras (): # girar en el otro sentido a velocidad máxima
  miServo.set_servo_pulsewidth(servoPin, 1280)

def parar ():
  miServo.set_servo_pulsewidth(servoPin, 1500) # 1.º lo ponemos a 0 rpm
  time.sleep(1)
  miServo.set_servo_pulsewidth(servoPin, 0) # y 2.º lo "apagamos"
  miServo.stop()

#==========================================================================

print ("Dispositivo listo. Esperando órdenes (w = adelante, s = atrás, x = parar)...")

while True:
  char = leerOrden()

  if char == "w":
    print("Adelante (" + char + ")")
    adelante ()

  elif char == "s":
    print("Atrás (" + char + ")")
    atras ()

  elif char == "x":
    print("Parando motor (" + char + ") ...")
    parar ()
    print("Motor parado")
    break

