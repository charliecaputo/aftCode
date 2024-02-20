import RPi.GPIO as GPIO
import time
import curses

# Set GPIO mode and pins
GPIO.setmode(GPIO.BOARD)
PUL_PIN = 16
DIR_PIN = 12

# Set up GPIO pins
GPIO.setup(PUL_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)

# Function to control stepper motor
def stepper_control(direction):
    GPIO.output(DIR_PIN, direction)  # Set direction
    for x in range(100):  # 400 steps for a full revolution
        GPIO.output(PUL_PIN, GPIO.HIGH)
        time.sleep(0.001)  # Adjust delay for desired speed
        GPIO.output(PUL_PIN, GPIO.LOW)
        time.sleep(0.001)  # Adjust delay for desired speed

try:
    stdscr = curses.initscr()
    curses.noecho()
    stdscr.keypad(True)

    while True:
        char = stdscr.getch()
        if char == ord('q'):  # Quit if 'q' is pressed
            break
        elif char == curses.KEY_UP:  # Up arrow key
            stepper_control(GPIO.HIGH)  # Rotate clockwise
        elif char == curses.KEY_DOWN:  # Down arrow key
            stepper_control(GPIO.LOW)  # Rotate counter-clockwise

except KeyboardInterrupt:
    pass

finally:
    curses.endwin()
    GPIO.cleanup()

