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
        pin15.write_digital(0)
        display.scroll("Blue")
        pin13.write_digital(0)

        time(1)

        pin14.write_digital(1)
        pin13.write_digital(0)
        pin15.write_digital(0)
        display.scroll("Green")
        pin14.write_digital(0)

        time(1)

        pin15.write_digital(1)
        pin14.write_digital(0)
        pin13.write_digital(0)
        display.scroll("Red")
        pin15.write_digital(0)

        time(1)

        pin14.write_digital(1)
        pin15.write_digital(1)
        pin13.write_digital(0)
        display.scroll("Yellow")
        pin14.write_digital(0)
        pin15.write_digital(0)

        time(1)

        pin15.write_digital(1)
        pin13.write_digital(1)
        pin14.write_digital(0)
        display.scroll("Purple")
        pin15.write_digital(0)
        pin13.write_digital(0)

        time(1)

        pin14.write_digital(1)
        pin13.write_digital(1)
        pin15.write_digital(0)
        display.scroll("Cyan")
        pin14.write_digital(0)
        pin13.write_digital(0)

        time(1)

        pin14.write_digital(1)
        pin13.write_digital(1)
        pin15.write_digital(1)
        display.scroll("White")
        pin14.write_digital(0)
        pin13.write_digital(0)
        pin15.write_digital(0)

        time(1)
        display.show(Image.HAPPY)
