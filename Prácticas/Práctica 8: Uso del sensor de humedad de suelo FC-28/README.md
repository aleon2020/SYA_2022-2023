# Resumen Sensores y Actuadores prácticas primer cuatrimestre

# Alberto León Luengo

## Grado de Ingeniería en Robótica Software

## Práctica 8: Uso del sensor de humedad de suelo FC-28

### 1. Pines del módulo M393

En este módulo se pueden apreciar cuatro pines (a su vez, con algunas siglas):

VCC: Es el pin al cual conectar uno de los pines 3v3 del raíl GPIO.
GND: Directamente a un pin GPIO de toma de tierra.
DO: Las siglas provienen de Digital Output.
AO: Este pin es el alternativo al anterior, cuyas siglas significan Analog Output.

### 2. Opinión personal sobre esta práctica

Esta práctica me ha parecido bastante sencilla de realizar, ya que simplemente con ver la imagen del esquema de conexión, no me ha sido necesaria la 
utlización de la protoboard para realizar esta práctica.

En mi caso, he creado dos programas, el primero se llama "sensordehumedad.py", cuyo principal funcionamiento es leer los valores del sensor de 
humedad y mostrar por pantalla cuando el mismo se encuentra en estado húmedo o seco, y una vez termina de ejecutarse el programa, coge esos valores
y los guarda en un fichero al que he llamado "registrodecambios.csv", que, básicamente lo que hace es mostrar si el sensor se encuentra en estado de humedad
o sequía (en mi caso, se imprimen esos valores cada dos segundos).

Y por último, el segundo programa, al que he llamado "graficasensordehumedad.py", que consiste en tomar los valores del fichero "registrodecambiosdehumedad.csv", y 
los inserta en una gráfica mediante el uso de algunas librerías que no había usado hata ahora en python, como son las librerías pandas y matplotlib, que mediante varias 
búsquedas por internet me han parecido la solución más viable para resolver este problema. Este programa lo que hace es, básicamente, coger esos valores (los que se incluyen 
dentro de la columna Timestamp y la columna Humedad), y los representa en una gráfica (para poder representar cuando el sensor se encuentra en estado húmedo o seco he asignado a 
dichos estados las variables 1 y 0, respectivamente).

NOTA: En la línea 16 de este último programa podemos cambiarle el atributo a plt para que pueda mostrarnos la gráfica de diferentes maneras (gráfico de barras, puntos, líneas, ...).

### 3. Contenido multimedia sobre esta práctica

Imagen: Montaje del circuito

<p align="center">
  <img src="https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%208:%20Uso%20del%20sensor%20de%20humedad%20de%20suelo%20FC-28/media/Imagen%20Circuito%20Pr%C3%A1ctica%208.jpg?raw=true">
</p>

[Vídeo: Ejecución de la práctica](https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%208%3A%20Uso%20del%20sensor%20de%20humedad%20de%20suelo%20FC-28/media/Video%20Ejecuci%C3%B3n%20Pr%C3%A1ctica%208.mp4)
