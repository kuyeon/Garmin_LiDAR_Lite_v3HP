import Jetson.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT)

while True:
    GPIO.output(33, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(33, GPIO.LOW)
    time.sleep(1)