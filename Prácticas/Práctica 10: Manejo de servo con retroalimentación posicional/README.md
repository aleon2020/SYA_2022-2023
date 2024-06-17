# Resumen Sensores y Actuadores prácticas primer cuatrimestre

# Alberto León Luengo

## Grado de Ingeniería en Robótica Software

## Práctica 10: Manejo de servo con retroalimentación posicional

### 1. Funcionamiento y conexión del servo

Para poder programar el servo, y como siempre, lo primero es conocer cómo funciona, y para ello lo mejor
es leerse las especificaciones (adjuntas a esta práctica). De estas podemos extraer información muy útil, por
ejemplo los siguientes aspectos:

Pin de señal de retroalimentación de posición: cable amarillo.

Periodo de envı́o de señal de control: 20 ms.

Ancho de pulso de la señal: p.ej. 1280 − 1480µs para girar en un sentido.

Periodo de señal de retroalimentación (tCycle): 1/910 Hz (1,1 ms).

Ciclo de trabajo de tCycle: 2,9 − 91,7 %

### 2. Opinión personal sobre esta práctica

Esta práctica me ha parecido bastante sencilla de realizar y me ha llevado muy poco tiempo realizar los programas que se me pedían. En mi opinión, es una de las prácticas de todas las que hemos realizado este curso que más me ha gustado y parecido más interesante. A continuación explico como he llevado a cabo los dos ejercicios que se nos pedían:

En el primer ejercicio he utilizado los valores del 1 al 0 a leer por teclado para asignar diferentes velocidades a ambos sentidos de giro del servo. Como bien se especifica en los comentarios del programa, he usado los números del 1 al 5 para ir de la velocidad más baja a la más alta cuando el servo gira en sentido horario, al contrario que para el sentido antihorario, donde he establecido los números del 0 al 6 (en ese orden), de menor a mayor velocidad, obteniendo el siguiente esquema de velocidades: 1 < 2 < 3 < 4 < 5 = 6 > 7 > 8 > 9 > 0, siendo del 1 al 5 los valores que giran en sentido horario (velocidad mínima 1 y velocidad máxima 5) y del 6 al 0 los que giran en sentido antihorario (velocidad mínima 0 y velocidad máxima 6).

Para el segundo ejercicio he utilizado los mismos métodos que en el apartado anterior, solo que en este caso, lo único que he modificado con respecto al anterior es que solo he establecido un sentido de giro (sentido horario), y que dichos valores que marcan esos rangos de velocidad los he guardado en 5 variables diferentes (MIN_SPEED para la velocidad mínima, MAX_SPEED para la velocidad máxima, y otras 3 variables más que he utilizado para valores intermedios de la velocidad).

Como se muestra en la imagen adjunta, he conectado el able rojo a 5V, el negro a GND y el blanco a un puerto GPIO determinado (en mi caso he utilizado el 2).

Aunque se pidan 2 ejercicios, solo he subido uno, ya que el funcionamiento de los programas es el mismo, solo cambiando las teclas que hay que pulsar para obtener diferentes valores de la velocidad en diferentes sentidos (básicamente 
el vídeo se adjunta para demostrar que el servo funciona).

### 3. Contenido multimedia sobre esta práctica

Imagen: Montaje del circuito de la práctica 10

<p align="center">
  <img src="https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%2010:%20Manejo%20de%20servo%20con%20retroalimentaci%C3%B3n%20posicional/media/Imagen%20Circuito%20Pr%C3%A1ctica%2010.jpg?raw=true">
</p>

[Vídeo: Ejecución de la práctica 10](https://github.com/aleon2020/SYA_2022-2023/raw/main/Pr%C3%A1cticas/Pr%C3%A1ctica%2010:%20Manejo%20de%20servo%20con%20retroalimentaci%C3%B3n%20posicional/media/Video%20Ejecuci%C3%B3n%20Pr%C3%A1ctica%2010.mp4)
