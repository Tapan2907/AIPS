import cv2
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)
counter=0
GPIO.setup(27,GPIO.LOW)
while(counter!=60):
    print("LED on")
    GPIO.output(21,GPIO.HIGH)
    time.sleep(0.05)
    print("LED off")
    GPIO.output(21,GPIO.LOW)
    time.sleep(0.05)
    counter+=1
GPIO.cleanup()
