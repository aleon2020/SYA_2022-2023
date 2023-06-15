# Resumen Sensores y Actuadores prácticas primer cuatrimestre

# Alberto León Luengo

## Grado de Ingeniería en Robótica Software

## Práctica 9: Uso del sensor de presión con el de presencia

### 1. El sensor de presencia FSR

Para utilizar el sensor de presencia he utilizado un esquema de conexión bastante sencillo, el cual ya se nos 
proporcionaba en el enunciado de esta práctica, que consiste básicamente en leer cada cierto tiempo (periodo corto)
los valores del sensor (LOW si no ha pasado nada cerca del sensor y HIGH si algo se ha movido o ha pasado cerca del sensor). Todo ello guardado en el fichero presencia.py.

Imagen: Ejercicio 1 apartado 1 (leer valores del sensor de presencia, ya sea LOW o HIGH)

https://urjc-my.sharepoint.com/:i:/g/personal/a_leon_2020_alumnos_urjc_es/EWc03QfFs7hAjENj1R3BeB8Befap_omD7GYVOUAx29hNMg?e=Y9rbf2

Video: Ejecución del ejercicio 1 apartado 1

https://urjc-my.sharepoint.com/:v:/g/personal/a_leon_2020_alumnos_urjc_es/EarYoGDY7MxCuBC5CfbqnTwBpbSsjrtxPobHryuakp1F5Q?e=no5vgO

### 2. El sensor de presión FSR

Al igual que para el caso anterior, ya se nos ha facilitado en el enunciado el esquema de conexión de dicho
sensor, y el código que he implementado es básicamente el mismo que he utilizado para leer los valores del sensor de presencia (LOW si no se está presionando la parte circular del sensor y HIGH si la estamos presionando). Todo ello guardado en el fichero fuerza.py.

Imagen: Ejercicio 1 apartado 2 (leer los valores del sensor de presión, ya sea LOW o HIGH).

https://urjc-my.sharepoint.com/:i:/g/personal/a_leon_2020_alumnos_urjc_es/EQGp9CrbpVhBkr52lOW5m6QBiZCKdO1ycxfcNrQC-Z0R_A?e=V4azrM

Video: Ejecución del ejercicio 1 apartado 2

https://urjc-my.sharepoint.com/:v:/g/personal/a_leon_2020_alumnos_urjc_es/EY0r4IhXGXhJiZB65Q1XCbgB2XnMvk3_Mct-BZsy8Q2fCg?e=tyBzDM

### 3. Opinión personal sobre esta práctica

Esta opinión está más centrada en el apartado 2 de esta práctica, donde se nos pide diseñar un sistema de iluminación
inteligente utilizando los sensores de presencia y de presión, añadiéndole la implementación de un LED, el cual se encenderá
cuando el sensor de presencia muestre por su salida HIGH, todo ello siempre y cuando el sensor de presión también esté en modo HIGH, ya que para este caso, utilizaremos este sensor a modo de botón (si se encuentra en estado LOW no funciona nada, pero si se encuentra en estado HIGH, sólo en ese instante puede funcionar el sensor de presencia, y encenderá el LED cada vez que detecte presencia).

Est apartado de la práctica me ha sido más complicado de llevar a cabo ya que he tenido que usar hilos y la "complejidad" que tenía el sincronizar la ejecución de 
todos los elementos presentes en el circuito. Según se puede ver en el vídeo, el programa comienza a ejecutarse, el sensor de presión funciona en este caso como botón (cuando lo pulsemos se activará por un tiempo específico, en mi 
caso han sido 30 segundos, el sensor de presencia, que a su vez, cuando su salida sea HIGH, es decir, que haya detectado algo, se encenderá el led rojo), y cuando ya llevemos un largo tiempo psando un objeto cerca del sensor de presencia 
y no detecte nada, siginificará que el tiempo que habíamos establecido previamente (30 segundos) ya ha expirado, y por tanto, debemos de pulsar de nuevo el sensor de presión que está a modo de botón para que el sensor de presencia pueda llevar a cabo su trabajo.

### 4. Contenido multimedia sobre esta práctica

Imagen: Montaje del circuito del ejercicio 2 (diseño de un sistema de iluminación inteligente)

https://urjc-my.sharepoint.com/:i:/g/personal/a_leon_2020_alumnos_urjc_es/ER5o3-IxwfVGoesqwNWbMJwBw7urjK_KlUtCA4RYeI11Ew?e=StBpFq

Vídeo: Ejecución del apartado 2 (diseño de un sistema de iluminación inteligente)

https://urjc-my.sharepoint.com/:v:/g/personal/a_leon_2020_alumnos_urjc_es/Eck1xqUZYztNqfY0AlUw_WEBLqXnzDv5ny4TUrXyD9HtUQ?e=PQRQoJ
