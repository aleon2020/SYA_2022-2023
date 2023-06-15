import sys, tty, termios, time, pigpio

servoPin = 2

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
  
print ("Dispositivo listo")
print("Órdenes sentido horario: 1, 2, 3, 4 y 5 (velocidad mínima 1 y velocidad máxima 5)")
print("Órdenes sentido antihorario: 6, 7, 8, 9 y 0 (velocidad mínima 0 y velocidad máxima 6)")

def main():
    while True:
      char = leerOrden()
      
      # Órdenes sentido horario:
      if char == "1":
        print("Adelante (" + char + ")")
        adelante (1440)
      elif char == "2":
        print("Adelante (" + char + ")")
        adelante (1400)      
      elif char == "3":
        print("Adelante (" + char + ")")
        adelante (1360)
      elif char == "4":
        print("Adelante (" + char + ")")
        adelante (1320)
      elif char == "5":
        print("Adelante (" + char + ")")
        adelante (1280)
        
      # Órdenes sentido antihorario:
      elif char == "6":
        print("Atrás (" + char + ")")
        atras (1720)
      elif char == "7":
        print("Atrás (" + char + ")")
        atras (1680)
      elif char == "8":
        print("Atrás (" + char + ")")
        atras (1640)
      elif char == "9":
        print("Atrás (" + char + ")")
        atras (1600)
      elif char == "0":
        print("Atrás (" + char + ")")
        atras (1560)
        
      # Orden para parar el motor y salir del programa:
      elif char == "x":
        print("Parando motor (" + char + ") ...")
        parar ()
        print("Motor parado")
        break
    
if __name__ == "__main__":
    main()