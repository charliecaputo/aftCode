import RPi.GPIO as GPIO
import time

# GPIO pins for PUL and DIR
PUL_PIN = 12
DIR_PIN = 16

# Set up GPIO mode and pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PUL_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)

# Set initial direction (clockwise)
GPIO.output(DIR_PIN, GPIO.HIGH)

# Function to make one step
def step():
    GPIO.output(PUL_PIN, GPIO.HIGH)
    time.sleep(0.005)  # Adjust this delay as needed for your motor
    GPIO.output(PUL_PIN, GPIO.LOW)
    time.sleep(0.005)  # Adjust this delay as needed for your motor

# Function to make continuous revolutions
def continuous_rotation(rev_per_minute):
    delay = 60.0 / (400 * rev_per_minute)  # Assuming 200 steps per revolution
    while True:
        step()
        time.sleep(delay)

try:
    continuous_rotation(30)  # Adjust 30 to desired revolutions per minute
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

