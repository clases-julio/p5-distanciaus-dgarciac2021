# P5-DistanceUS

This exercise consists on measure distance with the help of the [HC-SR04 sensor](https://github.com/clases-julio/p5-distanciaus-dgarciac2021/wiki/HCSR04). You might want to take a look on the wiki, since there is info of everything involved on this project. From the [voltage divider](https://github.com/clases-julio/p5-distanciaus-dgarciac2021/wiki/Voltage-Divider) to the [library](https://github.com/clases-julio/p5-distanciaus-dgarciac2021/wiki/Bluetin-Python-Echo) used to manage the sensor.

## Circuit Assembly

The assembly is not that messy like the previous one, but in order to preserve the integrity of the Raspberry Pi board we have to make sure that the connections are correct, since there is risk of damaging the GPIO pins and even the board itself. We are using two RGB Leds, the HC-SR04 sensor and a buch of resistors listed down below:

|Nº|Value|
|---|---|
|2|10 Ω|
|1|47 Ω|
|1|1K Ω|
|1|2.2K Ω|

The larger ones are used to build a voltage divider which protects the Raspberry Pi GPIO from the 5V output from the HC-SR04.

This is an schematic made with [Fritzing](https://fritzing.org/):

![Schematic](./doc/img/schematic.png)

And this is the real circuit![^1]

![aerial view](./doc/img/aerial-view.jpg)

## Code

This time there is nothing really worth to mention here, since all particular procedures used in this exercise were documented on previous exercises, like [p4](https://github.com/clases-julio/p4-encoderoptico-dgarciac2021) or [p2](https://github.com/clases-julio/p2-gpio-ledrgb-dgarciac2021)

As for the [library](https://github.com/clases-julio/p5-distanciaus-dgarciac2021/wiki/Bluetin-Python-Echo) used, there is no fancy things beyond the examples that the very library provides.

We think that with that being said and with the comments included in the [source code](https://github.com/clases-julio/p5-distanciaus-dgarciac2021/blob/main/src/distanceSensor.py) is pretty enough to understand how it works!

## Circuit testing

This is the result! Pretty nice, isn't it?

![Circuit test](./doc/img/distanceSensorDemo.gif)

[^1]: In the real circuit two LEDs are used in order to reduce the overall brightness of each of them since the current provided by the GPIO will be equally distributed between them.
