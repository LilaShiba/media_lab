import board
import neopixel
import weather
import random
from time import sleep

data = weather.url()
info = weather.parse_call(data)
summary = weather.parse_call(data)
temp = info[0]
#summary = info[1]
summary = "raining"
print(summary)

pixels = neopixel.NeoPixel(board.D18, 180, brightness = 1)

if summary == "raining":
    count = 0
    pixels.fill((0,255,0))
    for pixel in pixels:
        while count < 180:
            count += 1
            pixels.fill((255,255,255))
        