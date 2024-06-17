# Resumen Sensores y Actuadores prácticas primer cuatrimestre

# Alberto León Luengo

## Grado de Ingeniería en Robótica Software

## Práctica 5: Construcción de un encoder incremental usando un sensor óptico

### 1. El encoder óptico

					res = (pi*D)/(2*ar)

Esta es la fórmula general que se aplica para saber la resolución de un encoder, donde podemos distinguir: res (resolución de un encoder), D (diámetro del disco), ar (ancho de cada ranura). 

### 2. Divisor de voltaje para el transistor

			Vout = Vin * ((R2) / (R1 + R2))
			
A partir de esta fórmula podemos obtener el voltaje de salida deseado de 3.3 V partiendo de un voltaje de entrada de 5 V (si R2 es el doble de R1, como se puede ver en la fórmula anterior).

	Si R2 = 2*R1 => Vout = 2/3 * Vin = 2/3 * 5 V = 3.3 V
	
En nuestro caso, R1 será la resistencia de 10000 ohmios y R2 será la resistencia de 20000 ohmios.

### 3. Opinión personal sobre esta práctica

De todas las prácticas que había realizando en la asignatura, ésta ha sido la que más tiempo y trabajo me ha costado de desarrollar, ya que era la primera práctica
en la que no se nos facilitaba el esquema de conexión, y todo ello sumado a lo que se nos pide en el ejercicio, que es bastante complejo comparado con lo que se nos ha 
pedido en otras ocasiones.

Para realizar esta práctica he utilizado el optointerrutor, que contiene en el "hueco" que hay entre la E y la D un sensor infrarrojo que detecta cuando se ha roto esa 
barrera, y en nuestro caso, podemos crear un programa de tal manera que nos calcule las revoluciones por minuto de un disco con muescas que he realizado yo mismo en casa.

El disco encoder está hecho de papel y está formado por cuatro muescas, todo ello atravesado por una varilla de madera (se adjunta una imagen del disco al final de este documento).
Para poner a prueba a este circuito, es muy sencillo: comienza la ejecución del programa y lo que hacemos es comenzar a girar el disco encoder de tal manera que las muescas
pasen por el "hueco" del optointerruptor que hemos mencionado anteriormente, calculando así las revoluciones por minuto en función del número de muescas que tenga nuestro
disco y del tiempo que queremos que pase para que imprima las revoluciones por minuto en ese momento.

### 4. Contenido multimedia sobre esta práctica

Imagen: Disco encoder

<p align="center">
  <img src="https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%205:%20Construcci%C3%B3n%20de%20un%20encoder%20incremental%20usando%20un%20sensor%20%C3%B3ptico/media/Imagen%20Disco%20Pr%C3%A1ctica%205.jpg?raw=true">
</p>

Imagen: Montaje del circuito

<p align="center">
  <img src="https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%205:%20Construcci%C3%B3n%20de%20un%20encoder%20incremental%20usando%20un%20sensor%20%C3%B3ptico/media/Imagen%20Circuito%20Pr%C3%A1ctica%205.jpg?raw=true">
</p>

[Vídeo: Ejecución de la práctica](https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%205%3A%20Construcci%C3%B3n%20de%20un%20encoder%20incremental%20usando%20un%20sensor%20%C3%B3ptico/media/Video%20Ejecuci%C3%B3n%20Pr%C3%A1ctica%205.mp4)
