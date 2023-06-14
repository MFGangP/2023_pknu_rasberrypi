# MQTT 패키지 설치 - paho-mqtt
# sudo pip install paho-mqtt
## 동시에 publish(데이터 전송[출판]) / subscribe(데이터 수신[구독]) 처리

from threading import Thread, Timer
import time # time.sleep()
import paho.mqtt.client as mqtt
import json
import datetime as dt

# DHT11 온습도 센서
import Adafruit_DHT as dht
# GPIO 
import RPi.GPIO as GPIO

# GPIO, DHT 설정
sensor = dht.DHT11
rcv_pin = 10
green = 22
servo_pin = 18

GPIO.setwarnings(False)
# green led init
GPIO.setmode(GPIO.BCM)
GPIO.setup(green, GPIO.OUT)
GPIO.output(green, GPIO.HIGH) # True
# servo init
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 100) # 서보모터 속도, 50 ~ 100 주파수 Hz
pwm.start(3) # 각도 0도 DutyCycle 3 ~ 20

# 내가 데이터를 보내는 객체
class publisher(Thread):
    def __init__(self):
        Thread.__init__(self) # 기본적인 스레드 초기화
        self.host = '210.119.12.66' # 본인 PC IP 적기
        self.count = 0
        self.port = 1883    # 회사에서는 이 포트 안쓴다
        self.clientId = 'IOT66'
        print('publisher 스레드 시작')
        self.client = mqtt.Client(client_id=self.clientId) # 설계대로

    def run(self):
        self.client.connect(self.host, self.port)
        # self.client.username_pw_set() # id/pwd로 로그인 할 때는 필요
        self.publish_data_auto()

    def publish_data_auto(self):
        humid, temp = dht.read_retry(sensor, rcv_pin)
        curr = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S') #2023-06-14 10:39:24
        origin_data = {'DEV_ID':self.clientId, 
                       'CURR_DT':curr,
                       'TYPE':'DEHUMD', 
                       'STAT':f'{temp}|{humid}'} # real DATA
        pub_data = json.dumps(origin_data) # MQTT로 전송할 json 데이터로 변환
        self.client.publish(topic='pknu/rpi/control/',
                            payload=pub_data)
        print(f'Data Published # {self.count}')
        self.count += 1
        time.sleep(1)
        Timer(3.0, self.publish_data_auto).start()
    
# 다른 곳 데이터를 받아오는 객체
class subscriber(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.host = '210.119.12.66' # Broker IP
        # self.host = 'https://lovehyun95.azure.com/iotservice'
        # self.host = 'lovehyun.iot.aws-region.amazonaws.com'
        self.port = 1883
        self.clientId = 'IOT66_SUB'
        self.topic = "pknu/monitor/control/"
        print('subscriber 스레드 시작')
        self.client = mqtt.Client(client_id=self.clientId) # 설계대로

    def run(self): # Thread.start() 함수를 실행하면 실행되는 함수
        self.client.on_connect = self.onConnect # 접속 성공 시그널 처리
        self.client.on_message = self.onMessage # 접속 후 메시지가 수신되면 처리 - 핵심
        self.client.connect(self.host, self.port)
        self.client.subscribe(topic=self.topic)
        self.client.loop_forever()

    def onConnect(self, mqttc, obj, flags, rc):
        print(f'sub:connected with rc > {rc}')

    def onMessage(self, mqttc, obj, msg):
        rcv_msg = str(msg.payload.decode('utf-8'))
        print(f'{msg.topic} / {rcv_msg}')
        data = json.loads(rcv_msg) # json data로 형변환
        stat = data['STAT']
        print(f'현재 stat : {stat}')
        if (stat == 'OPEN'):
            GPIO.output(green, GPIO.LOW)
            pwm.ChangeDutyCycle(12) # 90도
        elif (stat == 'CLOSE'):
            GPIO.output(green, GPIO.HIGH)
            pwm.ChangeDutyCycle(3) # 0도

        time.sleep(1.0)

if __name__ == '__main__':
    thPub = publisher() # publisher 객체 생성
    thSub = subscriber() # subscriber 객체 생성
    thPub.start() # run() 자동 실행
    thSub.start()