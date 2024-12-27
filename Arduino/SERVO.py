#!/usr/bin/python

from pyfirmata import Arduino,SERVO
from time import sleep

port='COM5'
board=Arduino(port)
sleep(5);

pin=13
board.digital[pin].mode=SERVO

def setServoAngle(pin,angle:
        board.digital[pin].write(angle);
        sleep(0.015);

while


