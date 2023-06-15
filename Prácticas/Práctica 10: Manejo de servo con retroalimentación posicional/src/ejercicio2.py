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

def parar ():
  miServo.set_servo_pulsewidth(servoPin, 1500)
  time.sleep(1)
  miServo.set_servo_pulsewidth(servoPin, 0)
  miServo.stop()
  
print ("Dispositivo listo")
print("Valores velocidad: 1, 2, 3, 4 y 5 (velocidad mínima 1 y velocidad máxima 5)")

MIN_SPEED = 1440
INT_VALUE1 = 1400
INT_VALUE2 = 1360
INT_VALUE3 = 1320
MAX_SPEED = 1280

def main():
    while True:
      char = leerOrden()
      
      if char == "1":
        print("Adelante (" + char + ")")
        adelante (MIN_SPEED)
      elif char == "2":
        print("Adelante (" + char + ")")
        adelante (INT_VALUE1)      
      elif char == "3":
        print("Adelante (" + char + ")")
        adelante (INT_VALUE2)
      elif char == "4":
        print("Adelante (" + char + ")")
        adelante (INT_VALUE3)
      elif char == "5":
        print("Adelante (" + char + ")")
        adelante (MAX_SPEED)
        
      # Orden para parar el motor y salir del programa:
      elif char == "x":
        print("Parando motor (" + char + ") ...")
        parar ()
        print("Motor parado")
        break
    
if __name__ == "__main__":
    main()