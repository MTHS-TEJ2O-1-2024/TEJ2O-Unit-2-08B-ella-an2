/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Ella
 * Created on: Oct 2024
 * This program turns on the RGB light in different colors
*/

basic.clearScreen()
basic.showIcon(IconNames.Happy)

input.onButtonPressed(Button.A, function () {
    pins.digitalWritePin(DigitalPin.P13, 1)
    basic.showString("Blue")
    pins.digitalWritePin(DigitalPin.P13, 0)

    pause(1)

    pins.digitalWritePin(DigitalPin.P14, 1)
    basic.showString("Green")
    pins.digitalWritePin(DigitalPin.P14, 0)

    pause(1)

    pins.digitalWritePin(DigitalPin.P15, 1)
    basic.showString("Red")
    pins.digitalWritePin(DigitalPin.P15, 0)

    pause(1)

    pins.digitalWritePin(DigitalPin.P15, 1)
    pins.digitalWritePin(DigitalPin.P14, 1)
    basic.showString("Yellow")
    pins.digitalWritePin(DigitalPin.P15, 0)
    pins.digitalWritePin(DigitalPin.P14, 0)

    pause(1)

    pins.digitalWritePin(DigitalPin.P15, 1)
    pins.digitalWritePin(DigitalPin.P13, 1)
    basic.showString("Magenta")
    pins.digitalWritePin(DigitalPin.P15, 0)
    pins.digitalWritePin(DigitalPin.P13, 0)

    pause(1)



})

