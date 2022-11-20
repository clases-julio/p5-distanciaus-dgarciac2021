#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import signal
import sys

from Bluetin_Echo import Echo

GPIO.setmode(GPIO.BCM)

PIN_TRIGGER = 21
PIN_ECHO = 20
PIN_R = 14
PIN_G = 15
PIN_B = 18

""" Calibrate sensor with initial speed of sound m/s value """
SPEED_OF_SOUND = 343
""" Initialise Sensor with pins, speed of sound. """
echo = Echo(PIN_TRIGGER, PIN_ECHO, SPEED_OF_SOUND)

GPIO.setup(PIN_R, GPIO.OUT)
GPIO.setup(PIN_G, GPIO.OUT)
GPIO.setup(PIN_B, GPIO.OUT)

GPIO.output(PIN_R, GPIO.LOW)
GPIO.output(PIN_G, GPIO.LOW)
GPIO.output(PIN_B, GPIO.LOW)

def callbackExit(signal, frame): # signal and frame when the interrupt was executed.
    GPIO.cleanup() # Clean GPIO resources before exit.
    echo.stop()
    sys.exit(0)

def refreshData(data):
    print("                                        ", end="\r")
    print("Distancia: ", round(data, 2), " cm", end="\r")

def main():
    while True:
        signal.signal(signal.SIGINT, callbackExit) # callback for CTRL+C
        time.sleep(0.10)
        result, samples = echo.samples(10)
        refreshData(result)

if __name__ == "__main__":
    main()
