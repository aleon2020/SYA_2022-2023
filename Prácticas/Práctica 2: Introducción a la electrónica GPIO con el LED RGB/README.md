# Práctica 2: Introducción a la electrónica GPIO con el led RGB

## 1. The RGB LED

An RGB LED consists of 4 pins: The colors correspond to pins 1, 3, and 4 (red, green, and blue, respectively), while pin 2 corresponds to the cathode.

## 2. RGB LED programming example

```py
import time,sys
import RPI.GPIO as GPIO
# Variables de cada color asignadas a su pin
rojoPin = 11
azulPin = 13
verdePin = 15
# Función que enciende UN pin, el cual se pasa como parámetro
def encender(pin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,GPIO.HIGH)
# Función que apaga UN pin, el cual se pasa como parámetro
def apagar(pin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,GPIO.LOW)
# Función que enciende el color rojo
def encenderRojo():
	encenderRojo(rojoPin)
# Programa principal
def main():
	while True:
		encenderRojo()
	return
if __name__ == '__main__':
	main()
```

## 3. Personal opinion on this practice

This practice was faster for me to complete, since I was already familiar with the practice development environment after the previous practice, and it was less difficult to complete.

However, one of the biggest problems I encountered in this practice, like many of my classmates, was changing the polarity of the RGB LED, as it required us to modify the circuit from what was primarily described in the practice statement.

The code required was very easy for me to develop, as the only "external help" I needed in this exercise was to consult the table of RGB color values ​​and their derivatives to create the functions to turn those colors on and off.

The exercise I enjoyed doing the most was the last one, as I really liked the idea of ​​playing with the user to see what action they would like to perform.

### 4. Multimedia Content

<p align="center">
  <img src="https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%202:%20Introducci%C3%B3n%20a%20la%20electr%C3%B3nica%20GPIO%20con%20el%20LED%20RGB/media/Imagen%20Circuito%20Pr%C3%A1ctica%202.jpg?raw=true">
</p>

[PRACTICE 2 EXECUTION VIDEO EXERCISE 1 POINT 1](https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%202%3A%20Introducci%C3%B3n%20a%20la%20electr%C3%B3nica%20GPIO%20con%20el%20LED%20RGB/media/Video%20Ejecuci%C3%B3n%20Pr%C3%A1ctica%202%20Ejercicio%201%20Apartado%201.mp4)

[PRACTICE 2 EXECUTION VIDEO EXERCISE 1 POINT 2](https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%202%3A%20Introducci%C3%B3n%20a%20la%20electr%C3%B3nica%20GPIO%20con%20el%20LED%20RGB/media/Video%20Ejecuci%C3%B3n%20Pr%C3%A1ctica%202%20Ejercicio%201%20Apartado%202.mp4)

[PRACTICE 2 EXECUTION VIDEO](https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%202%3A%20Introducci%C3%B3n%20a%20la%20electr%C3%B3nica%20GPIO%20con%20el%20LED%20RGB/media/Video%20Ejecuci%C3%B3n%20Pr%C3%A1ctica%202%20Ejercicio%202.mp4)

**NOTE**: This last exercise involved developing the code in such a way that the user could choose which colors to turn on and off, and when to exit the program. In the case of the video, I instructed it to turn the 7 available colors on and off in the same order in which their functions are written, and finally, I instructed it to exit the program.
