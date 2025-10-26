# Práctica 6: Uso del sensor ultrasonidos para medir distancias

## 1. Introduction

The period of time elapsed between the emission of a wave and the reception of its echo, represented by the equation:
						
```bash
d = 1/2*Vs*t
```

Where d (distance from the transmitter-receiver to the object, in meters), Vs (speed of sound), and t (elapsed time, in seconds).

## 2. HC-SR04 Ultrasonic Sensor

The ultrasonic sensor we will use for this exercise consists of 4 pins: VCC (5V sensor power pin), Trig (trigger/output pin that enables sensor measurement), echo (input signal to the system), and GND (negative power pin or ground).

Measurement start: First, a high pulse or signal is applied through the Trig pin, lasting at least 10 microseconds. The sensor then sends a series of eight 40 kHz pulses, setting the Echo pin high. The signal remains high until the echo of the 40 kHz pulses is received. Conclusion: This time is used to estimate the distance to the object.

## 3. Calculating the distance to the object

Formula that reflects distance versus speed:

```bash
v = s/t <=> d = v*t
```
					
Considering the speed of sound in air of 343 m/s, we have the equation:

```bash
d = v*t => d = 343*t
```
					
In our case, since we are using the sensor in Direct Reflection (d is twice the actual distance dr between the sensor and the object), where we have the equation:

```bash
d = 343*t => dr = 171,5*t
```
				  
Finally, we adapt it to the units used in the particular problem (centimeters and microseconds) to make it more convenient for us to work with.

```bash
dr = 171,5*t = 17150*10^-6*t
```

## 4. Personal opinion on this practice

I found the development of this practice to be quite simple, and the only complications I encountered were in finding the ideal connection diagram for the ultrasound sensor. The connection diagram and the program's operation are quite simple and straightforward. On the one hand, the distance sensor performs its usual task, reading the distance values ​​to the object every second. On the other hand, I implemented three LEDs of different colors associated with whether the object is at a far distance (green LED), a medium distance (yellow LED), or a fairly close distance (red LED).

## 5. Multimedia Content

<p align="center">
  <img src="https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%206:%20Uso%20del%20sensor%20de%20ultrasonidos%20para%20medir%20distancias/media/Imagen%20Circuito%20Pr%C3%A1ctica%206.jpg?raw=true">
</p>

[PRACTICE 6 EXECUTION VIDEO](https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%206%3A%20Uso%20del%20sensor%20de%20ultrasonidos%20para%20medir%20distancias/media/Video%20Ejecuci%C3%B3n%20Pr%C3%A1ctica%206.mp4)
