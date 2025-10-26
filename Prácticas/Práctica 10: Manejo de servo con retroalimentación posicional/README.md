# Práctica 10: Manejo de Servo con Retroalimentación Posicional

## 1. Servo Operation and Connection

To program the servo, and as always, the first step is to understand how it works. To do this, it's best to read the specifications attached to this lab. We can glean very useful information from these specifications, such as the following:

- Position feedback signal pin: yellow wire.

- Control signal transmission period: 20 ms.

- Signal pulse width: e.g., 1280 − 1480 µs for one-way rotation.

- Feedback signal period (tCycle): 1/910 Hz (1.1 ms).

- tCycle duty cycle: 2.9 − 91.7%

## 2. Personal opinion on this practice

I found this practice to be quite easy to complete, and it took me very little time to complete the programs required. In my opinion, it's one of the practices I liked the most and found most interesting of all the practices we've completed in this course.

Below I explain how I carried out the two exercises required:

In the first exercise, I used the values ​​1 to 0 read from the keyboard to assign different speeds to both directions of the servo's rotation. As clearly specified in the program comments, I used the numbers 1 to 5 to go from the lowest to the highest speed when the servo rotates clockwise, as opposed to counterclockwise, where I set the numbers 0 to 6 (in that order), from lowest to highest speed, obtaining the following speed scheme: 1 < 2 < 3 < 4 < 5 = 6 > 7 > 8 > 9 > 0, with 1 to 5 being the values ​​for clockwise rotation (minimum speed 1 and maximum speed 5) and 6 to 0 being the values ​​for counterclockwise rotation (minimum speed 0 and maximum speed 6).

For the second exercise, I used the same methods as in the previous section. However, in this case, the only thing I've modified compared to the previous one is that I only set one rotation direction (clockwise), and I saved the values ​​that define these speed ranges in five different variables (MIN_SPEED for minimum speed, MAX_SPEED for maximum speed, and three more variables that I used for intermediate speed values).

As shown in the attached image, I connected the red wire to 5V, the black wire to GND, and the white wire to a specific GPIO port (in my case, I used GPIO port 2).

Although two exercises are required, I only uploaded one, since the programs operate the same, only changing the keys you need to press to obtain different speed values ​​in different directions (basically, the video is attached to demonstrate that the servo works).

## 3. Multimedia Content

<p align="center">
  <img src="https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%2010:%20Manejo%20de%20servo%20con%20retroalimentaci%C3%B3n%20posicional/media/Imagen%20Circuito%20Pr%C3%A1ctica%2010.jpg?raw=true">
</p>

[PRACTICE 10 EXECUTION VIDEO](https://github.com/aleon2020/SYA_2022-2023/blob/main/Pr%C3%A1cticas/Pr%C3%A1ctica%2010%3A%20Manejo%20de%20servo%20con%20retroalimentaci%C3%B3n%20posicional/media/Video%20Ejecuci%C3%B3n%20Pr%C3%A1ctica%2010.mp4)
