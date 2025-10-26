# Práctica 9: Uso del sensor de presión con el de presencia

## 1. The FSR presence sensor

To use the presence sensor, I used a fairly simple connection diagram, which was already provided in the instructions for this exercise. It basically consists of reading the sensor values ​​every so often (for a short period of time) (LOW if nothing has passed near the sensor and HIGH if something has moved or passed near the sensor). All of this is saved in the file presencia.py.

<p align="center">
  <img src="https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%209:%20Uso%20del%20sensor%20de%20presi%C3%B3n%20junto%20con%20el%20de%20presencia/media/Imagen%20Circuito%20Pr%C3%A1ctica%209%20Ejercicio%201%20Apartado%201.jpg?raw=true">
</p>

[PRACTICE 9 EXECUTION VIDEO EXERCISE 1 POINT 1](https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%209%3A%20Uso%20del%20sensor%20de%20presi%C3%B3n%20junto%20con%20el%20de%20presencia/media/Video%20Ejecuci%C3%B3n%20Pr%C3%A1ctica%209%20Ejercicio%201%20Apartado%201.mp4)

## 2. The FSR Pressure Sensor

As with the previous example, the connection diagram for the sensor has already been provided in the description, and the code I've implemented is basically the same as the one I used to read the values ​​from the presence sensor (LOW if the circular part of the sensor is not being pressed, and HIGH if it is being pressed). All of this is saved in the file fuerza.py.

<p align="center">
  <img src="https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%209:%20Uso%20del%20sensor%20de%20presi%C3%B3n%20junto%20con%20el%20de%20presencia/media/Imagen%20Circuito%20Pr%C3%A1ctica%209%20Ejercicio%201%20Apartado%202.jpg?raw=true">
</p>

[PRACTICE 9 EXECUTION VIDEO EXERCISE 1 POINT 2](https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%209%3A%20Uso%20del%20sensor%20de%20presi%C3%B3n%20junto%20con%20el%20de%20presencia/media/Video%20Ejecuci%C3%B3n%20Pr%C3%A1ctica%209%20Ejercicio%201%20Apartado%202.mp4)

## 3. Personal opinion on this practice

This opinion is more focused on section 2 of this practice, where we are asked to design an intelligent lighting system using presence and pressure sensors, adding the implementation of an LED. This LED will turn on when the presence sensor displays HIGH on its output, all as long as the pressure sensor is also in HIGH mode. In this case, we will use this sensor as a button (if it is in LOW mode, nothing works, but if it is in HIGH mode, the presence sensor can only work at that instant, and it will turn on the LED every time it detects presence).

This section of the exercise was more complicated for me to complete because I had to use threads and the complexity of synchronizing the execution of all the elements in the circuit. As you can see in the video, the program begins to run. The pressure sensor functions as a button (when we press it, the presence sensor will activate for a specific time, in my case 30 seconds). When its output is HIGH, meaning it has detected something, the red LED will turn on, and when we have been passing an object near the presence sensor for a long time and it doesn't detect anything, it means that the previously set time (30 seconds) has expired. Therefore, we must press the pressure sensor again, which acts as a button, so the presence sensor can do its job.

## 4. Multimedia Content

<p align="center">
  <img src="https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%209:%20Uso%20del%20sensor%20de%20presi%C3%B3n%20junto%20con%20el%20de%20presencia/media/Imagen%20Circuito%20Pr%C3%A1ctica%209%20Ejercicio%202.jpg?raw=true">
</p>

[PRACTICE 9 EXECUTION VIDEO EXERCISE 2](https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%209%3A%20Uso%20del%20sensor%20de%20presi%C3%B3n%20junto%20con%20el%20de%20presencia/media/Video%20Ejecuci%C3%B3n%20Pr%C3%A1ctica%209%20Ejercicio%202.mp4)
