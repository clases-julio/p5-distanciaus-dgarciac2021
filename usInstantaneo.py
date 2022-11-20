#!/usr/bin/python
import RPi.GPIO as GPIO
import time

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

TRIGGER_TIME = 0.00001

def callbackExit(signal, frame): # signal and frame when the interrupt was executed.
    GPIO.cleanup() # Clean GPIO resources before exit.
    sys.exit(0)

def main():
    while True:
        GPIO.output(PIN_TRIGGER, GPIO.HIGH)
        time.sleep(TRIGGER_TIME)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        while GPIO.input(PIN_ECHO)==0:
            inicioPulso = time.time()
        while GPIO.input(PIN_ECHO)==1:
            finPulso = time.time()

        duracionPulso = finPulso - inicioPulso
        distancia = round(duracionPulso * 17150, 2)
        print("Distancia: ", distancia, " cm", end="\r")

        signal.signal(signal.SIGINT, callbackExit) # callback for CTRL+C

if __name__ == "__main__":
    main()
