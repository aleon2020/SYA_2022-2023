# Resumen Sensores y Actuadores prácticas primer cuatrimestre

# Alberto León Luengo

## Grado de Ingeniería en Robótica Software

## Práctica 6: Uso del sensor ultrasonidos para medir distancias

### 1. Introducción

Periodo de tiempo transcurrido entre la emisión de onda y la recepción de su eco, representado por la ecuación:
						
						d = 1/2*Vs*t

Donde d (distancia del emisor-receptor al objeto, en metros), Vs (velocidad del sonido) y t (tiempo transcurrido, en segundos).

### 2. Sensor de ultrasonidos HC-SR04

EL sensor de ultrasonido que vamos a utilizar para esta práctica consta de 4 pines: VCC (pin de alimentación del sensor de 5V), Trig (pin de disparo/salida que habilita la medición del sensor), echo (señal de entrada al sistema), GND (pin negativo de alimentación o toma de tierra).

Comienzo de la medición: Primero se aplica un pulso o señal en alto a través del pin Trig, con una duración de al menos 10 microsegundos. Después, el sensor envía una serie de 8 pulsos de 40 KHz, poniendo el pin de Echo en alto, permaneciendo en este estado hasta que se reciba el eco de los pulsos de 40 KHz. Conclusión: Este tiempo es el que se toma en cuenta para estimar la distancia a la que se encuentra el objeto.

### 3. Cálculo de la distancia al objeto

Fórmula que refleja la distancia con la velocidad:

					v = s/t <=> d = v*t
					
Considerando la velocidad del sonido en el aire de 343 m/s, nos queda la ecuación:

					d = v*t => d = 343*t
					
En nuestro caso, como estamos usando el sensor en Reflexión directa (d es el doble de la distancia real dr entre el sensor y el objeto), donde nos queda la ecuación:

				  d = 343*t => dr = 171,5*t
				  
Por último, adaptamos a las unidades que se manejan en el problema en particular (centímetros y microsegundos), para que nos resulte más cómodo trabajar con ella.

				dr = 171,5*t = 17150*10^-6*t

### 4. Opinión personal sobre esta práctica

El desarrolllo de esta práctica me ha parecido bastante sencillo, donde las únicas complicaciones que me he podido encontrar han sido a la hora de buscar el esquema de conexión ideal para el sensor de
ultrasonido. El esquema de conexión y el funcionamiento del programa son bastante sencillos y visibles, ya que por un lado, el sensor de distancia hace su tarea habitual leyendo cada segundo los valores de 
la distancia a la que está el objeto, y por otro lado he implementado tres leds de diferentes colores asociados a si el objeto se encuentra a una distancia lejana (led verde), a una distancia media (led
amarillo), o a una distancia bastante cercana (led rojo).

### 5. Contenido multimedia sobre esta práctica

Imagen: Montaje del circuito de la práctica 6

https://urjc-my.sharepoint.com/:i:/g/personal/a_leon_2020_alumnos_urjc_es/Eb1DveJvn6FBmYAZZyQEfzEB3FanTLZMtr7cfcFtZc2etQ?e=wuL6rC

Vídeo: Ejecución de la práctica 6

https://urjc-my.sharepoint.com/:v:/g/personal/a_leon_2020_alumnos_urjc_es/ERYko9nWNyFBl1-E1CbpMIYBvTa2lGB4XcGpyPifXK2N7Q?e=07xBTw
