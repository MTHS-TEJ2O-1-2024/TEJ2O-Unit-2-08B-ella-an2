"""
Created by: Mr. Coxall
Created on: Sep 2020
This module is a Micro:bit MicroPython program
"""

from microbit import *
from time import *

display.clear()
display.show(Image.HAPPY)

while True:
    if button_a.is_pressed():
        pin13.write_digital(1)
        pin14.write_digital(0)
        display("Blue")
        pin13.write_digital(0)

        time(1)

        pin14.write_digital(1)
        pin13.write_digital(0)
        pin15.write_digital(0)
        display("Green")
        pin14.write_digital(0)
        
        time(1)

        pin15.write_digital(1)
        pin14.write_digital(0)
        pin13.write_digital(0)
        display("Red")
        pin15.write_digital(0)

        time(1)

        pin14.write_digital(1)
        pin15.write_digital(1)
        pin13.write_digital(0)
        display("Yellow")
        pin14.write_digital(0)
        pin15.write_digital(0)

        time(1)

        pin15.write_digital(1)
        pin13.write_digital(1)
        pin14.write_digital(0)
        display("Purple")
        pin15.write_digital(0)
        pin13.write_digital(0)

        time(1)

        pin14.write_digital(1)
        pin13.write_digital(1)
        pin15.write_digital(0)
        display("Cyan")
        pin14.write_digital(0)
        pin13.write_digital(0)

        time(1)

        pin14.write_digital(1)
        pin13.write_digital(1)
        pin15.write_digital(0)
        display("White")
        pin14.write_digital(0)
        pin13.write_digital(0)
        pin15.write_digital(0)

        time(1)
        display.show(Image.HAPPY)
