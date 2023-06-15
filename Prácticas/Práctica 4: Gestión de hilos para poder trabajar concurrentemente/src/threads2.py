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
