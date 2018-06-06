#coding:UTF-8
import RPi.GPIO as GPIO
import time

SW1=21
LED1=7

oof = False

GPIO.setmode(GPIO.BCM)

GPIO.setup(SW1,GPIO.IN)

GPIO.setup(LED1,GPIO.OUT)


while True:
	if GPIO.input(SW1)==GPIO.HIGH:
	
		if oof==False:
			GPIO.output(LED1,GPIO.LOW)
			oof=True
		else:
			GPIO.output(LED1,GPIO.HIGH)
			oof=False

		time.sleep(1)
