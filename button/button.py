import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO18

try:
    while True:
         button_state = GPIO.input(18)
         if button_state == False:
             print('Button Pressed...')
             time.sleep(0.2)
except:
    GPIO.cleanup()
