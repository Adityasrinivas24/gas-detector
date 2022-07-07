import time
import RPi.GPIO as GPIO

SENSOR_PIN = 12

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def read_value():
    return 0

def is_threshold_reached():
    return False if GPIO.input(SENSOR_PIN) else True