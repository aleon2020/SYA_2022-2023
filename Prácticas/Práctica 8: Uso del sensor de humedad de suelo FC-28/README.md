# Práctica 8: Uso del sensor de humedad de suelo FC-28

## 1. M393 Module Pins

This module displays four pins (with acronyms):

- VCC: This pin connects to one of the 3v3 pins on the GPIO rail.
- GND: Directly to a GPIO ground pin.
- DO: This acronym stands for Digital Output.
- AO: This pin is an alternative to the previous one, which stands for Analog Output.

## 2. Personal Opinion on this Practice

I found this practice to be quite simple to complete, since simply looking at the connection diagram, I didn't need to use a breadboard to complete this practice.

In my case, I created two programs. The first is called "humiditysensor.py." Its main function is to read the values ​​from the humidity sensor and display on the screen whether it is wet or dry. Once the program finishes running, it takes those values ​​and saves them in a file called "changelog.csv." This basically shows whether the sensor is wet or dry (in my case, these values ​​are printed every two seconds).

Finally, the second program, which I called "humusensorgraph.py," takes the values ​​from the "humiditychangelog.csv" file and inserts them into a graph using some libraries I hadn't used before in Python, such as pandas and matplotlib. After several internet searches, these libraries seemed to me to be the most viable solution for this problem. What this program does is basically take those values ​​(those included in the Timestamp column and the Humidity column), and represent them in a graph (to be able to represent when the sensor is in a wet or dry state I have assigned the variables 1 and 0 to said states, respectively).

**NOTE**: On line 16 of this last program we can change the attribute to plt so that it can show us the graph in different ways (bar graph, points, lines, ...).

## 3. Multimedia Content

<p align="center">
  <img src="https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%208:%20Uso%20del%20sensor%20de%20humedad%20de%20suelo%20FC-28/media/Imagen%20Circuito%20Pr%C3%A1ctica%208.jpg?raw=true">
</p>

[PRACTICE 8 EXECUTION VIDEO](https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%208%3A%20Uso%20del%20sensor%20de%20humedad%20de%20suelo%20FC-28/media/Video%20Ejecuci%C3%B3n%20Pr%C3%A1ctica%208.mp4)
