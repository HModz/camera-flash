import time
from brightpi import *
from picamera import PiCamera
camera = PiCamera()
f = BrightPi()
f.set_gain(15)
def PhotoShot():
    camera.start_preview()
    time.sleep(2)
    f.set_led_on_off(LED_ALL, ON)
    for filename in camera.capture_continuous('img{counter:03d}.jpg'): 
        f.set_led_on_off(LED_ALL, OFF)
        time.sleep(5)
        f.set_led_on_off(LED_ALL, ON)
while True:
    PhotoShot()

