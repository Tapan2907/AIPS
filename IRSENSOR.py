import RPi.GPIO as GPIO
import os
import pyautogui
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN)

while True:
 i = GPIO.input(27)
 if i==1:
     #os.system('python detect.py')

gpio.cleanup()