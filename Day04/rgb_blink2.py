# LED RGB 깜빡이기
import RPi.GPIO as GPIO
import time
\
is_run = True
red = 17
green = 27
blue = 22

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

GPIO.output(red, 0)
GPIO.output(green, 0)
GPIO.output(blue, 0)

try:
    while(True):
        GPIO.output(red, 0)
        time.sleep(1)
        GPIO.output(red, 1)
        time.sleep(1)

        
except KeyboardInterrupt:
    GPIO.cleanup()