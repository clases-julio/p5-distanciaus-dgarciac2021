#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import signal
import sys

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

TRIGGER_TIME = 10000

def callbackExit(signal, frame): # signal and frame when the interrupt was executed.
    GPIO.cleanup() # Clean GPIO resources before exit.
    sys.exit(0)

def measure(measures = 5, echoPin = PIN_ECHO, triggerPin = PIN_TRIGGER):
    measureSum = 0

    for measue in range(0, measures): 
        GPIO.output(PIN_TRIGGER, GPIO.HIGH)
        time.nanosleep(TRIGGER_TIME)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        while GPIO.input(PIN_ECHO)==0:
            inicioPulso = time.time()
        while GPIO.input(PIN_ECHO)==1:
            finPulso = time.time()

        measureSum = measureSum + ((finPulso - inicioPulso) * 17150)

    return round(measureSum/measures, 2)

def refreshData(data):
    print("                                        ", end="\r")
    print("Distancia: ", data, " cm", end="\r")

def main():
    while True:
        refreshData(measure())

        signal.signal(signal.SIGINT, callbackExit) # callback for CTRL+C

if __name__ == "__main__":
    main()
