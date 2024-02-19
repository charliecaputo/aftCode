import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

# GPIO Setup
DIR = 12  # DIR+ GPIO pin
STEP = 16  # PUL+ GPIO pin

CW = 1
CCW = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)


# Set Direction
GPIO.output(DIR, CW)  # Low will go opposite direction
count = 0

try:
    start = time.time()
    for i in range(50):
        print(i)
        GPIO.output(DIR, CCW)
        
        for x in range(100):
            GPIO.output(STEP, GPIO.HIGH)  # Sets voltage to on/1
            time.sleep(.00023)
            GPIO.output(STEP, GPIO.LOW)  # Sets voltage to off/0
            time.sleep(.00023)
    
    print((time.time() - start))
except KeyboardInterrupt:
    print('Clean up')
    GPIO.cleanup()
