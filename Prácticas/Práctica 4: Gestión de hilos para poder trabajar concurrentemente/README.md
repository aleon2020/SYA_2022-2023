# Práctica 4: Gestión de hilos para poder trabajar concurentemente

## 1. Thread Management in Python

### 1.1 The Hello World of Thread Management

Code Explanation: When running this code, the last message ("Main thread runs its course and terminates") is displayed first, since it is in the main program. Finally, a thread called "thread1" is created and assigned to the task function, which prints the message "New thread task done" to the screen.

```py
import threading
import time

def tarea():
  time.sleep (1) # simula thread ocupado en gran carga de trabajo
  print ("Tarea del nuevo hilo hecha")

hilo1 = threading.Thread(target=tarea)
hilo1.start()

print ("Hilo principal sigue su curso y termina")
```

### 1.2 Using join to wait for a thread to finish

Code explanation: When running this program, two threads ("thread1" and "thread2") have been created, and they execute what is inside the task function. However, due to the two lines in which the names of the two threads appear next to .join(), they have to wait for one of the two to finish executing before the next one can do so. Since the task function consists of an iterator that ranges from 0 to 4, the program output shows how thread1 and thread2 alternate execution (that is, once thread1 has executed its first iteration, it does not execute the second iteration until thread2 has executed its first iteration, and so on). Finally, the last message in the code is printed ("Main thread continues and terminates").

```py
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

### 1.3 Synchronization

Code Explanation: When running this code, we find several similarities with the previous section. We have two threads (thread1 and thread2) and a task function, which works the same as in the previous section (an iterator that goes from 0 to 4, but with some differences). In the previous section, we could see how thread1 and thread2 alternated in each iteration. The difference here is that thread1 executes all its iterations first (from 0 to 4), and thread2 will not begin executing until thread1 finishes ALL of its iterations (this is due to the .append we added to the vector containing all the threads, passing each thread as a parameter). Once thread1 finishes, thread2 will execute all of its iterations, showing them all consecutively due to the .join that each thread has in the code (instead of alternating the iterations as it happened in the previous section, they only alternate in order, that is, first the complete thread1 is executed and then thread2), and finally it prints the last line of code on the screen ("main thread continues its course and finishes").

```py
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

## 2. Personal opinion on this exercise

I had to dedicate considerably more time to completing this exercise compared to the previous ones. However, once I understood how all the thread types introduced in this exercise worked, it was much easier and more manageable.

For the sininterrupcionesmejorado.py and interrupcioneventmejorado.py exercises, I used the basic thread mechanism to operate the two LEDs, each with its respective button.

However, for the second exercise, since trying to run everything within a single program didn't work for me, I decided to use object-oriented programming (based on the threadsPOO.py program), which was provided in class. To do this, I created a separate program for each thread (one for the red thread and one for the green thread). This way, it worked for me, running each program in two different terminals, ensuring the program behaves exactly the same as the previous two.

## 3. Multimedia Content

<p align="center">
  <img src="https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%204:%20Gesti%C3%B3n%20de%20hilos%20para%20poder%20trabajar%20concurrentemente/media/Imagen%20Circuito%20Pr%C3%A1ctica%204.jpg?raw=true">
</p>

[PRACTICE 4 EXECUTION VIDEO](https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%204%3A%20Gesti%C3%B3n%20de%20hilos%20para%20poder%20trabajar%20concurrentemente/media/Video%20Ejecuci%C3%B3n%20Pr%C3%A1ctica%204.mp4)
