#!/usr/bin/python
import RPi.GPIO as GPIO
import time

try:
      GPIO.setmode(GPIO.BCM)

      PIN_TRIGGER = 21
      PIN_ECHO = 20
      PIN_R = 14
      PIN_G = 15
      PIN_B = 18

      GPIO.setup(PIN_TRIGGER, GPIO.OUT)
      GPIO.setup(PIN_R, GPIO.OUT)
      GPIO.setup(PIN_G, GPIO.OUT)
      GPIO.setup(PIN_B, GPIO.OUT)
      GPIO.setup(PIN_ECHO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

      GPIO.output(PIN_TRIGGER, GPIO.LOW)
      GPIO.output(PIN_R, GPIO.LOW)
      GPIO.output(PIN_G, GPIO.LOW)
      GPIO.output(PIN_B, GPIO.LOW)

      print("Esperando a que se estabilice el US")
      time.sleep(2)

      GPIO.output(PIN_TRIGGER, GPIO.HIGH)
      time.sleep(0.00001)
      GPIO.output(PIN_TRIGGER, GPIO.LOW)

      while GPIO.input(PIN_ECHO)==0:
            inicioPulso = time.time()
      while GPIO.input(PIN_ECHO)==1:
            finPulso = time.time()

      duracionPulso = finPulso - inicioPulso
      distancia = round(duracionPulso * 17150, 2)
      print("Distancia: ", distancia, " cm")

finally:
      GPIO.cleanup()
      
