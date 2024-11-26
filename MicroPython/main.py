"""
Created by: Ella
Created on: Sep 2024
This module is a Micro:bit MicroPython program
"""

from microbit import *
from time import *

# setup
display.clear()
display.show(Image.HAPPY)

while True:
    # when buttoon a is pressed
    if button_a.is_pressed():
        # blue lights up
        pin13.write_digital(1)
        pin14.write_digital(0)
        pin15.write_digital(0)
        display.scroll("Blue")
        pin13.write_digital(0)

        sleep(1)
        # green lights up
        pin14.write_digital(1)
        pin13.write_digital(0)
        pin15.write_digital(0)
        display.scroll("Green")
        pin14.write_digital(0)

        sleep(1)

        # red lights up
        pin15.write_digital(1)
        pin14.write_digital(0)
        pin13.write_digital(0)
        display.scroll("Red")
        pin15.write_digital(0)

        sleep(1)

        # yellow lights up
        pin14.write_digital(1)
        pin15.write_digital(1)
        pin13.write_digital(0)
        display.scroll("Yellow")
        pin14.write_digital(0)
        pin15.write_digital(0)

        sleep(1)

        # purple lights up
        pin15.write_digital(1)
        pin13.write_digital(1)
        pin14.write_digital(0)
        display.scroll("Purple")
        pin15.write_digital(0)
        pin13.write_digital(0)

        sleep(1)

        # cyan lights up
        pin14.write_digital(1)
        pin13.write_digital(1)
        pin15.write_digital(0)
        display.scroll("Cyan")
        pin14.write_digital(0)
        pin13.write_digital(0)

        sleep(1)

        # white lights up
        pin14.write_digital(1)
        pin13.write_digital(1)
        pin15.write_digital(1)
        display.scroll("White")
        pin14.write_digital(0)
        pin13.write_digital(0)
        pin15.write_digital(0)

        sleep(1)
        display.show(Image.HAPPY)
