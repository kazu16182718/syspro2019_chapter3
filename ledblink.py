import time
import RPi.GPIO as GPIO

TIME = 1.0 
ROOP = 10

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

for i in range(ROOP):
    GPIO.output(14, GPIO.HIGH) 
    time.sleep(TIME)
    GPIO.output(14, GPIO.LOW)
    time.sleep(TIME)

GPIO.cleanup()
