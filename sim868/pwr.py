import time
import RPi.GPIO as GPIO

GPIO_4 = 7

def toggle():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(GPIO_4, GPIO.OUT)
	GPIO.output(GPIO_4, GPIO.LOW)
	time.sleep(2)
	GPIO.output(GPIO_4, GPIO.HIGH)


