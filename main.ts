input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Happy)
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.Sad)
})
// Create a NeoPixel driver - specify the pin, number of LEDs, and the type of
// the NeoPixel srip, either standard RGB (with GRB or RGB format) or RGB+White.
let strip = neopixel.create(DigitalPin.P5, 4, NeoPixelMode.RGB)
basic.forever(function () {
    strip.clear()
    // red
    strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Green))
    // blue
    // send the data to the strip
    strip.show()
    basic.pause(1000)
    strip.clear()
    strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Orange))
    // blue
    // send the data to the strip
    strip.show()
    basic.pause(1000)
    strip.clear()
    // red
    strip.setPixelColor(2, neopixel.colors(NeoPixelColors.Red))
    // blue
    // send the data to the strip
    strip.show()
    basic.pause(1000)
    strip.clear()
    // white
    strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Orange))
    // blue
    // send the data to the strip
    strip.show()
    basic.pause(1000)
})
