# Práctica 3: Uso de interrupciones para leer valores de un sensor

## 1. Interrupts or Events

Callback: A special function that is passed to another function as an argument.

Callback example:

```py
def botonPresionado():
	print("El botón ha sido presionado")
GPIO.add_event_detect(BUTTON_GPIO,GPIO.FALLING,
  callback = botonPresionado, bounceTime = 100)
```

## 2. Method 0: Asking for the value continuously

```py
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

## 3. Method 1: Interrupts with wait_for_edge

```py
import RPi.GPIO as GPIO

pulsadorGPIO = 16

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pulsadorGPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        GPIO.wait_for_edge(pulsadorGPIO, GPIO.RISING)
        print("El boton se ha pulsado")
```

## 4. Method 2: Interrupts with add_event_detect

```py
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

## 5. Personal opinion/explanation on this exercise

The solution to exercise 1 is very simple: When running the program, I noticed that the "pressed" message was displayed more than once when I had actually only pressed the button once. To do this, the only thing I modified from the original program was that on the last line of the program, inside the infinite loop, I added a debounce system (mentioned as such in the statement of this exercise), which consists of a time.sleep(0.1). The lower the frequency, the greater the relief for the processor. However, using this method, we will always miss some checks.

On the other hand, when discussing exercise 2 and its respective sections, I haven't been able to find a correct solution. To create the program outlined in the statement, it would be necessary to create more than one thread for each LED, since multiple LEDs cannot be managed with their respective buttons within the same thread. In the following exercise, we'll solve this problem in a much more appropriate way, since exercise 4 introduces threads and some of the most common examples of this programming structure in Python.

Continuing with this exercise, in the interruptedge and sininterrupted sections, I found that, when it came to having infinite loops, I tried a method that consisted of duplicating the code and having one for each LED that we were going to operate, but when it came to writing it and trying to execute it, I realized that the copy of the code was "shadowed" with respect to the first, and the program only acted as if it took into account one of the two buttons and one of the two pushbuttons. And finally, speaking of the remaining section (interruptevent), when looking at the structure and trying to execute it, I observed that the functions and the way in which the code is written seem prepared to operate only one LED, so I have not been able to solve this section either.

In short, I wasn't able to complete this exercise because obtaining a correct solution requires several wires. This allows me to more easily and accurately manipulate the LEDs with their respective pushbuttons. The repository for this exercise includes the three programs that were previously provided, as well as the "solution" I provided to the exercises, explained in the previous paragraph.

In the next exercise, we'll be able to solve these exercises correctly using wires.
