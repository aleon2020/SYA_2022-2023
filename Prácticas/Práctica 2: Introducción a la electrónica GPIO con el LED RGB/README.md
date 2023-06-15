# Resumen Sensores y Actuadores prácticas primer cuatrimestre

# Alberto León Luengo

## Grado de Ingeniería en Robótica Software

## Práctica 2: Introducción a la electrónica GPIO con el led RGB

### 1. El led RGB

Un led RGB está compuesto por 4 pines: Los colores corresponden con los pines 1, 3 y 4 (rojo, verde y azul, respectivamente), mientras que el pin 2 corresponde con el cátodo.

### 2. Ejemplo de programación del led RGB

```
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

### 3. Opinión personal sobre esta práctica

Esta práctica me ha sido más rápida de realizar, ya que después de la práctica anterior ya vengo familiarizado con el entorno de desarrollo de prácticas y me ha sido menos costosa llevarla a cabo.

Sin embargo, uno de los problemas más grandes que me he podido encontrar en esta práctica, al igual que muchos de mis compañeros, ha sido el cambio de polaridad del led RGB, ya que nos ha hecho modificar el circuito a como venía principalmente en el enunciado de la práctica.

El código que se requería me ha sido muy fácil de desarrollar, ya que la única "ayuda externa" que he necesitado en esta práctica es consultar la tabla de valores de los colores RGB y sus derivados, para poder crear las funciones de encendido y apagado de dichos colores.

El ejercicio que más me ha gustado realizar ha sido el último, ya que me ha gustado mucho la idea de jugar con el usuario para ver que acción le gustaría realizar.

### 4. Contenido multimedia sobre esta práctica

Imagen: Montaje del circuito de la práctica 2.

https://urjc-my.sharepoint.com/:i:/g/personal/a_leon_2020_alumnos_urjc_es/EaHZ6IlEMuxMnEbRgavM8FUB1iuTNfzQyim6DS07Y2M7xg?e=VGnAQ1

Vídeo: Ejecución del ejercicio 1, apartado 1.

https://urjc-my.sharepoint.com/:v:/g/personal/a_leon_2020_alumnos_urjc_es/EWD6z8TeJFtBuKzDFkHzQa4BrVSFMrmguhpOp_cQXUtLvw?e=hVfVV6

Vídeo: Ejecución del ejercicio 1, apartado 2.

https://urjc-my.sharepoint.com/:v:/g/personal/a_leon_2020_alumnos_urjc_es/EapaClS2V9VArmhXjVtxIEQBCDpUHGunxre86jI0nTBDGw?e=pc4xK2

Vídeo: Ejecución del ejercicio 2.

https://urjc-my.sharepoint.com/:v:/g/personal/a_leon_2020_alumnos_urjc_es/EcjQaPhYT6FEmhg72wKDYpoBY3lx0ptJXgUeLJGqPt6mFw?e=g9Yggd

NOTA: Este último ejercicio consistía en desarrollar el código de tal manera que el usuario pudiese elegir qué colores encender y apagar, y cuándo salir del programa. En el caso del vídeo, le he ordenado que encienda y apague los 7 colores disponibles en el mismo órden en el que vienen escritas sus funciones, y por último, le he ordenado salir del programa.
