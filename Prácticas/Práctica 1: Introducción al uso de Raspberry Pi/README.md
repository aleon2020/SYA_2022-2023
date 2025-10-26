# Práctica 1: Introducción al uso de Raspberry Pi

## 1. GPIO elements and interface

[![Elementos e interfaz GPIO de la Raspberry Pi](/home/alumnos/aalberto/Escritorio/Elementos e interfaz GPIO en Raspberry Pi.png)]

## 2. Basic Commands (Turning on an LED)

**import RPi.GPIO as GPIO**: We must write this line whenever we want to use the GPIO ports.

**GPIO.setmode(GPIO.BOARD)**: Indicates the pin numbering scheme we will use (BOARD or BCM).

**GPIO.setup(11,GPIO.OUT)**: Indicates the pin we will use (11) and which will be the output (GPIO.OUT).

**pwm = GPIO.PWM(11,100)**: We must use PWM to control the LED brightness as we wish, so we create a PWM object with the pin and operating frequency as parameters.

**pwm.start(50)**: Sets the duty cycle (DutyCycle), indicating the percentage of the period the signal is high.

**pwm.ChangeDutyCycle(1)**: Used to change the duty cycle (LED intensity).

**pwm.ChangeFrequency(1000)**: Used to change the frequency of the PWM signal.

**input("...")**: This instruction forces the program to stop executing so that all other commanded instructions can take effect (we need to give them time to execute).

**pwm.stop()**: This line disables the PWM.

**GPIO.cleanup()**: This line disables the GPIO ports.

## 3. Personal opinion on this lab

Considering this was my first practice in this environment, and given my lack of prior knowledge, I found it to be a very interesting and easy-to-understand first practice.

Interestingly, as I mentioned earlier, it took me significantly longer to set up the environment and become familiar with it in this first practice than it took to complete the practice itself.

## 4. Multimedia Content

<p align="center">
  <img src="https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%201:%20Introducci%C3%B3n%20al%20uso%20de%20Raspberry%20Pi/media/Imagen%20Circuito%20Pr%C3%A1ctica%201%20(1).jpg?raw=true">
</p>

<p align="center">
  <img src="https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%201:%20Introducci%C3%B3n%20al%20uso%20de%20Raspberry%20Pi/media/Imagen%20Circuito%20Pr%C3%A1ctica%201%20(2).jpg?raw=true">
</p>

[PRACTICE 1 EXECUTION VIDEO](https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%201%3A%20Introducci%C3%B3n%20al%20uso%20de%20Raspberry%20Pi/media/Video%20Ejecuci%C3%B3n%20Pr%C3%A1ctica%201.mp4)
