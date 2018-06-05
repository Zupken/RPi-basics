import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
BUZZER = 4
ECHO = 18
TRIG = 17
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
while True:
    GPIO.output(TRIG, True)
    time.sleep(0.0001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO) is False:
        start = time.time()
    while GPIO.input(ECHO) is True:
        end = time.time()
    sig_time = end - start
    distance = sig_time / 0.00058
    if distance < 20:
        sleep = 0.1*distance
        GPIO.output(BUZZER, True)
        time.sleep(sleep)
        GPIO.output(BUZZER, False)
