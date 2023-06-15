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
