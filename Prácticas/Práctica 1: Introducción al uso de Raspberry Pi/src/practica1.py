import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup (11, GPIO.OUT)
pwm = GPIO.PWM(11,100)
pwm.start (50)
pwm.ChangeDutyCycle(100)
pwm.ChangeFrequency (1000)
input("Ejecutando hasta que pulse una tecla...")
pwm.stop()
GPIO.cleanup()
