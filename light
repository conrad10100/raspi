import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,GPIO.HIGH)

for i in range (5):
    print(i+1 , "s")
    time.sleep(1)

GPIO.output(18,GPIO.LOW)
