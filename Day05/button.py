# 푸쉬버튼 예제
import RPi.GPIO as GPIO
import time
button = 24
count = 0
red = 17
green = 27
blue = 22

def click_Handler(channel):
    global count
    count = count + 1
    print(count)
    if (count % 2 == 0):
        GPIO.output(red, GPIO.LOW)
    else:
        GPIO.output(red, GPIO.HIGH)

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)





























GPIO.add_event_detect(button, GPIO.RISING, callback=click_Handler)

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

GPIO.output(red, 1)
GPIO.output(green, 1)
GPIO.output(blue, 1)

while (True):
    time.sleep(1)