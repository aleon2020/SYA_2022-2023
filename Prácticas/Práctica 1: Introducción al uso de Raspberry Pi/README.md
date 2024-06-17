# Resumen Sensores y Actuadores prácticas primer cuatrimestre

# Alberto León Luengo

## Grado de Ingeniería en Robótica Software

## Práctica 1: Introducción al uso de Raspberry Pi

### 1. Elementos e interfaz GPIO

[![Elementos e interfaz GPIO de la Raspberry Pi](/home/alumnos/aalberto/Escritorio/Elementos e interfaz GPIO en Raspberry Pi.png)]

### 2. Comandos básicos (encendido de un LED)

**import RPi.GPIO as GPIO**: Esta línea la debemos de escribir siempre que queramos usar los puertos GPIO.

**GPIO.setmode(GPIO.BOARD)**: Indica el esquema de numeración de pin que vamos a usar (BOARD o BCM).

**GPIO.setup(11,GPIO.OUT)**: Indica el pin que vamos a usar (11) y que va a ser de salida (GPIO.OUT).

**pwm = GPIO.PWM(11,100)**: Debemos usar PWM para controlar el brillo del LED a nuestro antojo, por lo que creamos un objeto PWM con el pin y la frecuencia de trabajo como parámetros.

**pwm.start(50)**: Establece el ciclo de trabajo (DutyCycle), indica el porcentaje del periodo en que la señal está en estado alto.

**pwm.ChangeDutyCycle(1)**: Sirve para cambiar el ciclo de trabajo (intensidad del LED).

**pwm.ChangeFrequency(1000)**: Sirve para cambiar la frecuencia de la señal PWM.

**input("...")**: Esta instrucción fuerza a parar la ejecución del programa, todo esto para que todas las demás instrucciones comandadas tengan efecto (hemos de darles tiempo para que se ejecuten).

**pwm.stop()**: Esta línea desactiva el PWM.

**GPIO.cleanup()**: Esta línea desactiva los puertos GPIO.

### 3. Opinión personal sobre esta práctica

Para ser mi primera práctica en este entorno y al no tener conocimientos previos sobre ello, me ha parecido una primera práctica muy interesante y muy sencilla de entender.

Curiosamente, como ya he mencionado anteriormente, en esta primera práctica me ha llevado bastante más tiempo instalar el entorno y familiarizarme con él, que lo que he tardado en realizar la práctica en sí.

### 4. Contenido multimedia sobre esta práctica

Imagen: Montaje del circuito (1)

<p align="center">
  <img src="https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%201:%20Introducci%C3%B3n%20al%20uso%20de%20Raspberry%20Pi/media/Imagen%20Circuito%20Pr%C3%A1ctica%201%20(1).jpg?raw=true">
</p>

Imagen: Montaje del circuito (2)

<p align="center">
  <img src="https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%201:%20Introducci%C3%B3n%20al%20uso%20de%20Raspberry%20Pi/media/Imagen%20Circuito%20Pr%C3%A1ctica%201%20(2).jpg?raw=true">
</p>

[Vídeo: Video de ejecución de la práctica 1](https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%201%3A%20Introducci%C3%B3n%20al%20uso%20de%20Raspberry%20Pi/media/Video%20Ejecuci%C3%B3n%20Pr%C3%A1ctica%201.mp4)
