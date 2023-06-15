# Resumen Sensores y Actuadores prácticas primer cuatrimestre

# Alberto León Luengo

## Grado de Ingeniería en Robótica Software

## Práctica 3: Uso de interrupciones para leer valores de un sensor

### 1. Interrupciones o eventos

Callback: Función especial que se pasa a otra como argumento. Ejemplo de callback:

```
def botonPresionado():
	print("El botón ha sido presionado")
GPIO.add_event_detect(BUTTON_GPIO,GPIO.FALLING,
  callback = botonPresionado, bounceTime = 100)
```

### 2. Método 0: Pidiendo el valor contínuamente

```
import time
import RPi.GPIO as GPIO

pulsadorGPIO = 16

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)

    # Activamos resistencia pull_up_down en modo HIGH, esto es:
    # - HIGH: estado por defecto del GPIO (no se ha pulsado).
    # - LOW: estado del GPIO cuando se ha pulsado el boton.
    GPIO.setup(pulsadorGPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    pulsado = False

    while True:
        if not GPIO.input(pulsadorGPIO): # la lectura siempre da 1 (HIGH/True) excepto al pulsar,
                                         # y solo en ese instante, que da 0 (LOW/False)
            if not pulsado: # con esta variable evitamos considerar más de una vez una pulsación;
                            # puede que se lea +1 vez el estado del pin antes de cambiar su estado
                            # Este fenómeno se conoce como rebote (o bounce). Algunas funciones
                            # permiten establecer un parámetro denominado "bouncetime"
                print("El boton se ha pulsado")
                pulsado = True
        else:
            pulsado = False

        time.sleep(0.1) # si pulsamos rápida/ veremos que algunas se escapan...
```

### 3. Método 1: Interrupciones con wait_for_edge

```
import RPi.GPIO as GPIO

pulsadorGPIO = 16

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pulsadorGPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        GPIO.wait_for_edge(pulsadorGPIO, GPIO.RISING)
        print("El boton se ha pulsado")
```

### 4. Método 2: Interrupciones con add_event_detect

```
import signal
import sys
import RPi.GPIO as GPIO

pulsadorGPIO = 16

# señal y estado cuando se produjo la interrupción
def callbackSalir (senial, cuadro):
	# limpieza de los recursos GPIO antes de salir
    GPIO.cleanup ()
    sys.exit(0)

def callbackBotonPulsado (canal):
    print("El boton se ha pulsado")

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pulsadorGPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(pulsadorGPIO, GPIO.FALLING, 
      callback=callbackBotonPulsado, bouncetime=500) # expresado en ms.
    
	# callback para CTRL+C
    signal.signal(signal.SIGINT, callbackSalir)
	# esperamos por hilo/callback CTRL+C antes de acabar
    signal.pause()
```

### 5. Opinión personal/explicación sobre esta práctica

La solución al ejercicio 1 es muy sencilla: Al ejecutar el programa me he percatado de que se muestra más de una vez el mensaje de pulsado cuando realmente solo he pulsado el botón una vez. Para ello, lo único que he modificdo del programa original es que en la última línea del programa, dentro del bucle infinito, he añadido un sistema antirebote (mencionado así en el enunciado de esta práctica), que consiste en un time.sleep(0.1), ya que cuanto menor es la frecuencia, mayor será el alivio para el procesador, sin embargo, por este método siempre nos perderemos algunas comprobaciones. 

Por otro lado, a la hora de hablar del ejercicio 2, con cada uno de sus respectivos apartados, no he conseguido encontrar ninguna solución correcta, ya que para realizar el programa que se nos plantea en el enunciado se necesitaría crear más de un hilo para cada led, ya que no se pueden manejar varios leds con su respectivo botón dentro de  un mismo hilo. En la siguiente práctica resolveremos este problema de una forma mucho más adecuada, ya que lo que se hace en la práctica 4 es introducir los hilos, y algunos de los ejemplos más comunes sobre esta estructura de programación en Python.

Siguiendo con este ejercicio, en los apartados de interrupcionedge y sininterrupciones me he encontrado con que, a la hora de tener bucles infinitos, lo he intentado por un método que consiste en duplicar el código y tener uno por cada led que vayamos a hacer funcionar, pero a la hora de escribirlo e intentar ejecutarlo me he percatado de que la copia del código quedaba como "ensombrecida" respecto a la primera, y el programa solo actúa como si tuviera en cuenta uno de los dos botones y uno de los dos pulsadores. Y por último, hablando del apartado de restante (interrupcionevent), al ver la estructura e intentar ejecutarlo he observado que las funciones y la manera en la que está escrito el código parece preparada para hacer funcionar a solo un led, por lo que tampoco he conseguido resolver este apartado.

Resumiendo, no he podido realizar esta práctica, ya que para obtener una solución correcta se necesitan varios hilos, y de esta manera poder manejar con más soltura y precisión los leds con sus respectivos pulsadores, en el repositorio de esta práctica se incluyen los tres programas que ya se nos han ofrecido en un principio, y por otro lado, la "solución" que he dado a los ejercicios y que está explicada en el anterior párrafo.

En la siguiente práctica ya podremos resolver estos ejercicios correctamente mediante el uso de hilos.
