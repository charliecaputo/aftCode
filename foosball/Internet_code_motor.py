# Import necessary libraries
"""
make this code run the motor without keybaord commands
"""
import RPi.GPIO as GPIO
import time

# Set GPIO mode (BCM or BOARD)
GPIO.setmode(GPIO.BOARD)

# Define motor pins
DIR_PIN = 12  # Direction pin
PUL_PIN = 16  # Pulse pin


# Set up GPIO pins
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(PUL_PIN, GPIO.OUT)

# Set initial direction (1 for clockwise, 0 for counterclockwise)
direction = 1

# Set motor speed (adjust as needed)
delay = 0.001  # Time delay between steps (in seconds) for 1 revolution per 2 seconds

for x in range(1):  # 400 steps for a full revolution
        GPIO.output(PUL_PIN, GPIO.HIGH)
        time.sleep(.1)  # Adjust delay for desired speed
        GPIO.output(PUL_PIN, GPIO.LOW)
        time.sleep(.1)  # Adjust delay for desired speed

