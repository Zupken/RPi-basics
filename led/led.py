import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
for i in range(100):
	GPIO.output(18, 1)
	time.sleep(0.2)
	GPIO.output(18, 0)
	time.sleep(0.2)
GPIO.cleanup()
	
