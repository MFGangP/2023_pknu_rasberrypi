# 온습도 센서 DHT11
import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11 # 초 저가 센서
rcv_pin = 10

try:
    while True:
        humid, temp = Adafruit_DHT.read_retry(sensor, rcv_pin)
        if humid is not None and temp is not None:
            print(f'온도 : {temp}C / 습도 : {humid}%')
        else:
            print('센싱 에러!')
        time.sleep(1)

except Exception as ex:
    print(ex)

finally:
    print('프로그램 종료')