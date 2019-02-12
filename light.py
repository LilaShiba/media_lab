import board
import neopixel
import weather
import random
import time
from time import sleep

data = weather.url()
info = weather.parse_call(data)
icon = weather.parse_call(data)
temp = info[0]
#icon = info[1]
#summary = info[1]
icon = "thunderstorm"

print(icon)

pixels = neopixel.NeoPixel(board.D18, 180, brightness = 1)

num_pixels = 180

#if temp < 0:
    #pixels.fill((255,255,255))
    #count = 0
    #while count < 61:
    #    pixels[count] = (random.randint(0, 255), random.randint(0,255), random.randint(0, 255))
     #   count += 1
     
while icon == "thunderstorm": 
    pixels.fill((255,255,255))
    sleep(1)
    pixels.fill((255,255,255))
    sleep(1)
    
    
if icon == "rain":
    count = 0
    while count < 180:
        pixels[count] = (0,0,255)
        pixels.show()
        time.sleep(0.01)
        count += 1
        if count == 179:
            pixels.fill((0,0,0))
            count = 0


elif icon == "clear-day":
    pixels.fill((255,255,0))
elif icon == 'cloudy':
    pixels.fill((211,211,211))
elif icon == 'fog':
    pixels.fill((119,136,153))
elif icon == 'wind':
    pixels.fill((0,0,0))
elif icon == 'partly-cloudy-night':
    pixels.fill((25,25,112))
elif icon == 'clear-night':
    pixels.fill((255,255,224))


elif icon == "snow" or "hail":
    count = 0
    while count < 180:
        pixels[count] = (255,255,255)
        pixels.show()
        time.sleep(0.01)
        count += 1
        if count == 179:
            pixels.fill((0,0,0))
            count = 0

else:
    pixels.fill((255,255,0))
