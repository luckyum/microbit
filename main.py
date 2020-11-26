def on_button_pressed_a():
    basic.show_icon(IconNames.HAPPY)
    strip.clear()
    # white
    strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.ORANGE))
    # blue
    # send the data to the strip
    strip.show()
    basic.pause(500)
    strip.clear()
    # red
    strip.set_pixel_color(2, neopixel.colors(NeoPixelColors.RED))
    # blue
    # send the data to the strip
    strip.show()
    basic.pause(500)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_icon(IconNames.SAD)
    strip.clear()
    # white
    strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.ORANGE))
    # blue
    # send the data to the strip
    strip.show()
    basic.pause(500)
    strip.clear()
    # red
    strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.GREEN))
    # blue
    # send the data to the strip
    strip.show()
    basic.pause(500)
input.on_button_pressed(Button.B, on_button_pressed_b)

strip: neopixel.Strip = None
# Create a NeoPixel driver - specify the pin, number of LEDs, and the type of
# the NeoPixel srip, either standard RGB (with GRB or RGB format) or RGB+White.
strip = neopixel.create(DigitalPin.P5, 4, NeoPixelMode.RGB)