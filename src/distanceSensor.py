#!/usr/bin/python

###############################################################################
# distanceSensor.py                                                           #
#                                                                             #
# Authors: Ioana Carmen, Diego García                                         #
#                                                                             #
# This code will drive a LED depending on the distance measured by an         #
# ultrasonic sensor.                                                          #
###############################################################################

###############################################################################
# Neccesary modules

import RPi.GPIO as GPIO
import time
import signal
import sys

from Bluetin_Echo import Echo

###############################################################################
# Pinout management

GPIO.setmode(GPIO.BCM)

PIN_TRIGGER = 21
PIN_ECHO = 20
PIN_R = 14
PIN_G = 15
PIN_B = 18

## Sensor Object creation

# Calibrate sensor with initial speed of sound m/s value 
SPEED_OF_SOUND = 343
# Initialise Sensor with pins, speed of sound.
echo = Echo(PIN_TRIGGER, PIN_ECHO, SPEED_OF_SOUND)

GPIO.setup(PIN_R, GPIO.OUT)
GPIO.setup(PIN_G, GPIO.OUT)
GPIO.setup(PIN_B, GPIO.OUT)

###############################################################################
# Pinout initialization

GPIO.output(PIN_R, GPIO.LOW)
GPIO.output(PIN_G, GPIO.LOW)
GPIO.output(PIN_B, GPIO.LOW)

###############################################################################
# Global variables

# There are three regions in total
# - region 1: below lower limit
# - region 2: between lower and upper limit.
# - region 3: above upper limit.

LOWER_LIMIT = 10.0
UPPER_LIMIT = 20.0

colors = {"red": 4, "green": 2, "blue": 1, "cyan": 3, "magenta": 5, "yellow": 6, "white": 7, "black": 0}
# Each color is represented by the decimal number which gives each component value in binary.
# Red = 4 (dec) = 100 (bin) --> rValue = 1, gValue = 0, bValue = 0.
# ...

###############################################################################
# Global methods

def callbackExit(signal, frame): # signal and frame when the interrupt was executed.
    GPIO.cleanup() # Clean GPIO resources before exit.
    sys.exit(0)

def refreshData(data):
    print("                                        ", end="\r")
    # Erase the current line and returns carriage to the start of said line.
    print("Distance: ", round(data, 2), " cm", end="\r")
    # returns the carriage to the start of the line for next refresh.

def setLED(color):
    rValue, gValue, bValue = bin(colors[color])[2:].zfill(3)
    # Parse the value of each color needed on RGB as a binary number.
    # They represent the value of each pin which drives each color.

    rValue, gValue, bValue = bool(int(rValue)), bool(int(gValue)), bool(int(bValue))
    # The previous step returns each binary value in <<str>> format, so it is needed
    # to cast them to booleans.

    GPIO.output(PIN_R, rValue)
    GPIO.output(PIN_G, gValue)
    GPIO.output(PIN_B, bValue)

def driveLed(distance):
    if (echo.error_code == 0): # Echo could return 1 or 2 based on detected errors.
        if(distance <= LOWER_LIMIT):
            setLED("red")
        elif(distance <= UPPER_LIMIT):
            setLED("yellow")
        else:
            setLED("green")
    else: setLED("black") # If any error detected, turn off the LED.

###############################################################################
# Main program

def main():
    print("CTRL + C to exit!", end="\n\n")

    while True:
        time.sleep(0.06) # Min value tested to leave the sensor "rest"
        result, samples = echo.samples(5)
        refreshData(result)
        driveLed(result)
        signal.signal(signal.SIGINT, callbackExit) # callback for CTRL+C

if __name__ == "__main__":
    main()
