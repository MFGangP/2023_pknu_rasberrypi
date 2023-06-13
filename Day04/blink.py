# LED 깜빡이기
import RPi.GPIO as GPIO
import time

signal_pin = 18

# GPIO.setmode(GPIO.BORAD) # 1~40 핀번호
GPIO.setmode(GPIO.BCM) # GPIO 18, GROUND 핀 고유이름
GPIO.setup(signal_pin, GPIO.OUT) # GPIO 18핀에 출력을 설정

while (True):
    GPIO.output(signal_pin, True) # GPIO 18번 핀에 전압 시그널 ON
    time.sleep(0.1) # 1초동안 불을 켬
    GPIO.output(signal_pin, False) # GPIO 18번 핀에 전압 시그널 OFF
    time.sleep(0.1) # 1초동안 불을 켬