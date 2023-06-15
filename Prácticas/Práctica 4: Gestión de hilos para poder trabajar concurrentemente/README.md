# Resumen Sensores y Actuadores prácticas primer cuatrimestre

# Alberto León Luengo

## Grado de Ingeniería en Robótica Software

## Práctica 4: Gestión de hilos para poder trabajar concurentemente

## 1. Gestión de hilos en Python

### 1.1 El holamundo de la gestión de hilos

Explicación del código: Al ejecutar este código, primero se muestra el último mensaje ("Hilo principal sigue su curso y termina") ya que este está en el programa principal, y por último se ha creado un hilo llamado "hilo1" asignado a la función tarea, que consiste en imprimir por pantalla el mensaje "Tarea del nuevo hilo hecha".

```
import threading
import time

def tarea():
  time.sleep (1) # simula thread ocupado en gran carga de trabajo
  print ("Tarea del nuevo hilo hecha")

hilo1 = threading.Thread(target=tarea)
hilo1.start()

print ("Hilo principal sigue su curso y termina")
```

### 1.2 Uso del join para esperar a que termine un hilo

Explicación del código: Al ejecutar este programa, lo que ha ocurrido es que se han creado dos hilos ("hilo1" e "hilo2"), y lo que hacen es ejecutar lo que hay dentro de la función tarea. Sin embargo, debido a las las dos líneas en las que aparece el nombre de los dos hilos junto a .join(), hace que éstos esperen a que uno de los dos termine de ejecutarse para que lo haga el siguiente, y como la función tarea consiste en un iterador que va desde el 0 hasta el 4, hace que en el resultado del programa se pueda observar como hilo1 e hilo2 se van alternando en la ejecución (es decir, una vez que hilo1 ha ejecutado su primera iteración, éste no ejecuta la segunda iteración hasta que hilo2 no haya ejecutado su primera iteración,y así sucesivamente). Y por último, se imprime el último mensaje que aparece en el código ("Hilo principal sigue su curso y termina").

```
import threading
import time

def tarea (nombre):
  contador = 0
  while contador < 5:
    time.sleep(0.3)
    print (nombre + " ejecutando iteracion n.º " + str(contador))
    contador += 1

hilo1 = threading.Thread(target=tarea, args=("hilo1",))
hilo1.start()

hilo2 = threading.Thread(target=tarea, args=("hilo2",))
hilo2.start()

hilo1.join() # esperamos a que hilo1 termine
hilo2.join() # idem con hilo2

print ("Hilo principal sigue su curso y termina")
```

### 1.3 Sincronización

Explicación del código: Al ejecutar este código, podemos encontrarnos con varias similitudes respecto al apartado anterior. Tenemos dos hilos (hilo1 e hilo2) y una función tarea, con el mismo funcionamiento que en el apartado anterior (iterador que va del 0 al 4, pero con algunas diferencias). En el apartado anterior, podíamos observar cómo hilo1 e hilo2 se iban alternando en cada iteración, la diferencia es que aquí lo que ocurre es que hilo1 ejecuta primero todas sus iteraciones (de 0 a 4) e hilo2 no comenzará a ejecutarse hasta que hilo1 no termine TODAS sus iteraciones (esto se debe al .append que hemos añadido al vector que contiene todos los hilos, pasándole como parámetro cada hilo). Una vez hilo1 termine, hilo2 ejecutará todas sus iteraciones, mostrándolas todas de forma consecutiva debido al .join que tiene cada hilo en el código (en vez de alternarse las iteraciones como ocurría en el apartado anterior, solo se alternan en orden, es decir, primero se ejecuta el hilo1 completo y después el hilo2), y ya por último imprime por pantalla la última línea de código ("hilo principal sigue su curso y termina").

```
import threading
import time

def tarea (nombre):
  testigo.acquire() # LOCK - inicio zona de exclusión mutua (mutex)
  contador = 0
  while contador < 5:
    time.sleep(0.3)
    print (nombre + " ejecutando iteracion n.º " + str(contador))
    contador += 1
  testigo.release() # UNLOCK - fin de zona de exclusión mutua (mutex)

testigo = threading.Lock() # creamos el testigo
misHilos = [] # vector de hilos

hilo1 = threading.Thread(target=tarea, args=("hilo1",))
hilo1.start()

hilo2 = threading.Thread(target=tarea, args=("hilo2",))
hilo2.start()

misHilos.append(hilo1) # añado los hilos lanzados al vector
misHilos.append(hilo2)

# el vector es muy cómodo para trabajar con muchos threads. Ej.: hacer join
for h in misHilos:
   h.join()

print ("Hilo principal sigue su curso y termina")
```

### 2. Opinión personal sobre esta práctica

Para la realizacion de esta practica he tenido que dedicarle bastante mas tiempo comparado con las anteiores. Sin embargo, cuando he comprendido el funcionamiento de todos los tipos de hilos que se nos introducen en esta practica me ha sido mucho mas llevadero y sencillo.

Para los ejercicios de sininterrupcionesmejorado.py e interrupcioneventmejorado.py he utilizado el mecanismo basico de hilos para hacer funcionar los dos leds, cada uno con su respectivo boton.

Sin embargo, para el segundo ejercicio, ya que al tratar de ejecutar todo dentro de un mismo programa, no me funcionaba, asi que he decidido tirar por hacerlo con programacion orientada a objetos (partiendo del programa threadsPOO.py), que se nos facilito en clase. Para ello, he creado un programa distinto por hilo (uno para el rojo y otro para el verde), por lo que de esta manera me ha funcionado, ejecutando cada programa en dos terminales distintas, haciendo que el programa tenga el mismo comportamiento que los dos anteriores.

### 3. Contenido multimedia sobre esta práctica

Imagen: Montaje del circuito de la práctica 4

https://urjc-my.sharepoint.com/:i:/g/personal/a_leon_2020_alumnos_urjc_es/EdMIcIaazIFCgMAxPlKKoigBv3uuPeI07CDvZblA_eDQlw?e=ZBu08D

Vídeo: Ejecución de la práctica 4

https://urjc-my.sharepoint.com/:v:/g/personal/a_leon_2020_alumnos_urjc_es/EUgzfst5cEtEl9fc8cKTZJIB2uQFNCbrKPuWaxPJQ4t4JQ?e=wl1woY
