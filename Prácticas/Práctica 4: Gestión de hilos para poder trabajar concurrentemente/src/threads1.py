import threading
import time

def tarea():
  time.sleep (1) # simula thread ocupado en gran carga de trabajo
  print ("Tarea del nuevo hilo hecha")

hilo1 = threading.Thread(target=tarea)
hilo1.start()

print ("Hilo principal sigue su curso y termina")
