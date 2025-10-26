# Práctica 5: Construcción de un encoder incremental usando un sensor óptico

## 1. The optical encoder

```bash
res = (pi*D)/(2*ar)
```

This is the general formula used to determine the resolution of an encoder, where we can distinguish: res (encoder resolution), D (disk diameter), ar (width of each slot).

## 2. Voltage divider for the transistor

```bash
Vout = Vin * ((R2) / (R1 + R2))
```
			
From this formula we can obtain the desired output voltage of 3.3 V starting from an input voltage of 5 V (if R2 is twice R1, as can be seen in the formula above).

```bash
Si R2 = 2*R1 => Vout = 2/3 * Vin = 2/3 * 5 V = 3.3 V
```
	
In our case, R1 will be the 10,000 ohm resistor and R2 will be the 20,000 ohm resistor.

## 3. Personal opinion on this exercise

Of all the exercises I've completed in the subject, this one was the one that took the most time and effort to develop, as it was the first exercise in which we weren't provided with a connection diagram. Added to this, the exercise's requirements are quite complex compared to what we've been asked to do on other occasions.

To complete this exercise, I used the opto-switch, which contains an infrared sensor in the "gap" between the E and D that detects when that barrier has been broken. In our case, we can create a program that calculates the revolutions per minute of a notched disc that I made myself at home.

The encoder disc is made of paper and consists of four notches, each with a wooden rod passing through it (an image of the disc is attached at the end of this document).
To test this circuit, it's very simple: start the program and rotate the encoder disc so that the notches pass through the "gap" of the opto-switch mentioned above, thus calculating the revolutions per minute based on the number of notches on our disc and the time we want to wait for it to print the revolutions per minute at that moment.

## 4. Multimedia Content

<p align="center">
  <img src="https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%205:%20Construcci%C3%B3n%20de%20un%20encoder%20incremental%20usando%20un%20sensor%20%C3%B3ptico/media/Imagen%20Disco%20Pr%C3%A1ctica%205.jpg?raw=true">
</p>

<p align="center">
  <img src="https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%205:%20Construcci%C3%B3n%20de%20un%20encoder%20incremental%20usando%20un%20sensor%20%C3%B3ptico/media/Imagen%20Circuito%20Pr%C3%A1ctica%205.jpg?raw=true">
</p>

[PRACTICE 5 EXECUTION VIDEO](https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%205%3A%20Construcci%C3%B3n%20de%20un%20encoder%20incremental%20usando%20un%20sensor%20%C3%B3ptico/media/Video%20Ejecuci%C3%B3n%20Pr%C3%A1ctica%205.mp4)
